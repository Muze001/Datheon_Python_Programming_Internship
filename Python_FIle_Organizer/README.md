 Automated File Organizer

 Project Overview

The Automated File Organizer is a Python application that automatically organizes files into categorized folders based on their file extensions.

The application reduces the time spent manually organizing files and helps maintain a clean directory structure.

 Features

- Automatically scans a specified directory.
- Identifies files using their extensions.
- Creates category folders automatically.
- Moves files into their appropriate folders.
- Handles unknown file extensions using an Others folder.
- Prevents duplicate filenames from overwriting existing files.
- Handles operating-system errors.
- Displays an execution summary.

 Technologies Used

- Python 3
- pathlib
- shutil

 Project Structure

text
Python_File_Organizer/
│
├── organizer.py
├── README.md
│
└── Test_Files/


 File Categories

| File Types | Category |
|---|---|
| PDF, DOCX, PPTX, TXT, XLSX | Documents |
| JPG, JPEG, PNG, GIF | Images |
| MP4, MOV | Videos |
| MP3, WAV | Audio |
| ZIP, RAR | Archives |
| PY, JS, HTML, CSS | Code |
| Unrecognized extensions | Others |

 How to Run

1. Install Python 3.
2. Clone or download the project.
3. Open the project folder in VS Code.
4. Place test files inside the Test_Files directory.
5. Run:

bash
python organizer.py


6. Check the automatically created category folders.

 Python Concepts Demonstrated

- Variables and data types
- Dictionaries
- Functions
- Loops
- Conditional statements
- Exception handling
- File system operations
- Path manipulation
- File movement and automation

 Learning Outcome

This project demonstrates how Python can interact with the operating system to automate repetitive file management tasks.