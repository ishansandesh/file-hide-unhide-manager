
![Screenshot](img.png)

# File Hide/Unhide Manager - Windows CLI

This project provides a command-line tool to hide and unhide files using Python and SQLite3. It helps users manage file visibility by storing the status of hidden files in a database.

## Features

- **Hide Files:** Mark files as hidden in the file system and store their paths in the database.
- **Unhide Files:** Unmark files from hidden status and remove their paths from the database.
- **List Hidden Files:** Display all currently hidden files stored in the database.

## Prerequisites

- Python 3.x
- SQLite3

## Getting Started

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/file-hide-unhide-manager.git
    cd file-hide-unhide-manager
    ```

2. **Install required Python packages:**

    ```sh
    pip install sqlite3
    ```

### Usage

1. **Run the script:**

    ```sh
    python hiden_file.py
    ```

2. **Follow the on-screen instructions:**

    - Enter the full path of the file you want to hide or unhide.
    - Choose whether to hide or unhide the file.
    - Use the `showup` command to list all hidden files stored in the database.
    - Use the `exit` command to exit the program.

### Script Workflow

1. The script creates a database and a table (`file_path`) if they don't exist.
2. It prompts the user to enter a file path.
3. The user can choose to hide or unhide the file:
    - If hiding, the file path and status are stored in the database.
    - If unhiding, the file path is removed from the database.
4. Users can list all hidden files using the `showup` command.
5. The program exits when the user enters the `exit` command.

## Code Overview

- **Database Connection:**
    ```python
    con = sqlite3.connect("file_data.db")
    cursor = con.cursor()
    ```

- **Table Creation:**
    ```python
    create_table = """CREATE TABLE IF NOT EXISTS file_path (
        file_name VARCHAR(255) PRIMARY KEY, 
        status VARCHAR(5)
    )"""
    cursor.execute(create_table)
    con.commit()
    ```

- **File Hiding/Unhiding Logic:**
    ```python
    os.system(fr'attrib +h "{directory}"')
    cursor.execute("INSERT INTO file_path (file_name, status) VALUES (?, ?)", (directory, 'h'))
    con.commit()
    ```

- **Show Hidden Files:**
    ```python
    cursor.execute("SELECT * FROM file_path")
    list_files = cursor.fetchall()
    ```

## Contributing

Contributions are welcome! Please create a pull request or open an issue for any feature requests or bugs.

## Acknowledgments

- This project uses `os` and `sqlite3` libraries from Python's standard library.

---
