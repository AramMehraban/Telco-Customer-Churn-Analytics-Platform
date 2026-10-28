# Telco Customer Churn Analytics Platform

**End-to-End Customer Churn Analytics | Python · SQL · Streamlit · Power BI**

[🚀 Open Live Dashboard](https://telco-customer-churn-analysis-platform.streamlit.app/) · [📂 GitHub Repository](https://github.com/AramMehraban/Telco-Customer-Churn-Analytics-Platform)

An end-to-end data analytics portfolio project exploring customer churn, customer segments, contract behavior, and revenue exposure in a telecommunications dataset.

The project combines Python, Jupyter Notebooks, SQL workflows, Power BI, and an interactive Streamlit dashboard to transform customer data into structured analysis and business-oriented insights.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Business Objectives](#business-objectives)
- [Business Questions](#business-questions)
- [Key Findings](#key-findings)
- [Dashboard](#dashboard)
- [Dashboard Screenshots](#dashboard-screenshots)
- [Analytical Workflow](#analytical-workflow)
- [Technology Stack](#technology-stack)
- [Repository Structure](#repository-structure)
- [SQL Analytics](#sql-analytics)
- [Data and Methodology](#data-and-methodology)
- [How to Run Locally](#how-to-run-locally)
- [Limitations](#limitations)
- [Future Improvements](#future-improvements)
- [Author](#author)
- [License](#license)

---

## Project Overview

Customer churn is an important business challenge for subscription-based companies. Understanding which customer groups have higher observed churn rates can help organizations identify areas for further investigation and evaluate potential customer-retention strategies.

This project explores customer behavior and churn patterns through a structured analytical workflow covering:

- Data understanding and quality assessment
- Data cleaning and exploratory data analysis (EDA)
- Feature engineering and customer segmentation
- Churn analysis across customer and service categories
- Revenue impact analysis
- SQL-based data preparation and analytical reporting
- Business insight communication
- Interactive dashboard development

The objective is to demonstrate practical skills in data processing, analytical SQL, Python scripting, data visualization, and communicating findings in a business-oriented format.

## Business Objectives

- Measure the overall customer churn rate.
- Compare churn rates across contract types, internet services, and payment methods.
- Investigate the relationship between churn, customer tenure, and monthly charges.
- Prepare analytical features for customer segmentation.
- Examine historical charges associated with churned customers.
- Identify customer segments that may warrant further retention analysis.
- Present analytical results through SQL outputs, visualizations, and interactive dashboards.

## Business Questions

1. What proportion of customers have churned?
2. How does churn differ between month-to-month, one-year, and two-year contracts?
3. Which internet service categories have higher observed churn rates?
4. How does churn vary by payment method?
5. How are customer tenure and monthly charges associated with churn?
6. Which customer segments merit further investigation?
7. What historical charges are associated with customers who churned?
8. How can the findings inform measurable customer-retention initiatives?

## Key Findings

The current project analysis reports **7,043 customers**, including **1,869 customers who churned**.

| Metric | Reported result |
|---|---:|
| Total customers analyzed | 7,043 |
| Churned customers | 1,869 |
| Overall churn rate | 26.54% |
| Month-to-month contract churn rate | 42.71% |
| One-year contract churn rate | 11.27% |
| Two-year contract churn rate | 2.83% |
| Fiber optic customer churn rate | 41.89% |
| Electronic check customer churn rate | 45.29% |

*These figures are reported from the existing project analysis. They should be interpreted in the context of the analyzed dataset and revalidated against the final analytical outputs before being used for business decisions.*

### Business Interpretation

**Contract type**

The reported churn rate is higher among customers with month-to-month contracts than among customers with longer-term contracts. This group may be a useful starting point for further retention analysis.

**Internet service**

The reported churn rate is higher in the fiber optic segment. Additional analysis could investigate possible relationships with pricing, service experience, customer satisfaction, and other customer characteristics.

**Payment method**

Customers using electronic checks show a higher reported churn rate in this dataset. This pattern may warrant further investigation into payment preferences and the overall customer experience.

**Retention opportunities**

The findings can help prioritize customer segments for further investigation and support the design of measurable retention experiments.

These observations are descriptive. They do not establish that contract type, internet service, or payment method causes customer churn.

## Dashboard

Explore the interactive dashboard:

**[🚀 Launch the Live Streamlit Dashboard](https://telco-customer-churn-analysis-platform.streamlit.app/)**

The project includes a Streamlit application intended to communicate customer churn patterns and analytical results through interactive visualizations.

The repository also contains a Power BI report:

`powerbi/Customer_Churn_Analystics_Platform_Final.pbix`

The availability of individual features and the consistency of displayed metrics depend on the currently deployed application and report versions.

## Dashboard Screenshots

The repository includes screenshots illustrating the dashboard's main analytical areas.

| Screenshot | Analytical area |
|---|---|
| `01_Executive_Overview.png` | Executive overview |
| `02_Customer_Segmentation.png` | Customer segmentation |
| `03_Churn_Analysis.png` | Churn analysis |
| `04_Revenue_Impact.png` | Revenue impact analysis |
| `05_Customer_Details.png` | Customer details |
| `06_Customer_Risk_Rentation.png` | Customer risk analysis |
| `07_Recommendations.png` | Recommendations |

Screenshots are stored in the `screenshots/` directory.

## Analytical Workflow

The analytical work is organized into seven available Jupyter Notebooks and a set of reusable Python scripts. Final insights are consolidated through the Python outputs.

### 1. Data Understanding

Notebook: `01_Data_Understanding.ipynb`

- Inspect the source dataset and its structure.
- Review customer characteristics and data types.
- Identify the churn target and relevant business dimensions.

### 2. Data Cleaning

Notebook: `02_Data_Cleaning.ipynb`

- Prepare the dataset for analysis.
- Investigate data-quality issues.
- Produce cleaned data for downstream analysis.

### 3. Exploratory Data Analysis

Notebook: `03_EDA.ipynb`

- Explore customer distributions and characteristics.
- Compare churn rates across categories.
- Investigate patterns involving tenure, monthly charges, contracts, and services.

### 4. Feature Engineering

Notebook: `04_Feature_Engineering.ipynb`

- Create additional analytical variables.
- Prepare derived features for segmentation and further analysis.
- Save processed datasets for subsequent workflows.

### 5. Customer Segmentation

Notebook: `05_Customer_Segmentation.ipynb`

- Compare customer groups.
- Examine differences in observed churn rates.
- Identify segments for further investigation.

### 6. Churn Analysis

Notebook: `06_Churn_Analysis.ipynb`

- Analyze churn by contract type.
- Compare internet service categories.
- Investigate payment-method differences.
- Explore relationships between churn and customer characteristics.

### 7. Revenue Impact Analysis

Notebook: `07_Revenue_Impact_Analysis.ipynb`

- Examine monthly charges associated with churned customers.
- Review historical customer charges.
- Distinguish observed financial amounts from estimates of potential revenue exposure.

### Final Insights and Recommendations

Python script: `python/scripts/05_final_insights.py`

Output: `python/outputs/final_insights.md`

The final insights are consolidated into a Markdown report supported by analytical outputs. The previously empty eighth Notebook is not included in the current repository workflow.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data analysis and processing |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations |
| Matplotlib and Seaborn | Data visualization and exploratory analysis |
| Plotly | Interactive visualizations |
| Jupyter Notebook | Analysis workflow and documentation |
| SQL | Data preparation, querying, and analytical reporting |
| Streamlit | Interactive dashboard application |
| Power BI | Business intelligence reporting |
| Git and GitHub | Version control and portfolio publishing |

## Repository Structure

The following tree summarizes the main project files and directories.

```text
Telco-Customer-Churn-Analytics-Platform/
├── README.md
├── app.py
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── raw/
│   │   └── Telco-Customer-Churn.csv
│   └── processed/
│       ├── churn_analysis_summary.csv
│       ├── customer_churn_clean.csv
│       ├── customer_churn_features.csv
│       └── telco_churn_clean.csv
│
├── docs/
│   ├── Customer_Churn_Projekt_SQL_Queries.pdf
│   └── SQL_Code_PDF/
│       ├── SQL script documentation (PDF)
│       └── Analytics_Views/
│           └── Analytics view documentation (PDF)
│
├── powerbi/
│   └── Customer_Churn_Analystics_Platform_Final.pbix
│
├── python/
│   ├── notebooks/
│   │   ├── 01_Data_Understanding.ipynb
│   │   ├── 02_Data_Cleaning.ipynb
│   │   ├── 03_EDA.ipynb
│   │   ├── 04_Feature_Engineering.ipynb
│   │   ├── 05_Customer_Segmentation.ipynb
│   │   ├── 06_Churn_Analysis.ipynb
│   │   └── 07_Revenue_Impact_Analysis.ipynb
│   │
│   ├── scripts/
│   │   ├── common.py
│   │   ├── 01_eda.py
│   │   ├── 02_feature_engineering.py
│   │   ├── 03_churn_analysis.py
│   │   ├── 04_revenue_impact_analysis.py
│   │   └── 05_final_insights.py
│   │
│   └── outputs/
│       ├── final_insights.md
│       └── Analytical result tables (CSV)
│
├── screenshots/
│   ├── 01_Executive_Overview.png
│   ├── 02_Customer_Segmentation.png
│   ├── 03_Churn_Analysis.png
│   ├── 04_Revenue_Impact.png
│   ├── 05_Customer_Details.png
│   ├── 06_Customer_Risk_Rentation.png
│   └── 07_Recommendations.png
│
└── sql/
    ├── 01_Create_Database.sql
    ├── 02_Create_Schema.sql
    ├── 03_Create_ Raw_Table.sql
    ├── 04_Load_Raw_Data.sql
    ├── 05_ETL_Cleaning.sql
    ├── 06_DataQuality_Report.sql
    ├── 07_Create_Dimensions.sql
    ├── 08_Load_Dimensions.sql
    ├── 09_Create_Fact.sql
    ├── 10_Add_ForeignKeys.sql
    ├── 11_Load_Fact.sql
    └── 12_analytics/
        ├── 00_Analytics_Views_Documents.sql
        ├── 01_vw_Churn_KPT_View.sql
        ├── 02_vw_Churn_By_Contract.sql
        ├── 03_vw_Churn_By_Payment.sql
        ├── 04_vw_Churn_By_Internet_Service.sql
        ├── 05_vw_Revenue_Analysis.sql
        ├── 06_vw_Customer_Risk_Analysis.sql
        ├── 07_vw_Executive_Summary.sql
        └── 08_Test_All_Views.sql
```

The structure above highlights the principal project components. Some nested documentation and output files are grouped to keep the overview readable; the repository itself is the source of truth for the complete file list.

## SQL Analytics

The SQL component contains scripts covering database preparation, data loading, cleaning, dimensional modeling, and analytical reporting.

The workflow includes:

- Database and schema creation
- Raw table creation and data loading
- ETL cleaning and data-quality reporting
- Dimension and fact table creation
- Foreign-key relationships
- Analytical views for churn, contracts, payments, internet services, revenue, customer risk, and executive summaries
- Queries for testing analytical views

The SQL scripts are organized in the `sql/` directory. Supporting PDF documentation is available in `docs/SQL_Code_PDF/`.

The SQL work complements the Python analysis by organizing data preparation and business reporting into reusable database operations.

## Data and Methodology

The project uses the Telco Customer Churn dataset stored in `data/raw/`. Cleaned datasets, engineered features, and analytical outputs are maintained separately in `data/processed/` and `python/outputs/`.

The analysis emphasizes descriptive statistics, segment comparisons, and business interpretation.

The overall churn rate is calculated as:

\[
\text{Churn Rate} =
\frac{\text{Churned Customers}}{\text{Total Customers}}
\times 100
\]

For a customer segment, the churn rate is calculated by dividing the number of churned customers in that segment by the total number of customers in the same segment.

Historical customer charges, monthly charges, and potential future revenue exposure represent different concepts and should not be treated as interchangeable.

## How to Run Locally

### Prerequisites

- Python installed on your computer
- Git, if you want to clone the repository
- The project data files required by the dashboard
- A compatible environment for the optional Power BI report

### 1. Clone the repository

```bash
git clone https://github.com/AramMehraban/Telco-Customer-Churn-Analytics-Platform.git
cd Telco-Customer-Churn-Analytics-Platform
```

### 2. Create a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell prevents environment activation, use the appropriate execution policy permitted on your computer or activate the environment through your preferred Python development tool.

### 3. Install dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Start the Streamlit application

From the project root directory:

```powershell
streamlit run app.py
```

Streamlit should open the dashboard in your browser. If it does not, follow the local URL printed in the terminal.

**Note:** Local execution depends on the dependencies listed in `requirements.txt`, the availability of the required data files, and the current implementation of `app.py`. This README does not guarantee that every feature has been independently tested in a fresh environment.

## Limitations

- **Descriptive analysis:** Observed relationships do not establish causation.
- **Risk assessment:** A heuristic risk score should not be interpreted as a calibrated probability of churn unless validated accordingly.
- **Historical charges:** Total charges accumulated before churn do not represent future revenue or customer lifetime value.
- **Revenue exposure:** Monthly charges associated with churned customers are not necessarily equivalent to current recurring revenue.
- **Retention recommendations:** Proposed actions require further validation and, where possible, controlled experiments.
- **Generalizability:** Results reflect the analyzed dataset and may not represent every telecommunications business.
- **Reproducibility:** Local execution depends on the availability of project files, dependencies, and compatible configuration.
- **Metric validation:** Reported metrics should be reconciled with the final analytical outputs before being used for operational decisions.

## Future Improvements

- Develop and validate a predictive churn classification model.
- Evaluate model performance using appropriate classification metrics.
- Improve risk scoring through validation and probability calibration.
- Expand interactive dashboard filters and drill-down analysis.
- Automate data-quality checks and analytical reporting.
- Strengthen the reproducibility of the Python and SQL workflows.
- Improve documentation and add automated tests.
- Evaluate retention strategies against measurable business outcomes.

## Author

**Aram Mehraban**

Data analytics portfolio project focused on:

- Data cleaning and exploratory data analysis
- Feature engineering and customer segmentation
- SQL and analytical reporting
- Customer churn and revenue analysis
- Data visualization and dashboard development
- Translating analytical results into business insights

**Portfolio links**

- [GitHub](https://github.com/AramMehraban)
- [LinkedIn](https://linkedin.com/in/AramMehraban)


## License

**Copyright © 2026 Aram Mehraban. All rights reserved.**

Unless otherwise stated, the original source code, documentation, project structure, and original visualizations are provided for portfolio review and personal learning. No general permission is granted to reproduce, modify, redistribute, republish, or commercially use these original materials, except where permitted by applicable law or separately authorized in writing.

Third-party datasets, libraries, and other materials remain subject to their respective licenses and terms of use. Making this repository publicly available does not grant a general license to reuse its original materials.
