USE CustomerChurnDW;
GO


CREATE OR ALTER VIEW analytics.vw_Revenue_Analysis
AS


SELECT


CASE

WHEN ChurnFlag=1

THEN 'Churn Customer'

ELSE 'Active Customer'

END AS CustomerStatus,


COUNT(*) Customers,


SUM(MonthlyCharges) TotalMonthlyRevenue,


AVG(MonthlyCharges) AverageMonthlyCharges


FROM fact.FactCustomerChurn


GROUP BY

CASE

WHEN ChurnFlag=1

THEN 'Churn Customer'

ELSE 'Active Customer'

END;


GO