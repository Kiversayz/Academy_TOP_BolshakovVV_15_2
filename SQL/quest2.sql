SELECT W.Name AS WardName
FROM Wards W
WHERE W.Places > ANY (
    SELECT W2.Places
    FROM Wards W2
    WHERE W2.DepartmentId = W.DepartmentId
);

SELECT Doc.Name, Doc.Surname
FROM Doctors Doc
WHERE Doc.Salary < SOME (
    SELECT Doc2.Salary
    FROM Doctors Doc2
);