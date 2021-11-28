UPDATE Clients SET date_of_reg = SUBSTR(date_of_reg, 7, 4) || '-' || SUBSTR(date_of_reg, 4, 2) || '-' || SUBSTR(date_of_reg, 1, 2);
SELECT name FROM Clients WHERE date_of_reg = (SELECT max(date_of_reg) FROM Clients);
SELECT DISTINCT date_of_birth FROM Clients;
SELECT COUNT(*) AS "total_items" FROM Products;
SELECT AVG(DATEDIFF("YYYY", GETDATE(), date_of_birth)) FROM Clients WHERE (DATEDIFF("YYYY", GETDATE(), SELECT date_of_reg FROM Clients) < 2);