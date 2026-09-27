from validation import validate_attendance_status
def mark_attendance(students):
    roll = input("Enter Roll Number: ").upper()
    if roll not in students:
        print("Student not found.")
        return
    status = input("Enter P for Present or A for Absent: ").upper()
    if not validate_attendance_status(status):
        print("Invalid input. Enter P or A.")
        return
    if status == "P":
        students[roll]["present"] += 1
        print("Attendance marked as Present.")
    elif status == "A":
        students[roll]["absent"] += 1
        print("Attendance marked as Absent.")