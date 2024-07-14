import os
import sqlite3

# Establish database connection
con = sqlite3.connect("file_data.db")
cursor = con.cursor()

# Create the table if it doesn't exist
create_table = """CREATE TABLE IF NOT EXISTS file_path (
    file_name VARCHAR(255) PRIMARY KEY, 
    status VARCHAR(5)
)"""
cursor.execute(create_table)
con.commit()

current = True

while current:
    print("\n")
    print("""\n███████╗██╗██╗     ███████╗    ██╗  ██╗██╗██████╗ ██████╗ ███████╗██████╗ 
               ██╔════╝██║██║     ██╔════╝    ██║  ██║██║██╔══██╗██╔══██╗██╔════╝██╔══██╗
               █████╗  ██║██║     █████╗      ███████║██║██║  ██║██║  ██║█████╗  ██████╔╝
               ██╔══╝  ██║██║     ██╔══╝      ██╔══██║██║██║  ██║██║  ██║██╔══╝  ██╔══██╗
               ██║     ██║███████╗███████╗    ██║  ██║██║██████╔╝██████╔╝███████╗██║  ██║
               ╚═╝     ╚═╝╚══════╝╚══════╝    ╚═╝  ╚═╝╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                          \n""")
    print("Enter File Full-Path (With File extensions)")
    print("Exit -> exit")
    print("Get-Hidden files -> showup")
    directory = input(">> ")

    if directory.lower() == "exit":
        current = False
        print("Good Bye!")
        break

    elif directory.lower() == "showup":
        cursor.execute("SELECT * FROM file_path")
        list_files = cursor.fetchall()
        if not list_files:
            print("\nNo hidden files found.")
        else:
            for i, file in enumerate(list_files, start=1):
                print(f"{i}. {file[0]}")
        continue

    if not os.path.isfile(directory):
        print(f"The file {directory} does not exist. Please check the path and try again.")
        continue

    method = input("Hide(h) or Unhide(u) -> ")
    if method.lower() == "h":
        try:
            os.system(fr'attrib +h "{directory}"')
            print("\n*** Success Hide ***\n")
            try:
                cursor.execute("INSERT INTO file_path (file_name, status) VALUES (?, ?)", (directory, 'h'))
                con.commit()
                print("Data saved!")
            except sqlite3.IntegrityError:
                print("The file is already hidden and saved in the database.")
        except Exception as e:
            print(f"Something went wrong! (File-path not found)\nError: {e}")
    elif method.lower() == "u":
        try:
            os.system(fr'attrib -h "{directory}"')
            print("\n*** Success Unhide ***\n")
            try:
                cursor.execute("DELETE FROM file_path WHERE file_name = ?", (directory,))
                con.commit()
                print("Data removed!")
            except Exception as e:
                print(f"Error while removing data from the database.\nError: {e}")
        except Exception as e:
            print(f"Something went wrong! (File-path not found)\nError: {e}")
    else:
        print("Wrong Command")

con.close()
