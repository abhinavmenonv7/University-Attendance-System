def view_student(students):
    roll = input("Enter Roll Number: ").upper()
    if roll not in students:
        print("Student not found.")
        return
    name = students[roll]["name"]
    present = students[roll]["present"]
    absent = students[roll]["absent"]
    total = present + absent
    if total > 0:
        percentage = (present / total) * 100
    else:
        percentage = 0
    print("\n--- Student Attendance ---")
    print("Name:", name)
    print("Roll Number:", roll)
    print("Present:", present)
    print("Absent:", absent)
    print("Attendance:", round(percentage, 2), "%")
def view_all_students(students):
    if len(students) == 0:
        print("No students found.")
        return
    print("\n========== ALL STUDENTS ==========")
    for roll, student in students.items():
        name = student["name"]
        present = student["present"]
        absent = student["absent"]
        total = present + absent
        if total > 0:
            percentage = (present / total) * 100
        else:
            percentage = 0
        print("\nName:", name)
        print("Roll Number:", roll)
        print("Present:", present)
        print("Absent:", absent)
        print("Attendance:", round(percentage, 2), "%")