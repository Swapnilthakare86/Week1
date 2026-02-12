
from operation import (addStudent,viewStudets,updateStudent,deleteStudent,searchStudent,init_file)

def main():
    
    init_file()

    while(True):
        print("Student Record Manager")
        print("1.Add Student Record")
        print("2.View Student Records")
        print("3.Update Student Record")
        print("4.Delete Student Record")
        print("5.Search Student Record")
        print("6.Exit")

        choice=input("Enter Your Choice:")

        if choice==1:
            addStudent()

        elif choice==2:
            viewStudets()
 
        elif choice==3:
            updateStudent()

        elif choice==4:
            deleteStudent()

        elif choice==5:
            searchStudent()

        elif choice==6:
            print("Exit program.")
            break
        
        else:
            print("Invalid Choice.")

if __name__=="__main__":
    main()

            
            

       

       
       


