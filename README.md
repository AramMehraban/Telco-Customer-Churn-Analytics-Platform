# Telco Customer Churn Analytics Platform

An end-to-end customer churn analytics portfolio project using Python, SQL, Jupyter Notebook, and Streamlit. The project explores customer retention, contract types, service usage, customer risk, and revenue exposure to support data-driven business decisions.

## Overview

Customer churn is a key challenge for subscription-based businesses. This project examines customer characteristics and churn patterns to identify segments that may benefit from further retention analysis.

The workflow covers data understanding, cleaning, exploratory data analysis, feature engineering, customer segmentation, churn analysis, and revenue impact assessment. An interactive Streamlit dashboard is used to present analytical results.

## Business Questions

- What percentage of customers have churned?
- How does churn differ across contract types?
- Which internet service and payment-method segments have higher churn rates?
- How are tenure and monthly charges associated with churn?
- Which customer segments could be prioritized for retention analysis?
- What historical charges are associated with customers who churned?

## Key Findings

The current analysis contains 7,043 customers, including 1,869 customers who churned.

| Metric | Result |
|---|---:|
| Total customers | 7,043 |
| Churned customers | 1,869 |
| Overall churn rate | 26.54% |
| Month-to-month contract churn rate | 42.71% |
| One-year contract churn rate | 11.27% |
| Two-year contract churn rate | 2.83% |
| Fiber optic customer churn rate | 41.89% |
| Electronic check customer churn rate | 45.29% |

These are descriptive results for the analyzed dataset. They indicate associations, not causation, and should not be interpreted as proof that any specific service, contract, or payment method causes churn.

## Project Workflow

1. **Data Understanding** — inspect the dataset, fields, and customer characteristics.
2. **Data Cleaning** — handle data-quality issues and prepare analytical data.
3. **Exploratory Data Analysis** — examine distributions, customer profiles, and churn patterns.
4. **Feature Engineering** — create derived variables for segmentation and risk analysis.
5. **Customer Segmentation** — compare customer groups and their churn rates.
6. **Churn Analysis** — investigate churn across contracts, services, tenure, and payment methods.
7. **Revenue Impact Analysis** — examine historical charges and potential revenue exposure.
8. **Final Insights** — consolidate findings and develop measurable business recommendations.

## Technology Stack

- **Python** — analysis and data preparation
- **Pandas and NumPy** — data manipulation and numerical calculations
- **Matplotlib and Seaborn** — data visualization
- **Plotly** — interactive visualizations
- **Jupyter Notebook** — exploratory analysis and documentation
- **Streamlit** — interactive dashboard
- **SQL** — querying and analytical workflows
- **Git and GitHub** — version control and portfolio publishing

## Repository Structure

```text
Telco-Customer-Churn-Analytics-Platform/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   └── processed/
├── docs/
├── powerbi/
├── python/
│   ├── notebooks/
│   ├── outputs/
│   └── scripts/
├── screenshots/
└── sql/
```

The structure represents the intended organization of the project. Only files actually present in the repository should be considered part of the final published version.

## Getting Started

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Telco-Customer-Churn-Analytics-Platform
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with the actual GitHub repository URL.

### 2. Create a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Run the Streamlit dashboard

```powershell
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, usually `http://localhost:8501`.

### 5. Run the Python analysis scripts

After the scripts have been added and the input data paths verified, run them from the repository root in the documented order. See the `python/scripts/` directory.

## Deployment

The dashboard can be deployed through [Streamlit Community Cloud](https://share.streamlit.io/) after the project has been pushed to GitHub.

1. Verify that `app.py` runs locally.
2. Confirm that all required data files are included and accessible.
3. Check that the dependencies are listed in `requirements.txt`.
4. Push the verified project files to GitHub.
5. Connect the repository to Streamlit Community Cloud.
6. Select the correct branch and `app.py` as the main file.
7. Test the deployed application and its visualizations.

## Business Value

The analysis can help stakeholders identify customer segments that merit further investigation, compare churn patterns, and develop measurable retention initiatives.

Potential next steps include evaluating targeted retention offers, monitoring churn by customer segment, and measuring campaign performance against a baseline.

## Limitations

- Segment differences are descriptive associations and do not establish causation.
- Heuristic risk scores are not calibrated churn probabilities.
- Historical total charges are not equivalent to future revenue or customer lifetime value.
- Monthly charges associated with churned customers represent an estimate of exposure at churn, not current recurring revenue.
- Retention recommendations should be validated using additional analysis and, where possible, controlled experiments.

## Project Status

Portfolio project under development. Dashboard functionality, data dependencies, analysis scripts, and deployment should be tested before the project is described as production-ready.

## Author

Created as a portfolio project demonstrating data analytics, feature engineering, SQL, business intelligence, and interactive dashboard development.