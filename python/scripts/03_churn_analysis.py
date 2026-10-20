import pandas as pd

from common import load_features, normalize_churn, require_columns, save_output


def churn_by_segment(df, column, filename):
    result = (
        df.groupby(column, dropna=False, observed=True)
        .agg(
            customers=("churn_flag", "size"),
            churned=("churn_flag", "sum"),
        )
        .reset_index()
    )

    result["churn_rate_pct"] = (
        result["churned"] / result["customers"] * 100
    ).round(2)

    save_output(result, filename)
    return result


def main():
    df = normalize_churn(load_features())

    if "churn_flag" not in df.columns:
        df["churn_flag"] = df["churn"].eq("yes").astype(int)

    require_columns(df, ["churn_flag"])

    overall = pd.DataFrame(
        [{
            "customers": len(df),
            "churned": int(df["churn_flag"].sum()),
            "churn_rate_pct": round(df["churn_flag"].mean() * 100, 2),
        }]
    )
    save_output(overall, "churn_analysis_overall.csv")

    segments = [
        ("contract", "contract_churn_analysis.csv"),
        ("internetservice", "internet_churn_analysis.csv"),
        ("paymentmethod", "payment_churn_analysis.csv"),
        ("tenure_group", "tenure_churn_analysis.csv"),
        ("risk_category", "risk_category_churn_analysis.csv"),
    ]

    for column, filename in segments:
        if column in df.columns:
            churn_by_segment(df, column, filename)

    print("\nOverall churn analysis:")
    print(overall.to_string(index=False))


if __name__ == "__main__":
    main()