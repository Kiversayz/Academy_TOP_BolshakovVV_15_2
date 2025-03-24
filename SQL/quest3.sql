SELECT D.Amount
FROM Donations D
WHERE D.Amount > ALL (
    SELECT D2.Amount
    FROM Donations D2
    WHERE D.Id <> D2.Id
);