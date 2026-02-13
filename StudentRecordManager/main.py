from operation import ( addStudent, viewStudents, updateStudent, deleteStudent,searchStudent,init_file,filterByGrade)

def main():
    init_file()

    while True:
        print("\n===== Student Record Manager =====\n")
        print("1. Add Student Record")
        print("2. View Student Records")
        print("3. Update Student Record")
        print("4. Delete Student Record")
        print("5. Search Student Record")
        print("6.Search Student ByGrade")
        print("7. Exit")

        choice = input("Enter Your Choice: ")


        if choice == "1":
            addStudent()
        elif choice == "2":
            viewStudents()
        elif choice == "3":
            updateStudent()
        elif choice == "4":
            deleteStudent()
        elif choice == "5":
            searchStudent()
        elif choice =="6":
            filterByGrade()
        elif choice == "7":
            print("Exiting program...")
            break
        else:
            print("Invalid Choice.")

        



if __name__ == "__main__":
    main()
