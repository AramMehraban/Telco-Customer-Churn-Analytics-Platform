
-- 06 DATA QUALITY REPORT


USE CustomerChurnDW;
GO


DROP TABLE IF EXISTS analytics.DataQuality_Report;
GO


CREATE TABLE analytics.DataQuality_Report
(
	ID INT IDENTITY PRIMARY KEY,
	Metric VARCHAR(100),
	Value INT,
	Status VARCHAR(20)
);

GO


INSERT INTO analytics.DataQuality_Report
(
	Metric,
	Value,
	Status
)



SELECT
	'Raw Rows',
	COUNT(*),
	'PASS'

FROM staging.Customer_Churn_Raw

UNION ALL

SELECT
	'Clean Rows',
	COUNT(*),
	'PASS'

FROM staging.Customer_Churn_Clean

UNION ALL

SELECT
   	'Duplicate Customers',
	COUNT(*),

	CASE
	WHEN COUNT(*)=0 THEN 'PASS'
	ELSE 'FAIL'
	END

FROM

	(
	SELECT CustomerID
	FROM staging.Customer_Churn_Clean
	GROUP BY CustomerID
	HAVING COUNT(*)>1
	) D;

GO




-- FINAL TEST

SELECT *
FROM analytics.DataQuality_Report;
GO