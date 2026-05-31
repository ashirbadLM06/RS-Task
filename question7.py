students = {}

while True:
    print("1. Add Student")
    print("2. View Student")
    print("3. View All Students")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        students[roll] = {
            "Name": name,
            "Marks": marks
        }
        print("Student added successfully!")

    elif choice == "2":
        roll = input("Enter Roll Number: ")

        if roll in students:
            print(students[roll])
        else:
            print("Student not found!")

    elif choice == "3":
        if students:
            for roll, details in students.items():
                print(f"Roll No: {roll}, Name: {details['Name']}, Marks: {details['Marks']}")
        else:
            print("No records found!")

    elif choice == "4":
        roll = input("Enter Roll Number: ")

        if roll in students:
            del students[roll]
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")