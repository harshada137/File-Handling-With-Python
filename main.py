# Import os module to interact with the operating system
# Used for file, directory, and path operations
import os

# Import shutil module
# Used for high-level file operations like deleting folders and moving files
import shutil


# Function to display the main menu
def show_menu():
    print("\n📁 FILE MANAGER")
    print("1. List files and folders")
    print("2. Create a file")
    print("3. Create a folder")
    print("4. Delete a file")
    print("5. Delete a folder")
    print("6. Rename file/folder")
    print("7. Move file")
    print("8. Show current directory")
    print("9. Exit")


# Function to list all files and folders in the current directory
def list_items():
    # Get list of files and folders
    items = os.listdir()

    # Check if directory is empty
    if not items:
        print("📂 Directory is empty")
    else:
        # Print each file/folder name
        for item in items:
            print(item)


# Function to create a new file
def create_file():
    name = input("Enter file name: ")

    # Create an empty file in write mode
    open(name, 'w').close()

    print("✅ File created")


# Function to create a new folder
def create_folder():
    name = input("Enter folder name: ")

    # Create directory
    os.mkdir(name)

    print("✅ Folder created")


# Function to delete a file
def delete_file():
    name = input("Enter file name to delete: ")

    # Check if the file exists
    if os.path.isfile(name):
        os.remove(name)  # Delete file
        print("🗑️ File deleted")
    else:
        print("❌ File not found")


# Function to delete a folder
def delete_folder():
    name = input("Enter folder name to delete: ")

    # Check if folder exists
    if os.path.isdir(name):
        shutil.rmtree(name)  # Delete folder and its contents
        print("🗑️ Folder deleted")
    else:
        print("❌ Folder not found")


# Function to rename a file or folder
def rename_item():
    old = input("Enter old name: ")
    new = input("Enter new name: ")

    # Check if file/folder exists
    if os.path.exists(old):
        os.rename(old, new)
        print("✏️ Renamed successfully")
    else:
        print("❌ Item not found")


# Function to move a file to another folder
def move_file():
    file_name = input("Enter file name: ")
    destination = input("Enter destination folder path: ")

    # Check if file and destination folder exist
    if os.path.isfile(file_name) and os.path.isdir(destination):
        shutil.move(file_name, destination)
        print("📦 File moved")
    else:
        print("❌ Invalid file or destination")


# Function to show current working directory
def current_directory():
    print("📍 Current Directory:")
    print(os.getcwd())


# Infinite loop to keep the program running
while True:
    show_menu()  # Display menu
    choice = input("Choose an option (1-9): ")

    # Call function based on user choice
    if choice == '1':
        list_items()
    elif choice == '2':
        create_file()
    elif choice == '3':
        create_folder()
    elif choice == '4':
        delete_file()
    elif choice == '5':
        delete_folder()
    elif choice == '6':
        rename_item()
    elif choice == '7':
        move_file()
    elif choice == '8':
        current_directory()
    elif choice == '9':
        print("👋 Exiting File Manager")
        break  # Exit loop and program
    else:
        print("❌ Invalid choice")
