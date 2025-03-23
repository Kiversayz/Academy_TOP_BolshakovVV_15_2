SELECT Dep.Name AS DepartmentName
FROM Departments Dep
WHERE 
    (SELECT COUNT(*) FROM Donations D WHERE D.DepartmentId = Dep.Id) > ANY (
        SELECT COUNT(*)
        FROM Donations D2
        WHERE D2.DepartmentId <> Dep.Id
    )
AND 
    (SELECT COUNT(*) FROM Donations D WHERE D.DepartmentId = Dep.Id) <= ALL (
        SELECT COUNT(*)
        FROM Donations D3
        WHERE D3.DepartmentId <> Dep.Id
    );