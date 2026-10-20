
import numpy as np
import pandas as pd

from common import PROCESSED_DIR, load_clean_data, normalize_churn, require_columns


def main():
    df = normalize_churn(load_clean_data())

    require_columns(
        df,
        ["churn", "tenure", "monthlycharges", "totalcharges",
         "contract", "paymentmethod"],
    )

    for column in ["tenure", "monthlycharges", "totalcharges"]:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    df["churn_flag"] = df["churn"].eq("yes").astype(int)
    df["active_flag"] = df["churn"].eq("no").astype(int)

    df["tenure_group"] = pd.cut(
        df["tenure"],
        bins=[-1, 12, 24, 48, 72],
        labels=["0-12 Months", "13-24 Months",
                "25-48 Months", "49-72 Months"],
        include_lowest=True,
    )

    df["monthly_charges_group"] = pd.cut(
        df["monthlycharges"],
        bins=[0, 30, 60, 90, np.inf],
        labels=["0-30", "30-60", "60-90", "90+"],
        include_lowest=True,
    )

    # Historical charges are not customer lifetime value.
    df["historical_charges"] = df["totalcharges"]

    safe_tenure = df["tenure"].replace(0, np.nan)
    df["average_charges_per_tenure_month"] = (
        df["totalcharges"] / safe_tenure
    ).fillna(df["monthlycharges"])

    if "internetservice" in df.columns:
        df["has_internet"] = (
            df["internetservice"].astype("string").str.lower().ne("no")
        ).astype(int)

    service_columns = [
        "phoneservice", "onlinesecurity", "onlinebackup",
        "deviceprotection", "techsupport", "streamingtv",
        "streamingmovies", "multiplelines",
    ]
    existing = [c for c in service_columns if c in df.columns]

    if existing:
        df["service_count"] = sum(
            df[c].astype("string").str.lower().eq("yes").astype(int)
            for c in existing
        )

    # Transparent heuristic score, not a trained churn model.
    score = pd.Series(0, index=df.index, dtype="int64")

    score += df["contract"].astype("string").str.lower().eq(
        "month-to-month"
    ).astype(int) * 30

    score += df["tenure"].le(12).fillna(False).astype(int) * 20
    score += df["monthlycharges"].ge(80).fillna(False).astype(int) * 20

    score += df["paymentmethod"].astype("string").str.lower().eq(
        "electronic check"
    ).astype(int) * 20

    support_columns = [
        c for c in ["onlinesecurity", "techsupport"] if c in df.columns
    ]

    if support_columns:
        no_support = pd.Series(True, index=df.index)

        for column in support_columns:
            no_support &= (
                df[column].astype("string").str.lower().eq("no")
            )

        score += no_support.astype(int) * 10

    df["risk_score"] = score.clip(upper=100)

    df["risk_category"] = pd.cut(
        df["risk_score"],
        bins=[-1, 29, 59, 79, 100],
        labels=["Low", "Medium", "High", "Very High"],
    )

    # Monthly charges associated with churned customers at churn.
    # This is not current recurring revenue.
    df["monthly_charges_at_churn"] = np.where(
        df["churn_flag"].eq(1),
        df["monthlycharges"],
        0,
    )

    output = PROCESSED_DIR / "customer_churn_features.csv"
    df.to_csv(output, index=False)

    print(f"Saved feature dataset: {output}")
    print(f"Rows: {len(df):,}; columns: {len(df.columns):,}")
    print("\nRisk categories:")
    print(df["risk_category"].value_counts(dropna=False))


if __name__ == "__main__":
    main()
