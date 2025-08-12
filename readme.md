# File Organizer

## Description

This project is written in Python.

The purpose of this project is to :

help users organize their files by moving them into appropriate directories based on file types. The script scans a specified directory and sorts files into subdirectories like 'Images', 'Documents', 'Videos', etc.

## How to Run

1. Make sure you have Python installed on your system.  
2. Clone this repository or download the project files.  
3. Open a terminal and navigate to the project directory.
4. type the following command to run the script:

```bash
     python file_organizer.py "path/to/your/source/directory" "path/to/your/destination/directory"
        # The script will move files from the source directory to the destination directory based on their file types.
    python file_organizer.py "path/to/your/source/directory" "path/to/your/destination/directory" --simulate
        # The script will display the actions it would take without actually moving any files.