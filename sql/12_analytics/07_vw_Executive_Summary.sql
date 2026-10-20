USE CustomerChurnDW;
GO


CREATE OR ALTER VIEW analytics.vw_Executive_Summary
AS


SELECT


COUNT(*) TotalCustomers,


SUM(CAST(ChurnFlag AS INT)) LostCustomers,


COUNT(*)-
SUM(CAST(ChurnFlag AS INT)) ActiveCustomers,


CAST(

SUM(CAST(ChurnFlag AS FLOAT))
/
COUNT(*)

AS DECIMAL(5,4)

) ChurnRate,


SUM(MonthlyCharges) TotalMonthlyRevenue


FROM fact.FactCustomerChurn;


GO