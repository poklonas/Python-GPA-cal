SELECT Student_Records.SubjectName,Student_Records.Grade, Student.First_name, Student.Last_name
FROM Student

INNER JOIN Student_Records ON Student_Records.Student_id = Student.Student_id

WHERE (Student_Records.SubjectID='010123117');