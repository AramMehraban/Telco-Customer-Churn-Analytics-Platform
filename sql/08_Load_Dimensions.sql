USE CustomerChurnDW;
GO


-- LOAD DIM CUSTOMER


INSERT INTO dim.DimCustomer
(
	CustomerID,
	Gender,
	SeniorCitizen,
	Partner,
	Dependents,
	Tenure
)

SELECT DISTINCT

	CustomerID,
	Gender,
	SeniorCitizen,
	Partner,
	Dependents,
	Tenure

FROM staging.Customer_Churn_Clean;

GO


-- LOAD DIM SERVICE

INSERT INTO dim.DimService
(  
	PhoneService,
	MultipleLines,
	InternetService,

	OnlineSecurity,
	OnlineBackup,
	DeviceProtection,
	TechSupport,

	StreamingTV,
	StreamingMovies
)

SELECT DISTINCT

	PhoneService,
	MultipleLines,
	InternetService,

	OnlineSecurity,
	OnlineBackup,
	DeviceProtection,
	TechSupport,

	StreamingTV,
	StreamingMovies

FROM staging.Customer_Churn_Clean;

GO



-- LOAD DIM CONTRACT

INSERT INTO dim.DimContract
	(
	Contract,
	PaperlessBilling
)

SELECT DISTINCT

	Contract,
	PaperlessBilling

FROM staging.Customer_Churn_Clean;

GO


-- LOAD DIM PAYMENT

INSERT INTO dim.DimPayment
(
	PaymentMethod
)

SELECT DISTINCT

	PaymentMethod

FROM staging.Customer_Churn_Clean;
GO



-- VALIDATION
SELECT 
	'DimCustomer' AS TableName,
	COUNT(*) AS RowsCount

FROM dim.DimCustomer

UNION ALL

SELECT 
	'DimService',
	COUNT(*)

FROM dim.DimService

UNION ALL

SELECT 
	'DimContract',
	COUNT(*)

FROM dim.DimContract

UNION ALL

SELECT 
	'DimPayment',
	COUNT(*)

FROM dim.DimPayment;

GO