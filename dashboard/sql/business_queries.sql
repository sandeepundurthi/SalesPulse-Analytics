-- Total Sales by Region
SELECT Region,
       ROUND(SUM(Sales),2) AS Total_Sales,
       ROUND(SUM(Profit),2) AS Total_Profit
FROM superstore
GROUP BY Region
ORDER BY Total_Sales DESC;

-- Top Loss-Making Categories
SELECT Sub_Category,
       ROUND(SUM(Profit),2) AS Total_Profit
FROM superstore
GROUP BY Sub_Category
ORDER BY Total_Profit ASC
LIMIT 5;

-- Monthly Sales Trend
SELECT
    strftime('%Y-%m', Order_Date) AS Month,
    ROUND(SUM(Sales),2) AS Monthly_Sales
FROM superstore
GROUP BY Month
ORDER BY Month;