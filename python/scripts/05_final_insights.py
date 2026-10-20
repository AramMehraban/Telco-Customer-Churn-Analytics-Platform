from pathlib import Path

import pandas as pd

from common import OUTPUT_DIR, load_features, normalize_churn, require_columns


def main():
    df = normalize_churn(load_features())

    require_columns(
        df,
        ["churn", "contract", "monthlycharges", "tenure"],
    )

    df["monthlycharges"] = pd.to_numeric(
        df["monthlycharges"], errors="coerce"
    )
    df["tenure"] = pd.to_numeric(df["tenure"], errors="coerce")

    customers = len(df)
    churned = int(df["churn"].eq("yes").sum())
    churn_rate = churned / customers * 100 if customers else 0

    contract_churn = (
        df.groupby("contract", dropna=False)["churn"]
        .apply(lambda s: s.eq("yes").mean() * 100)
        .sort_values(ascending=False)
    )

    insights = [
        "# Telco Customer Churn — Final Insights",
        "",
        "## Executive Summary",
        "",
        f"- Customers analyzed: {customers:,}",
        f"- Churned customers: {churned:,}",
        f"- Overall churn rate: {churn_rate:.2f}%",
        "",
        "## Contract Analysis",
        "",
    ]

    for contract, rate in contract_churn.items():
        insights.append(f"- {contract}: {rate:.2f}% churn rate")

    if "internetservice" in df.columns:
        internet_churn = (
            df.groupby("internetservice", dropna=False)["churn"]
            .apply(lambda s: s.eq("yes").mean() * 100)
            .sort_values(ascending=False)
        )

        insights.extend(["", "## Internet Service Analysis", ""])

        for service, rate in internet_churn.items():
            insights.append(f"- {service}: {rate:.2f}% churn rate")

    insights.extend([
        "",
        "## Recommended Next Steps",
        "",
        "1. Investigate the high churn rate among month-to-month customers.",
        "2. Evaluate onboarding and retention initiatives for newer customers.",
        "3. Investigate service quality, pricing, and support among high-churn segments.",
        "4. Test targeted retention campaigns and measure results against a baseline.",
        "5. Monitor churn and retention metrics over time.",
        "",
        "## Interpretation and Limitations",
        "",
        "- Segment-level churn rates show associations, not causation.",
        "- Heuristic risk scores are not calibrated churn probabilities.",
        "- Historical charges are not future revenue or customer lifetime value.",
        "- Recommendations should be validated with additional analysis.",
    ])

    report = "\n".join(insights) + "\n"
    output = OUTPUT_DIR / "final_insights.md"
    output.write_text(report, encoding="utf-8")

    print(report)
    print(f"\nReport saved to: {output}")


if __name__ == "__main__":
    main()