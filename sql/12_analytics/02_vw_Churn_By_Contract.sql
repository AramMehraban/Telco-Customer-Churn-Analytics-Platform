USE CustomerChurnDW;
GO


CREATE OR ALTER VIEW analytics.vw_Churn_By_Contract
AS

SELECT

ct.Contract,

COUNT(*) AS Customers,


SUM(CAST(f.ChurnFlag AS INT)) AS ChurnCustomers,


CAST(

SUM(CAST(f.ChurnFlag AS FLOAT))
/
COUNT(*)

AS DECIMAL(5,4)

) AS ChurnRate


FROM fact.FactCustomerChurn f


INNER JOIN dim.DimContract ct

ON f.ContractKey = ct.ContractKey


GROUP BY

ct.Contract;

GO