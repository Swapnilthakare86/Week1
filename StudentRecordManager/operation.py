import json
import os

filename="student_records.json"

#initialise file
def init_file():
    if not os.path.exits(filename):
        with open(filename,"w") as file:
            json.dump([],file)

#read from file
def read():
    with open(filename,"r") as file:
        return json.load(file)

#write to file
def write(data):
    with open(filename,"w") as file:
        json.dump(data,file,indent=4)


#Add function
def addStudent():
    data=read()

    rollNo=input("Enter roll No: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    grade = input("Enter Grade: ")
    email = input("Enter Email: ")

    new_student={
        "rollNo":rollNo,
        "name":name,
        "age":age,
        "grade":grade,
        "email":email
    }

    data.append(new_student)
    write(data)
    print("Student Added.")


#View Funcion
def viewStudets():
    data=read()
    if not data:
        print("No Student Record Found.")

    print("\n Student Records.")
    for Student in data:
        print(Student)


def updateStudent():
    data=read()

    update_roll=int(input("Enter RollNo for Update:"))

    for student in data:
        if student["rollno"] == update_roll:
            student["name"] = input("New Name: ")
            student["age"] = input("New Age: ")
            student["grade"] = input("New Grade: ")
            student["email"] = input("New Email: ")

            write(data)
            print("Student updated successfully!")
            return
        
        else:
            print("Student Not found.")


def deleteStudent():
    data=read()

    delete_roll=int(input("Enter RollNo for Delete"))




def searchStudent():
    data =read()




