-- 11 LOAD FACT TABLE

USE CustomerChurnDW;
GO

TRUNCATE TABLE fact.FactCustomerChurn;
GO

INSERT INTO fact.FactCustomerChurn
(
	CustomerKey,
	ServiceKey,
	ContractKey,
	PaymentKey,
	ChurnFlag,
	MonthlyCharges,
	TotalCharges
)


SELECT
	c.CustomerKey,
	s.ServiceKey,
	ct.ContractKey,
	p.PaymentKey,

CASE
	WHEN cl.Churn='Yes'
	THEN 1
	ELSE 0
END,

	cl.MonthlyCharges,
	cl.TotalCharges

FROM staging.Customer_Churn_Clean cl

INNER JOIN dim.DimCustomer c
ON cl.CustomerID = c.CustomerID

INNER JOIN dim.DimService s
ON cl.PhoneService = s.PhoneService
AND cl.MultipleLines = s.MultipleLines
AND cl.InternetService = s.InternetService
AND cl.OnlineSecurity = s.OnlineSecurity
AND cl.OnlineBackup = s.OnlineBackup
AND cl.DeviceProtection = s.DeviceProtection
AND cl.TechSupport = s.TechSupport
AND cl.StreamingTV = s.StreamingTV
AND cl.StreamingMovies = s.StreamingMovies

INNER JOIN dim.DimContract ct
ON cl.Contract = ct.Contract
AND cl.PaperlessBilling = ct.PaperlessBilling

INNER JOIN dim.DimPayment p
ON cl.PaymentMethod = p.PaymentMethod;

GO


-- Fact VALIDATION

SELECT
	COUNT(*) AS FactRows
FROM fact.FactCustomerChurn;
	SELECT
		ChurnFlag,
		COUNT(*) Customers
	FROM fact.FactCustomerChurn
GROUP BY ChurnFlag;
GO



-- Final Validation
-- 1. Unique Customers

SELECT 
	COUNT(DISTINCT CustomerKey) AS UniqueCustomers
FROM fact.FactCustomerChurn;



-- 2. Missing Keys

SELECT *
FROM fact.FactCustomerChurn
WHERE
	CustomerKey IS NULL
	OR ServiceKey IS NULL
	OR ContractKey IS NULL
	OR PaymentKey IS NULL;



-- 3. Churn Distribution

SELECT
	ChurnFlag,
	COUNT(*) AS Customers

FROM fact.FactCustomerChurn
GROUP BY ChurnFlag;
GO