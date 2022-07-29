create database student;
use student;
create user 'root' @'localhost'IDENTIFIED BY 'Who@1234';
grant all on student.*to 'root'@'localhost';
create table student(PRN varchar(12),First_Name varchar(20),Middle_Name varchar(20),Last_Name varchar(20),Address varchar(50),
Mobile_Number int, Email_ID varchar(20),DOB date);

SELECT * FROM student.student_tbl;