USE CustomerChurnDW;
GO

DROP TABLE IF EXISTS staging.Customer_Churn_Raw;
GO

CREATE TABLE staging.Customer_Churn_Raw
(
	CustomerID VARCHAR(50),
	Gender VARCHAR(20),
	SeniorCitizen VARCHAR(10),
	Partner VARCHAR(10),
	Dependents VARCHAR(10),
	Tenure VARCHAR(20),

	PhoneService VARCHAR(20),
	MultipleLines VARCHAR(50),
	InternetService VARCHAR(50),

	OnlineSecurity VARCHAR(50),
	OnlineBackup VARCHAR(50),
	DeviceProtection VARCHAR(50),
	TechSupport VARCHAR(50),

	StreamingTV VARCHAR(50),
	StreamingMovies VARCHAR(50),

	Contract VARCHAR(50),
	PaperlessBilling VARCHAR(20),
	PaymentMethod VARCHAR(100),
	MonthlyCharges VARCHAR(50),
	TotalCharges VARCHAR(50),
	Churn VARCHAR(20)
	);

GO



-- Test Query
SELECT 
TABLE_SCHEMA,
TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_NAME='Customer_Churn_Raw';

GO