from validation import validate_roll
def add_student(students):
    roll = input("Enter Roll Number (Example: CSE101): ").upper()
    if not validate_roll(roll):
        print("Invalid Roll Number.")
        return
    name = input("Enter Student Name: ")
    if name.strip() == "":
        print("Student name cannot be empty.")
        return
    if roll in students:
        print("Student already exists.")
        return
    students[roll] = {
        "name": name,
        "present": 0,
        "absent": 0
    }
    print("Student added successfully!")