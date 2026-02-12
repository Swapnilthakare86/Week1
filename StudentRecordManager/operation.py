from validation import input_nonempty,input_int,check_email

import json
import os

filename = "student_records.json"


# file check not exit then create
def init_file():
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            json.dump([], file)


#read data from file
def read():
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return data
        
    except FileNotFoundError:
        print("File not found.")
        
    except:
        print("Error in reading file") 


# Write data to file
def write(data):
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
    
    except FileNotFoundError:
        print("File not found.")

    except:
        print("Error writing file")

    

def addStudent():
    data = read()

    rollNo = input_nonempty("Enter Roll No: ")

    # Check if rollNo already exists
    if any(student["rollNo"] == rollNo for student in data):
        print("Roll No already exists!")
        return

    name = input_nonempty("Enter Name: ")
    age =  input_int("Enter Age: ")
    grade = input_nonempty("Enter Grade: ")
    email = check_email("Enter Email: ")

    new_student = {
        "rollNo": rollNo,
        "name": name,
        "age": age,
        "grade": grade,
        "email": email
    }

    data.append(new_student)
    write(data)
    print("Student added.")


def viewStudents():
    data = read()

    if not data:
        print("No student records found.")
        return

    print("\n--- Student Records ---\n")
    for student in data:
        print(f"Roll No: {student['rollNo']}  Name: {student['name']}  Age: {student['age']}   Grade: {student['grade']}  Email: {student['email']}")


def updateStudent():
    data = read()

    update_roll = input_nonempty("Enter Roll No: ")

    for student in data:
        if student["rollNo"] == update_roll:
            student["name"] = input_nonempty("New Name: ")
            student["age"] =  input_int("New Age: ")
            student["grade"] = input_nonempty("New Grade: ")
            student["email"] = input_nonempty("New Email: ")

            write(data)
            print("Student updated.")
            return

    print("Student not found.")


def deleteStudent():
    data = read()

    delete_roll = input_nonempty("Enter Roll No: ")

    new_data = [student for student in data if student["rollNo"] != delete_roll]

    if len(new_data) == len(data):
        print("Student not found.")

    else:
        write(new_data)
        print("Student deleted.")


def searchStudent():
    data = read()
    search_roll = input_nonempty("Enter Roll No to Search: ")

    for student in data:
        if student["rollNo"] == search_roll:
            print(f"Roll No: {student['rollNo']}   Name: {student['name']}    Age: {student['age']}  Grade: {student['grade']}  Email: {student['email']}")
            return

    print("Student not found.")
