from data import students
from student import add_student
from attendance import mark_attendance
from display import view_student, view_all_students
from menu import show_menu
while True:
    show_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        add_student(students)
    elif choice == "2":
        mark_attendance(students)
    elif choice == "3":
        view_student(students)
    elif choice == "4":
        view_all_students(students)
    elif choice == "5":
        print("Thank you for using Attendance System!")
        break
    else:
        print("Invalid choice. Please try again.")