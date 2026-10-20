USE CustomerChurnDW;
GO


CREATE OR ALTER VIEW analytics.vw_Churn_By_Payment
AS


SELECT
	p.PaymentMethod,

	COUNT(*) AS Customers,

	SUM(CAST(f.ChurnFlag AS INT)) AS ChurnCustomers,
	CAST( 
		SUM(CAST(f.ChurnFlag AS FLOAT))
		/
		COUNT(*)
			AS DECIMAL(5,4)
		)
		AS ChurnRate

FROM fact.FactCustomerChurn f

INNER JOIN dim.DimPayment p
ON f.PaymentKey = p.PaymentKey

GROUP BY p.PaymentMethod;

GO





-- Test Query 

SELECT * 
FROM analytics.vw_Churn_By_Payment; 
GO