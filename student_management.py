students = {}

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")
        students[roll] = {"Name": name, "Marks": marks}
        print("Student Added Successfully!")

    elif choice == "2":
        for roll, data in students.items():
            print("Roll:", roll, "| Name:", data["Name"], "| Marks:", data["Marks"])

    elif choice == "3":
        roll = input("Enter Roll Number to Search: ")
        if roll in students:
            print(students[roll])
        else:
            print("Student Not Found")

    elif choice == "4":
        roll = input("Enter Roll Number to Delete: ")
        if roll in students:
            del students[roll]
            print("Student Deleted")
        else:
            print("Student Not Found")

    elif choice == "5":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
