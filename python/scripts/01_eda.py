import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd

from common import (
    OUTPUT_DIR,
    load_clean_data,
    normalize_churn,
    require_columns,
    save_output,
)


def main():
    df = normalize_churn(load_clean_data())

    require_columns(
        df,
        ["churn", "tenure", "monthlycharges", "totalcharges"],
    )

    for column in ["tenure", "monthlycharges", "totalcharges"]:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    df = df.dropna(subset=["churn"])
    df = df[df["churn"].isin(["yes", "no"])].copy()

    # Overall churn summary
    summary = (
        df["churn"]
        .value_counts()
        .rename_axis("churn")
        .reset_index(name="customers")
    )
    summary["percentage"] = (
        summary["customers"] / len(df) * 100
    ).round(2)

    save_output(summary, "churn_summary.csv")

    # Contract churn
    if "contract" in df.columns:
        contract = (
            df.groupby("contract", dropna=False)
            .agg(
                customers=("churn", "size"),
                churned=("churn", lambda s: s.eq("yes").sum()),
            )
            .reset_index()
        )
        contract["churn_rate"] = (
            contract["churned"] / contract["customers"] * 100
        ).round(2)
        save_output(contract, "contract_churn.csv")

    # Internet service churn
    if "internetservice" in df.columns:
        internet = (
            df.groupby("internetservice", dropna=False)
            .agg(
                customers=("churn", "size"),
                churned=("churn", lambda s: s.eq("yes").sum()),
            )
            .reset_index()
        )
        internet["churn_rate"] = (
            internet["churned"] / internet["customers"] * 100
        ).round(2)
        save_output(internet, "internet_churn.csv")

    # Monthly charges by churn status
    monthly = (
        df.groupby("churn")["monthlycharges"]
        .agg(["count", "mean", "median", "min", "max"])
        .reset_index()
        .round(2)
    )
    save_output(monthly, "monthly_charges_by_churn.csv")

    # Tenure by churn status
    tenure = (
        df.groupby("churn")["tenure"]
        .agg(["count", "mean", "median", "min", "max"])
        .reset_index()
        .round(2)
    )
    save_output(tenure, "tenure_by_churn.csv")

    # Total charges by churn status
    total_charges = (
        df.groupby("churn")["totalcharges"]
        .agg(["count", "mean", "median", "min", "max"])
        .reset_index()
        .round(2)
    )
    save_output(total_charges, "total_charges_by_churn.csv")

    # Payment method churn
    if "paymentmethod" in df.columns:
        payment = (
            df.groupby("paymentmethod", dropna=False)
            .agg(
                customers=("churn", "size"),
                churned=("churn", lambda s: s.eq("yes").sum()),
            )
            .reset_index()
        )
        payment["churn_rate"] = (
            payment["churned"] / payment["customers"] * 100
        ).round(2)
        save_output(payment, "payment_churn.csv")

    # Plot churn counts
    counts = df["churn"].value_counts().reindex(["no", "yes"], fill_value=0)

    fig, ax = plt.subplots(figsize=(7, 5))
    counts.plot(kind="bar", ax=ax)
    ax.set_title("Customer Churn Distribution")
    ax.set_xlabel("Churn")
    ax.set_ylabel("Number of customers")
    ax.tick_params(axis="x", rotation=0)
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "churn_distribution.png", dpi=150)
    plt.close(fig)

    print(f"\nEDA complete. Customers analyzed: {len(df):,}")


if __name__ == "__main__":
    main()