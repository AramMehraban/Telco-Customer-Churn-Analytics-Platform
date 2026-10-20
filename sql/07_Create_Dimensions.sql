USE CustomerChurnDW;
GO


DROP TABLE IF EXISTS fact.FactCustomerChurn;
DROP TABLE IF EXISTS dim.DimCustomer;
DROP TABLE IF EXISTS dim.DimService;
DROP TABLE IF EXISTS dim.DimContract;
DROP TABLE IF EXISTS dim.DimPayment;
Go


-- DIM CUSTOMER

CREATE TABLE dim.DimCustomer
(
    CustomerKey INT IDENTITY(1,1) PRIMARY KEY,

    CustomerID VARCHAR(50),
    Gender VARCHAR(20),
    SeniorCitizen BIT,
    Partner VARCHAR(10),
    Dependents VARCHAR(10),
    Tenure INT
);
GO



-- DIM SERVICE

CREATE TABLE dim.DimService
(
    ServiceKey INT IDENTITY(1,1) PRIMARY KEY,

    PhoneService VARCHAR(20),
    MultipleLines VARCHAR(30),

    InternetService VARCHAR(30),

    OnlineSecurity VARCHAR(30),
    OnlineBackup VARCHAR(30),
    DeviceProtection VARCHAR(30),
    TechSupport VARCHAR(30),

    StreamingTV VARCHAR(30),
    StreamingMovies VARCHAR(30)
);
GO




-- DIM CONTRACT

CREATE TABLE dim.DimContract
(
    ContractKey INT IDENTITY(1,1) PRIMARY KEY,

    Contract VARCHAR(50),
    PaperlessBilling VARCHAR(20)
);
GO




-- DIM PAYMENT

CREATE TABLE dim.DimPayment
(
    PaymentKey INT IDENTITY(1,1) PRIMARY KEY,

    PaymentMethod VARCHAR(100)
);
GO


-- CHECK TABLES
SELECT 
    TABLE_SCHEMA,
    TABLE_NAME

FROM INFORMATION_SCHEMA.TABLES

    WHERE TABLE_SCHEMA IN
    (
        'dim',
        'fact'
    );

GO