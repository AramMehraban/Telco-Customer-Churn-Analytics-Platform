USE CustomerChurnDW;
GO

CREATE OR ALTER VIEW analytics.vw_Customer_Risk_Analysis
AS


SELECT


c.CustomerID,


c.Gender,


c.Tenure,


ct.Contract,


f.MonthlyCharges,


f.TotalCharges,


f.ChurnFlag,


CASE


WHEN f.ChurnFlag=1

THEN 'High Risk'


WHEN c.Tenure < 12
AND ct.Contract='Month-to-month'

THEN 'Medium Risk'


ELSE 'Low Risk'


END AS RiskCategory



FROM fact.FactCustomerChurn f


INNER JOIN dim.DimCustomer c

ON f.CustomerKey=c.CustomerKey


INNER JOIN dim.DimContract ct

ON f.ContractKey=ct.ContractKey;


GO