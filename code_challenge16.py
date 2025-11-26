import os
import json
os.system('cls')

print("Student information system")

studentrecords = {}

while True:
    print("Select from the options below")
    print("A- Add information")
    print("B- Print Student Record")
    print("C- Search a Record")
    print("D- Delete a Record")
    print("E- Modify a Record")
    print("F- Export Student Record")
    print("G- Import File")
    print("H- Exit System")
    Choice = input("Your Choice -->  ").lower()

    if Choice == 'a':
        print("Adding Student Information")
        
        code = input("key search -->  ")
        fname = input("Input First name -->  ").upper()
        lname = input("Input Last Name -->  ").upper()
        course = input("Input Course -->  ").upper()
        email = input("Enter email address -->  ")

        studentrecords[code] = [fname, lname, course, email]
        print("DATA SAVED")

        os.system('cls')
        continue

    elif Choice == 'b':
        print("Printing Student Record")

        for id, record in studentrecords.items():
             print(f"Student code {id} in Student Record {record}")    
        continue

    elif Choice == 'c':
        os.system('cls')
        print("Search Student Record ")
        
        searchcode = input("Input key to search -->  ").lower()

        for id in studentrecords.keys():
            if searchcode in studentrecords.keys():
                print("Record Found")
                
                for i in studentrecords[searchcode]:
                    print(i)

            else:
                print("No Recordi Found")
                
        continue
    elif Choice == 'd':
        os.system('cls')
        print("Delete Existing Record")

        searchcode = input("Input key to search -->  ").lower()

        if searchcode in studentrecords.keys():
            print("Record Found")
                
            for i in studentrecords[searchcode]:
                print(i)

            studentrecords.pop(searchcode)
            print("Record Deleted")

        else:
                
            print("No Record Found")
                
        continue

    elif Choice == 'e':
        os.system('cls')
        print("EDIT/MODIFY Existing Record")
        
        searchcode = input("Input key to search -->  ").lower()

        for id in studentrecords.keys():
            if searchcode in studentrecords.keys():
                
                print("Record Found")
                for i in studentrecords[searchcode]:
                    print(i)

                code = input("key for this student -->  ")
                fname = input("Input First name -->  ").upper()
                lname = input("Input Last Name -->  ").upper()
                course = input("Input Course -->  ").upper()
                email = input("Enter email address -->  ")

                studentrecords[searchcode][0] = fname
                studentrecords[searchcode][1] = lname
                studentrecords[searchcode][2] = course
                studentrecords[searchcode][3] = email

                print("Record Edited")

            else:
                
                print("No Record Found")
                
            break
    
    elif Choice == 'f':
        os.system('cls')
        print("Export Student Record")

        with open('studentrecords.json', 'w') as new_file:
            json.dump(studentrecords, new_file)
        print("DATA EXPORTED TO json")
        continue

    elif Choice == 'g':
        os.system('cls')
        print("Export Student Record")

        with open('studentrecords.json', 'r') as new_file:
           student_json = json.load(new_file)

           studentrecords = student_json
        print("DATA IMPORTED TO json")
        continue


    elif Choice == 'h':
        print("System exit")
        break
    else:
        print("Invalid Choice")


