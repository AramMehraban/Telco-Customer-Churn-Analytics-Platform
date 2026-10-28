# Telco Customer Churn Analytics Platform

**End-to-End Customer Churn Analytics | Python · SQL · Data Visualization · Business Intelligence**

[🚀 Live Dashboard](https://telco-customer-churn-analysis-platform.streamlit.app/) · [📂 GitHub Repository](https://github.com/AramMehraban/Telco-Customer-Churn-Analytics-Platform)

An end-to-end data analytics portfolio project exploring customer churn, retention patterns, customer segments, and revenue exposure in a telecommunications dataset.

The project combines Python-based data analysis, Jupyter Notebooks, SQL data workflows, and an interactive Streamlit dashboard to turn customer data into actionable business insights.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Business Objectives](#business-objectives)
- [Business Questions](#business-questions)
- [Key Findings](#key-findings)
- [Dashboard](#dashboard)
- [Analytical Workflow](#analytical-workflow)
- [Technology Stack](#technology-stack)
- [Repository Structure](#repository-structure)
- [SQL Analytics](#sql-analytics)
- [Data and Methodology](#data-and-methodology)
- [Limitations](#limitations)
- [Future Improvements](#future-improvements)
- [Author](#author)
- [License](#license)

---

## Project Overview

Customer churn is an important business challenge for subscription-based companies. Understanding which customer segments have higher observed churn rates can help businesses prioritize retention analysis and develop better customer engagement strategies.

This project explores customer behavior and churn patterns through a structured analytical workflow, including:

- Data understanding and quality assessment
- Data cleaning and exploratory data analysis (EDA)
- Feature engineering and customer segmentation
- Churn analysis across customer and service categories
- Revenue impact analysis
- SQL-based analytical reporting
- Business insight communication and dashboard visualization

The objective is to demonstrate how data analysis can support business decisions, from preparing raw data to communicating findings in a clear and structured format.

## Business Objectives

- Measure the overall customer churn rate.
- Compare churn across contract types, internet services, and payment methods.
- Investigate the relationship between churn, customer tenure, and monthly charges.
- Develop analytical features for customer segmentation.
- Examine historical charges associated with churned customers.
- Identify customer segments that may warrant further retention investigation.
- Communicate findings through visualizations, SQL outputs, and an interactive dashboard.

## Business Questions

1. What proportion of customers have churned?
2. How does churn differ between month-to-month, one-year, and two-year contracts?
3. Which internet service categories have higher observed churn rates?
4. How does churn vary by payment method?
5. How are customer tenure and monthly charges associated with churn?
6. Which customer segments merit further investigation?
7. What historical charges are associated with customers who churned?
8. How can these findings inform measurable customer-retention initiatives?

## Key Findings

The current project analysis reports **7,043 customers**, including **1,869 customers who churned**.

| Metric                               | Reported result |
| ------------------------------------ | --------------: |
| Total customers analyzed             |           7,043 |
| Churned customers                    |           1,869 |
| Overall churn rate                   |          26.54% |
| Month-to-month contract churn rate   |          42.71% |
| One-year contract churn rate         |          11.27% |
| Two-year contract churn rate         |           2.83% |
| Fiber optic customer churn rate      |          41.89% |
| Electronic check customer churn rate |          45.29% |

*These figures are reported from the current project analysis and should be interpreted in the context of the analyzed dataset.*

### Business Interpretation

**Contract type:** Month-to-month customers show a substantially higher observed churn rate than customers with longer-term contracts. This segment may be worth prioritizing for further retention analysis.

**Internet service:** The fiber optic segment has a higher observed churn rate in this dataset. Further investigation could examine customer satisfaction, service experience, pricing, and other relevant factors.

**Payment method:** Customers paying by electronic check show a higher observed churn rate. This association may help guide additional investigation into payment experience and customer behavior.

**Retention opportunities:** These patterns can help identify segments for further analysis and carefully measured retention experiments.

These are descriptive findings. They do not establish that contract type, internet service, or payment method causes churn.

## Dashboard

Explore the interactive dashboard:

**[🚀 Open the Live Streamlit Dashboard](https://telco-customer-churn-analysis-platform.streamlit.app/)**

The project includes a dashboard component intended to communicate customer churn patterns and business metrics in an accessible visual format.

The availability and functionality of individual dashboard features depend on the currently deployed application version.

## Analytical Workflow

The project is organized into eight planned analytical stages.

### 1. Data Understanding

- Inspect the source dataset and its structure.
- Review customer characteristics and data types.
- Identify the churn target and relevant business dimensions.

### 2. Data Cleaning

- Prepare the data for analysis.
- Investigate data-quality issues.
- Produce cleaned datasets for downstream analysis.

### 3. Exploratory Data Analysis

- Explore customer distributions and characteristics.
- Compare churn rates across categories.
- Investigate patterns involving tenure, monthly charges, contracts, and services.

### 4. Feature Engineering

- Create additional analytical variables.
- Prepare derived features for segmentation and risk assessment.
- Save processed datasets for subsequent analysis.

### 5. Customer Segmentation

- Compare customer groups.
- Examine differences in observed churn rates.
- Identify segments for further investigation.

### 6. Churn Analysis

- Analyze churn by contract type.
- Compare internet service categories.
- Investigate payment-method differences.
- Explore relationships between churn and customer characteristics.

### 7. Revenue Impact Analysis

- Examine monthly charges associated with churned customers.
- Review historical charges.
- Distinguish observed financial amounts from estimates of potential revenue exposure.

### 8. Final Insights and Recommendations

- Consolidate the main analytical findings.
- Translate results into business-oriented interpretations.
- Identify retention initiatives that could be tested and measured.

## Technology Stack

| Technology             | Purpose                                              |
| ---------------------- | ---------------------------------------------------- |
| Python                 | Data analysis and processing                         |
| Pandas                 | Data manipulation and analysis                       |
| NumPy                  | Numerical operations                                 |
| Matplotlib and Seaborn | Data visualization and exploratory analysis          |
| Plotly                 | Interactive visualizations                           |
| Jupyter Notebook       | Analysis workflow and documentation                  |
| SQL                    | Data preparation, querying, and analytical reporting |
| Streamlit              | Interactive dashboard                                |
| Git and GitHub         | Version control and portfolio publishing             |

## Repository Structure

The project repository contains the following main areas:

```text
Telco-Customer-Churn-Analytics-Platform/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
├── docs/
├── powerbi/
├── screenshots/
│
├── python/
│   ├── data/
│   │   ├── raw/
│   │   │   └── Telco-Customer-Churn.csv
│   │   └── processed/
│   │       ├── churn_analysis_summary.csv
│   │       ├── customer_churn_clean.csv
│   │       ├── customer_churn_features.csv
│   │       └── telco_churn_clean.csv
│   │
│   ├── notebooks/
│   │   ├── 01_Data_Understanding.ipynb
│   │   ├── 02_Data_Cleaning.ipynb
│   │   ├── 03_EDA.ipynb
│   │   ├── 04_Feature_Engineering.ipynb
│   │   ├── 05_Customer_Segmentation.ipynb
│   │   ├── 06_Churn_Analysis.ipynb
│   │   └── 07_Revenue_Impact_Analysis.ipynb
│   │
│   └── outputs/
│       └── tables/
│
└── sql/
    ├── Database and schema creation
    ├── Raw data loading
    ├── ETL and data-quality checks
    ├── Dimension and fact table loading
    └── Analytical views and reporting queries
```

This is a simplified overview of the project structure. Refer to the repository for the actual files and their current implementation status.

## SQL Analytics

The SQL component contains scripts covering database preparation, data loading, cleaning, dimensional modeling, and analytical views.

The workflow includes:

- Database and schema creation
- Raw table creation and data loading
- ETL cleaning and data-quality reporting
- Dimension and fact table creation
- Foreign-key relationships
- Analytical views for churn, contracts, payments, internet services, revenue, customer risk, and executive summaries
- Queries for testing analytical views

The SQL work complements the Python analysis by organizing data preparation and business reporting into reusable database operations.

## Data and Methodology

The analysis uses the Telco Customer Churn dataset stored in the project's raw-data directory. Processed datasets and analytical outputs are maintained separately from the raw input.

The analytical approach emphasizes descriptive statistics, segment comparisons, and business interpretation.

The reported churn rate is calculated as:

[
\text{Churn Rate} =
\frac{\text{Churned Customers}}{\text{Total Customers}}
\times 100
]

Segment-level churn rates should be calculated using the number of churned customers divided by the total customers in the respective segment.

Historical customer charges, monthly charges, and potential future revenue exposure represent different concepts and should not be treated as interchangeable.

## Limitations

- **Descriptive analysis:** Observed relationships do not establish causation.
- **Risk assessment:** A heuristic risk score is not a calibrated probability of churn.
- **Historical charges:** Total charges accumulated before churn do not represent future revenue or customer lifetime value.
- **Revenue exposure:** Monthly charges associated with churned customers are not equivalent to current recurring revenue.
- **Retention recommendations:** Proposed actions require further validation and, where possible, controlled experiments.
- **Generalizability:** Results reflect the analyzed dataset and may not represent every telecommunications business.
- **Reproducibility:** Local execution depends on the availability of the relevant project files, dependencies, and configuration.

## Future Improvements

- Develop and validate a predictive churn classification model.
- Evaluate model performance using appropriate classification metrics.
- Improve risk scoring through validation and probability calibration.
- Expand interactive dashboard filters and drill-down analysis.
- Automate data-quality checks and analytical reporting.
- Strengthen the reproducibility of the Python and SQL workflows.
- Add dashboard screenshots and implementation documentation.
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
- [Kaggle](https://kaggle.com/aramehr)

## License

**Copyright © 2026 Aram Mehraban. All rights reserved.**

Unless otherwise stated, the original source code, documentation, project structure, and original visualizations are provided for portfolio review and personal learning. Reproduction, modification, redistribution, republication, or commercial use of original materials requires prior written permission, except where permitted by applicable law.

Third-party datasets, libraries, and other materials remain subject to their respective licenses and terms of use. Making this repository publicly available does not grant a general license to reuse its original materials.
