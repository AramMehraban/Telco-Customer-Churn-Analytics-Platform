USE CustomerChurnDW;
GO

DROP TABLE IF EXISTS staging.Customer_Churn_Clean;
GO

CREATE TABLE staging.Customer_Churn_Clean
(
	CustomerID VARCHAR(50),
	Gender VARCHAR(20),
	SeniorCitizen BIT,
	Partner VARCHAR(10),
	Dependents VARCHAR(10),
	Tenure INT,

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

	MonthlyCharges DECIMAL(10,2),
	TotalCharges DECIMAL(10,2),

	Churn VARCHAR(20)


);
GO

INSERT INTO staging.Customer_Churn_Clean
(
	CustomerID,
	Gender,
	SeniorCitizen,
	Partner,
	Dependents,
	Tenure,
	PhoneService,
	MultipleLines,
	InternetService,
	OnlineSecurity,
	OnlineBackup,
	DeviceProtection,
	TechSupport,
	StreamingTV,
	StreamingMovies,
	Contract,
	PaperlessBilling,
	PaymentMethod,
	MonthlyCharges,
	TotalCharges,
	Churn
)

SELECT

	CustomerID,

	LTRIM(RTRIM(Gender)),

CASE
	WHEN SeniorCitizen='1'
	THEN 1
	ELSE 0
END,

	LTRIM(RTRIM(Partner)),
	LTRIM(RTRIM(Dependents)),

	CAST(Tenure AS INT),

	LTRIM(RTRIM(PhoneService)),
	LTRIM(RTRIM(MultipleLines)),
	LTRIM(RTRIM(InternetService)),
	LTRIM(RTRIM(OnlineSecurity)),
	LTRIM(RTRIM(OnlineBackup)),
	LTRIM(RTRIM(DeviceProtection)),
	LTRIM(RTRIM(TechSupport)),
	LTRIM(RTRIM(StreamingTV)),
	LTRIM(RTRIM(StreamingMovies)),

	LTRIM(RTRIM(Contract)),

	LTRIM(RTRIM(PaperlessBilling)),
	LTRIM(RTRIM(PaymentMethod)),

	CAST(MonthlyCharges AS DECIMAL(10,2)),

		CASE
			WHEN TotalCharges=''
			THEN NULL
			ELSE CAST(TotalCharges AS DECIMAL(10,2))
		END,

		CASE

			WHEN UPPER(LTRIM(RTRIM(Churn))) LIKE 'YES%'
			THEN 'Yes'

			WHEN UPPER(LTRIM(RTRIM(Churn))) LIKE 'NO%'
			THEN 'No'

		END

FROM staging.Customer_Churn_Raw;

GO

-- TEST CLEAN TABLE
SELECT COUNT(*) CleanRows
FROM staging.Customer_Churn_Clean;

-- TEST CHURN DISTRIBUTION
SELECT
	Churn,
	COUNT(*) AS Customers

FROM staging.Customer_Churn_Clean
GROUP BY Churn;


-- TEST NULL TOTAL CHARGES
SELECT

	COUNT(*) AS Missing_TotalCharges

FROM staging.Customer_Churn_Clean
WHERE TotalCharges IS NULL;
GO