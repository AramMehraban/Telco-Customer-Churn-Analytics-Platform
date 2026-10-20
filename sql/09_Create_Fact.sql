
-- 09 CREATE FACT TABLE

USE CustomerChurnDW;
GO


DROP TABLE IF EXISTS fact.FactCustomerChurn;
GO



CREATE TABLE fact.FactCustomerChurn
(
	ChurnFactKey INT IDENTITY(1,1)
	PRIMARY KEY,
	CustomerKey INT NOT NULL,
	ServiceKey INT NOT NULL,
	ContractKey INT NOT NULL,
	PaymentKey INT NOT NULL,
	ChurnFlag BIT NOT NULL,
	MonthlyCharges DECIMAL(10,2),
	TotalCharges DECIMAL(10,2)
);

GO


-- Test 
SELECT *
FROM fact.FactCustomerChurn;
GO