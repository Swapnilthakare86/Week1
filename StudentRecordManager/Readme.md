# Python: CLI-based student record manager

# project Structure

|
----main.py 
|
--- operation.py
|
--- validation.py

# Run the program:

 python main.py


# main.py 

 In this file the created menu and take input from user choice.

 In this what choice user enter that function execute

 1.Add new student records
 2.View all student records
 3.Update an existing student record
 4.Delete a student record
 5.Search for a student by Roll Number


# operation.py
 
 # File Storage
        Records are stored in student_records.json.
        File is created automatically if it doesn't exist.  

 functions
    addStudent(): Add a new student.
    viewStudents(): Display all students
    updateStudent(): Update student details by Roll No.
    deleteStudent(): Delete student by Roll No.
    searchStudent(): Search for a student by Roll No.


# validation

input_int(prompt): Ensures numeric input.
input_nonempty(prompt): Ensures input is not empty.
check_email(prompt): Ensures the email contains @gmail.com.