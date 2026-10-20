import pandas as pd

from common import load_features, normalize_churn, require_columns, save_output


def main():
    df = normalize_churn(load_features())

    require_columns(
        df,
        ["churn", "monthlycharges", "totalcharges"],
    )

    for column in ["monthlycharges", "totalcharges"]:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    # Historical charges grouped by churn status
    historical = (
        df.groupby("churn", dropna=False)
        .agg(
            customers=("churn", "size"),
            historical_charges=("totalcharges", "sum"),
            average_historical_charges=("totalcharges", "mean"),
            median_historical_charges=("totalcharges", "median"),
        )
        .reset_index()
        .round(2)
    )
    save_output(historical, "revenue_historical_by_churn.csv")

    # Monthly charges associated with churned customers
    churned = df[df["churn"].eq("yes")].copy()

    churned_monthly = pd.DataFrame(
        [{
            "churned_customers": len(churned),
            "monthly_charges_at_churn": round(
                churned["monthlycharges"].sum(), 2
            ),
            "average_monthly_charges_at_churn": round(
                churned["monthlycharges"].mean(), 2
            ),
            "historical_charges_of_churned_customers": round(
                churned["totalcharges"].sum(), 2
            ),
        }]
    )
    save_output(churned_monthly, "revenue_exposure_summary.csv")

    # Monthly charges for customers who have not churned
    active = df[df["churn"].eq("no")]

    active_monthly = pd.DataFrame(
        [{
            "active_customers": len(active),
            "monthly_charges_of_active_customers": round(
                active["monthlycharges"].sum(), 2
            ),
        }]
    )
    save_output(active_monthly, "active_customer_monthly_charges.csv")

    # Optional contract-level analysis
    if "contract" in df.columns:
        contract = (
            df.groupby("contract", dropna=False)
            .agg(
                customers=("churn", "size"),
                historical_charges=("totalcharges", "sum"),
                monthly_charges=("monthlycharges", "sum"),
            )
            .reset_index()
            .round(2)
        )
        save_output(contract, "revenue_by_contract.csv")

    print("\nRevenue exposure summary:")
    print(churned_monthly.to_string(index=False))

    print(
        "\nImportant: charges associated with churned customers "
        "are estimates of exposure, not current recurring revenue."
    )


if __name__ == "__main__":
    main()
    