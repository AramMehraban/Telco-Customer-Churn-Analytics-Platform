--------------------------------------------------
-- 02 CREATE SCHEMAS
--------------------------------------------------

USE CustomerChurnDW;
GO


CREATE SCHEMA staging;
GO

CREATE SCHEMA dim;
GO

CREATE SCHEMA fact;
GO

CREATE SCHEMA analytics;
GO

-- Test Query

SELECT 
name AS SchemaName
FROM sys.schemas
WHERE name IN
(
'staging',
'dim',
'fact',
'analytics'
);

GO