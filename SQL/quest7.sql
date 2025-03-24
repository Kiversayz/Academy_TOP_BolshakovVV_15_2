/* INNER */
SELECT Doc.Name, Doc.Surname, E.Name AS ExaminationName
FROM Doctors Doc
INNER JOIN DoctorsExaminations DE ON Doc.Id = DE.DoctorId
INNER JOIN Examinations E ON DE.ExaminationId = E.Id;
/* LEFT */
SELECT Doc.Name, Doc.Surname, E.Name AS ExaminationName
FROM Doctors Doc
LEFT JOIN DoctorsExaminations DE ON Doc.Id = DE.DoctorId
LEFT JOIN Examinations E ON DE.ExaminationId = E.Id;
/* RIGHT */
SELECT Doc.Name, Doc.Surname, E.Name AS ExaminationName
FROM Doctors Doc
RIGHT JOIN DoctorsExaminations DE ON Doc.Id = DE.DoctorId
RIGHT JOIN Examinations E ON DE.ExaminationId = E.Id;
/* FULL */
SELECT Doc.Name, Doc.Surname, E.Name AS ExaminationName
FROM Doctors Doc
FULL JOIN DoctorsExaminations DE ON Doc.Id = DE.DoctorId
FULL JOIN Examinations E ON DE.ExaminationId = E.Id;
/* LEFT + RIGHT */
SELECT Doc.Name, Doc.Surname, E.Name AS ExaminationName
FROM Doctors Doc
LEFT JOIN DoctorsExaminations DE ON Doc.Id = DE.DoctorId
LEFT JOIN Examinations E ON DE.ExaminationId = E.Id
UNION
SELECT Doc.Name, Doc.Surname, E.Name AS ExaminationName
FROM Doctors Doc
RIGHT JOIN DoctorsExaminations DE ON Doc.Id = DE.DoctorId
RIGHT JOIN Examinations E ON DE.ExaminationId = E.Id;