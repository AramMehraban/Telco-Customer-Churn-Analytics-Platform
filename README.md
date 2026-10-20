# Telco Customer Churn Analytics Platform

**End-to-End Data Analytics Portfolio Project**

[🚀 Live Dashboard](https://telco-customer-churn-analysis-platform.streamlit.app/) | [📂 GitHub Repository](https://github.com/AramMehraban/Telco-Customer-Churn-Analytics-Platform)

An end-to-end customer churn analytics portfolio project built with Python, SQL, Jupyter Notebook, and Streamlit. This project analyzes customer retention, contract types, service usage, churn risk indicators, and revenue exposure to support data-driven business decisions.

---

## Table of Contents

- [Overview](#overview)
- [Business Objectives](#business-objectives)
- [Business Questions](#business-questions)
- [Key Findings](#key-findings)
- [Dashboard](#dashboard)
- [Project Workflow](#project-workflow)
- [Technology Stack](#technology-stack)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Running the Dashboard](#running-the-dashboard)
- [Running the Analysis Scripts](#running-the-analysis-scripts)
- [Deployment](#deployment)
- [Business Value](#business-value)
- [Limitations](#limitations)
- [Future Improvements](#future-improvements)
- [Author](#author)

---

## Overview

Customer churn is a major challenge for subscription-based businesses. Understanding why customers leave helps organizations identify vulnerable customer segments, improve retention strategies, and make better business decisions.

This project presents an end-to-end customer churn analytics workflow, from data preparation and exploratory analysis to feature engineering, churn investigation, revenue impact assessment, and interactive dashboard development.

The project combines Python-based analytics, SQL workflows, Jupyter notebooks, and an interactive Streamlit dashboard to communicate findings in a business-oriented format.

**Explore the live application:** [Telco Customer Churn Analytics Dashboard](https://telco-customer-churn-analysis-platform.streamlit.app/)

## Business Objectives

- Measure customer churn and compare churn rates across customer segments.
- Identify customer characteristics associated with higher churn.
- Investigate relationships between churn, contract type, tenure, internet service, and payment method.
- Engineer additional analytical features to support segmentation and risk assessment.
- Examine historical charges associated with customers who churned.
- Present analytical results through an interactive dashboard.
- Translate findings into practical, measurable customer-retention recommendations.

## Business Questions

This project addresses the following questions:

1. What percentage of customers have churned?
2. How does churn vary across month-to-month, one-year, and two-year contracts?
3. Which internet service segments have higher observed churn rates?
4. How does churn differ by payment method?
5. How are customer tenure and monthly charges associated with churn?
6. Which customer segments may warrant further retention analysis?
7. What historical charges are associated with customers who have churned?
8. How can the findings inform customer-retention strategies?

## Key Findings

The current analysis covers **7,043 customers**, including **1,869 customers who churned**.

| Metric | Result |
|---|---:|
| Total customers analyzed | 7,043 |
| Churned customers | 1,869 |
| Overall churn rate | 26.54% |
| Month-to-month contract churn rate | 42.71% |
| One-year contract churn rate | 11.27% |
| Two-year contract churn rate | 2.83% |
| Fiber optic customer churn rate | 41.89% |
| Electronic check customer churn rate | 45.29% |

### Business Interpretation

- **Contract type:** Month-to-month customers show a substantially higher observed churn rate than customers on longer-term contracts.
- **Internet service:** Customers with fiber optic service show a higher observed churn rate than the other service groups in this analysis.
- **Payment method:** Customers using electronic checks have a higher observed churn rate in the analyzed dataset.
- **Retention opportunities:** These segments may be useful starting points for further investigation and targeted retention experiments.

These findings describe patterns in the analyzed dataset. They do not establish causation or prove that a particular contract, service, or payment method causes customer churn.

## Dashboard

The interactive dashboard presents analytical results in a visual, accessible format.

**[🚀 Open the Live Streamlit Dashboard](https://telco-customer-churn-analysis-platform.streamlit.app/)**

The project is designed to support exploration of customer churn patterns, segment comparisons, customer risk indicators, and revenue-related metrics.

Dashboard functionality depends on the deployed version of the application.

## Project Workflow

The project follows a structured analytics workflow.

### 1. Data Understanding

- Inspect the dataset and its fields.
- Review customer characteristics and data types.
- Understand the target variable and relevant business dimensions.

### 2. Data Cleaning

- Prepare the data for analysis.
- Address data-quality issues.
- Ensure that analytical fields are suitable for downstream calculations.

### 3. Exploratory Data Analysis (EDA)

- Examine customer distributions and characteristics.
- Compare churn rates across relevant categories.
- Investigate patterns in tenure, monthly charges, contracts, and services.

### 4. Feature Engineering

- Create additional variables for customer analysis.
- Prepare derived features for segmentation and risk assessment.
- Generate processed datasets for subsequent analytical steps.

### 5. Customer Segmentation

- Compare customer groups.
- Evaluate observed churn differences across segments.
- Identify groups that merit additional investigation.

### 6. Churn Analysis

- Analyze churn by contract type.
- Compare churn across internet service categories.
- Investigate payment-method differences.
- Examine relationships between churn and customer characteristics.

### 7. Revenue Impact Analysis

- Examine monthly charges associated with customers who churned.
- Review historical charges for churned customers.
- Distinguish historical amounts from estimates of potential revenue exposure.

### 8. Final Insights

- Consolidate the main analytical findings.
- Develop business-oriented interpretations.
- Identify potential customer-retention initiatives for future testing.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data analysis and processing |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Plotly | Interactive charts |
| Jupyter Notebook | Exploratory analysis and documentation |
| Streamlit | Interactive web dashboard |
| SQL | Data querying and analytical workflows |
| Git | Version control |
| GitHub | Source-code hosting and portfolio publishing |

## Repository Structure

The repository is organized around the dashboard, data, analysis scripts, notebooks, SQL workflows, and supporting project documentation.

```text
Telco-Customer-Churn-Analytics-Platform/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
├── powerbi/
├── screenshots/
│
├── python/
│   ├── notebooks/
│   ├── outputs/
│   └── scripts/
│       ├── 01_eda.py
│       ├── 02_feature_engineering.py
│       ├── 03_churn_analysis.py
│       ├── 04_revenue_impact_analysis.py
│       ├── 05_final_insights.py
│       └── common.py
│
└── sql/
```

This is a representative structure. The files and folders available in the GitHub repository are the source of truth for the published project.

## Getting Started

### Prerequisites

Install the following before running the project locally:

- Python
- Git
- A code editor, such as Visual Studio Code
- A web browser for the Streamlit dashboard

### 1. Clone the Repository

```bash
git clone https://github.com/AramMehraban/Telco-Customer-Churn-Analytics-Platform.git
cd Telco-Customer-Churn-Analytics-Platform
```

### 2. Create a Virtual Environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, review your local execution-policy settings before proceeding.

### 3. Install Dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Run the Dashboard

From the repository root:

```powershell
python -m streamlit run app.py
```

Open the local address displayed in the terminal. Streamlit commonly uses:

```text
http://localhost:8501
```

### 5. Explore the Analysis Scripts

The `python/scripts/` directory contains the project's analysis workflow.

Before running a script, confirm that its required input files exist and that its paths are configured relative to the repository structure.

## Running the Analysis Scripts

Run the analysis scripts from the repository root, in the intended order:

```powershell
python .\python\scripts\01_eda.py
python .\python\scripts\02_feature_engineering.py
python .\python\scripts\03_churn_analysis.py
python .\python\scripts\04_revenue_impact_analysis.py
python .\python\scripts\05_final_insights.py
```

The scripts may create processed datasets, analytical outputs, or reports. Check each script's configuration and output messages to confirm the actual input and output paths.

## Deployment

The interactive dashboard is hosted through Streamlit Community Cloud.

- **Live application:** [Telco Customer Churn Analytics Dashboard](https://telco-customer-churn-analysis-platform.streamlit.app/)
- **Source code:** [GitHub Repository](https://github.com/AramMehraban/Telco-Customer-Churn-Analytics-Platform)

The application is configured to run from `app.py`, with Python dependencies specified in `requirements.txt`.

For future updates:

1. Make and test changes locally.
2. Commit the changes to Git.
3. Push the changes to the GitHub `main` branch.
4. Check the Streamlit deployment logs if the application fails to update.
5. Verify the deployed dashboard after each significant change.

## Business Value

The analysis provides a starting point for understanding customer churn and identifying groups that may benefit from additional retention investigation.

Potential business applications include:

- Monitoring churn rates across customer segments.
- Investigating retention opportunities among month-to-month customers.
- Evaluating service and payment-method differences.
- Developing and testing targeted retention offers.
- Tracking retention campaign outcomes against a baseline.
- Supporting communication between analytics teams and business stakeholders.

Any proposed retention intervention should be evaluated using measurable outcomes rather than assumptions based on segment-level correlations alone.

## Limitations

- **Descriptive analysis:** Observed differences do not establish causal relationships.
- **Risk assessment:** Heuristic risk scores are not calibrated probabilities of churn.
- **Historical charges:** Total charges accumulated before churn are not equivalent to future revenue or customer lifetime value.
- **Revenue exposure:** Monthly charges associated with churned customers represent an estimate of exposure at churn, not current recurring revenue.
- **Retention strategy:** Recommendations require validation with further analysis and, where possible, controlled experiments.
- **Generalizability:** Results reflect the analyzed dataset and may not represent every telecommunications business.

## Future Improvements

Potential extensions include:

- Developing and evaluating a predictive churn model.
- Comparing model performance with suitable classification metrics.
- Improving customer risk scoring through calibration and validation.
- Adding filters and additional drill-down capabilities to the dashboard.
- Automating data-quality checks.
- Expanding SQL-based analytical reporting.
- Tracking retention initiatives and their measurable business outcomes.
- Adding dashboard screenshots and further project documentation.

## Author

Created as a portfolio project demonstrating skills in:

- Data analytics
- Data cleaning and feature engineering
- Exploratory data analysis
- SQL and analytical workflows
- Customer churn investigation
- Data visualization
- Interactive dashboard development
- Business insight communication
- Git and GitHub

## Project Links

- **Live Dashboard:** https://telco-customer-churn-analysis-platform.streamlit.app/
- **GitHub Repository:** https://github.com/AramMehraban/Telco-Customer-Churn-Analytics-Platform

---

*This project is intended for portfolio and learning purposes. Findings and recommendations should be interpreted within the context of the analyzed dataset.*
