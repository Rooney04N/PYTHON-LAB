"""Experiment 3. Manage student information with a menu and a dictionary."""


def add_student(students):
    roll = input("Enter roll number: ").strip()
    if not roll:
        print("Please enter a roll number.")
        return
    if roll in students:
        print("This roll number already exists.")
        return

    name = input("Enter name: ").strip()
    department = input("Enter department: ").strip()
    if not name or not department:
        print("Both name and department are required.")
        return
    students[roll] = {"Name": name, "Department": department}
    print("Student added successfully.")


def show_student(roll, student):
    print(f"Roll No: {roll} | Name: {student['Name']} | Department: {student['Department']}")


def view_students(students):
    if not students:
        print("No student records found.")
        return
    for roll, student in students.items():
        show_student(roll, student)


def search_student(students):
    roll = input("Enter roll number to search: ").strip()
    if roll in students:
        show_student(roll, students[roll])
    else:
        print("Student not found.")


def delete_student(students):
    roll = input("Enter roll number to delete: ").strip()
    if roll in students:
        del students[roll]
        print("Student deleted successfully.")
    else:
        print("Student not found.")


def main():
    students = {}
    while True:
        print("\n1. Add student")
        print("2. View students")
        print("3. Search student")
        print("4. Delete student")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
