-- Total revenue
SELECT SUM(MonthlyCharges) AS TotalRevenue FROM customers;

-- Churn rate
SELECT COUNT(*) AS TotalCustomers,
       SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS Churned,
       ROUND(SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)*100.0/COUNT(*),2) AS ChurnRate
FROM customers;

-- Average tenure by contract type
SELECT Contract, ROUND(AVG(tenure),1) AS AvgTenure
FROM customers
GROUP BY Contract;

-- Top 5 customers by CLV
SELECT customerID, CLV
FROM customers
ORDER BY CLV DESC
LIMIT 5;
