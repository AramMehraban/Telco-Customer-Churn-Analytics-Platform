USE CustomerChurnDW;
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
	WHEN LTRIM(RTRIM(cl.Churn)) = 'Yes'
		THEN 1
		ELSE 0
END,


cl.MonthlyCharges,
cl.TotalCharges


FROM staging.Customer_Churn_Clean cl


JOIN dim.DimCustomer c
ON cl.CustomerID = c.CustomerID


JOIN dim.DimService s
ON cl.PhoneService = s.PhoneService
AND cl.MultipleLines = s.MultipleLines
AND cl.InternetService = s.InternetService
AND cl.OnlineSecurity = s.OnlineSecurity
AND cl.TechSupport = s.TechSupport



JOIN dim.DimContract ct
ON cl.Contract = ct.Contract
AND cl.PaperlessBilling = ct.PaperlessBilling



JOIN dim.DimPayment p
ON cl.PaymentMethod = p.PaymentMethod;

GO


-- Test query
SELECT 
CustomerID,
COUNT(*) AS DuplicateCount

FROM staging.Customer_Churn_Clean

GROUP BY CustomerID

HAVING COUNT(*) > 1;
-- Ergebniss: 0


SELECT 
COUNT(*) AS ServiceRows
FROM dim.DimService;
-- Ergebniss: 322

SELECT 
PhoneService,
MultipleLines,
InternetService,
OnlineSecurity,
TechSupport,
COUNT(*) AS cnt

FROM dim.DimService

GROUP BY
PhoneService,
MultipleLines,
InternetService,
OnlineSecurity,
TechSupport

HAVING COUNT(*) > 1;
-- Ergebniss: 
/*
PhoneService	MultipleLines	InternetService	OnlineSecurity	TechSupport	cnt
No	No phone service	DSL	No	No	16
No	No phone service	DSL	No	Yes	16
No	No phone service	DSL	Yes	No	16
No	No phone service	DSL	Yes	Yes	16
Yes	No	DSL	No	No	16
Yes	No	DSL	No	Yes	16
Yes	No	DSL	Yes	No	16
Yes	No	DSL	Yes	Yes	16
Yes	No	Fiber optic	No	No	16
Yes	No	Fiber optic	No	Yes	16
Yes	No	Fiber optic	Yes	No	16
Yes	No	Fiber optic	Yes	Yes	16
Yes	Yes	DSL	No	No	16
Yes	Yes	DSL	No	Yes	16
Yes	Yes	DSL	Yes	No	16
Yes	Yes	DSL	Yes	Yes	16
Yes	Yes	Fiber optic	No	No	16
Yes	Yes	Fiber optic	No	Yes	16
Yes	Yes	Fiber optic	Yes	No	16
Yes	Yes	Fiber optic	Yes	Yes	16  */
