USE CustomerChurnDW;
GO


CREATE OR ALTER VIEW analytics.vw_Churn_By_Internet_Service
AS


SELECT


s.InternetService,


COUNT(*) Customers,


SUM(CAST(f.ChurnFlag AS INT)) ChurnCustomers,


CAST(

SUM(CAST(f.ChurnFlag AS FLOAT))
/
COUNT(*)

AS DECIMAL(5,4)

) ChurnRate


FROM fact.FactCustomerChurn f


INNER JOIN dim.DimService s

ON f.ServiceKey=s.ServiceKey


GROUP BY

s.InternetService;


GO