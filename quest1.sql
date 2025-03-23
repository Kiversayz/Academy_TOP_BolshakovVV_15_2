SELECT D.Name AS DepartmentName
FROM Departments D
WHERE EXISTS (
    SELECT 1
    FROM Doctors Doc
    WHERE Doc.Id = D.Id
);

SELECT S.Name AS SponsorName
FROM Sponsors S
WHERE EXISTS (
    SELECT 1
    FROM Donations D
    WHERE D.SponsorId = S.Id
);