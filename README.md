*University Attendance System*

*Overview of the Project

The **University Attendance System** is a command-line based Python project designed to manage student attendance. It allows the user to add students, mark them as Present or Absent, view the attendance details of an individual student, and view attendance information for all students.
The project is implemented using **custom Python modules**. The main program (`main.py`) imports and coordinates the functions provided by the other modules, making the project organized, modular, and easier to maintain.

*Features

- Add a new student using a roll number and name.
- Mark attendance as **Present (P)** or **Absent (A)**.
- View attendance details for a particular student.
- View attendance details of all registered students.
- Automatically calculate attendance percentage.
- Validate roll number and attendance status input.
- Display clear messages for invalid input or students that do not exist.
- Modular structure using separate user-defined Python files.
- Simple menu-driven command-line interface.

*Technologies/Tools Used

- **Python 3.x**
- **Visual Studio Code (VS Code)** – for writing and running the program
- **Python Standard Library** – basic Python functions, dictionaries, loops, conditions, and modules
- **GitHub** – for storing and sharing the project source code

*Project Structure

University_Attendance_System/
├── main.py
├── data.py
├── student.py
├── attendance.py
├── validation.py
├── display.py
└── menu.py

*Module Description

| File | Purpose |
|---|---|
| `main.py` | Main program that controls the complete application |
| `data.py` | Stores the students dictionary |
| `student.py` | Handles adding students |
| `attendance.py` | Handles Present/Absent attendance |
| `validation.py` | Validates user input |
| `display.py` | Displays student and attendance information |
| `menu.py` | Displays the main menu |

*Steps to Install & Run the Project

1. Install Python
Install **Python 3.x** on your computer if it is not already installed.
Check whether Python is installed by opening a terminal and running:
bash python --version
2. Download or Clone the Project
Download this repository or clone it using Git:
bash git clone <your-repository-url>
Then open the project folder.
3. Open the Project in VS Code
Open the project folder in **Visual Studio Code**.
Make sure all seven `.py` files are located in the same folder.
4. Run the Main Program
Open the VS Code terminal and run:
bash python main.py
Only `main.py` needs to be executed. It automatically imports the required custom modules.
5. Use the Menu
The program displays:
===== ATTENDANCE SYSTEM =====
1. Add Student
2. Mark Attendance
3. View Student Attendance
4. View All Students
5. Exit
Enter the corresponding number to perform an operation.

*Instructions for Testing

The following test cases can be used to verify that the project works correctly.
| Test | Action/Input | Expected Result |
|---|---|---|
| Add Student | Select `1` and enter a valid roll number and name | Student is added successfully |
| Duplicate Student | Enter an existing roll number | `Student already exists.` is displayed |
| Empty Roll Number | Leave the roll number blank | `Invalid Roll Number.` is displayed |
| Mark Present | Select `2`, enter an existing roll number, then `P` | Present count increases |
| Mark Absent | Select `2`, enter an existing roll number, then `A` | Absent count increases |
| Invalid Attendance | Enter a value other than `P` or `A` | Invalid input message is displayed |
| Unknown Student | Enter a roll number that does not exist | `Student not found.` is displayed |
| View Student | Select `3` and enter an existing roll number | Student attendance and percentage are displayed |
| View All Students | Select `4` | All registered students and attendance details are displayed |
| No Students | Select `4` before adding any student | `No students found.` is displayed |
| Exit | Select `5` | Program exits successfully |

*Attendance Percentage

The system calculates attendance using:
Attendance Percentage =
(Present / (Present + Absent)) × 100