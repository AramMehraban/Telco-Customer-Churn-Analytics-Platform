USE CustomerChurnDW;
GO

-- Show Views 

SELECT *
FROM analytics.vw_Churn_KPI_View;



SELECT *
FROM analytics.vw_Churn_By_Contract;



SELECT *
FROM analytics.vw_Churn_By_Payment;



SELECT *
FROM analytics.vw_Churn_By_Internet_Service;



SELECT *
FROM analytics.vw_Revenue_Analysis;



SELECT TOP 20 *
FROM analytics.vw_Customer_Risk_Analysis;



SELECT *
FROM analytics.vw_Executive_Summary;


GO

SELECT name
FROM sys.views
WHERE schema_id = SCHEMA_ID('analytics');