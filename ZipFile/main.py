import pyminizip
import os

def add_password_to_file(file_path, new_file_path, password):
    if not os.path.isfile(file_path):
        print(f"File {file_path} does not exist.")
        return

    pyminizip.compress(file_path, None, new_file_path, password, 5)
    print(f"File has been zipped with password and saved as: {new_file_path}")

def main():

    file_path = input("Please enter the path to your file: ").strip()
    
    
    file_name = input("Please enter the name of the zip file with .zip extension: ").strip()
    
    
    save_directory = input("Please enter the directory where you want to save the ZIP file: ").strip()

    
    if not os.path.exists(save_directory):
        print(f"Directory {save_directory} does not exist. Creating it now.")
        os.makedirs(save_directory)

    
    new_file_path = os.path.join(save_directory, file_name)
    
    
    password_choice = input("Do you want to add a password? (yes or no): ").strip().lower()
    
    if password_choice == "yes":
        file_password = input("Please enter the password: ").strip()
        add_password_to_file(file_path, new_file_path, file_password)
        print(f"File has been zipped with password.")
    elif password_choice == "no":
        pyminizip.compress(file_path, None, new_file_path, None, 5)
        print(f"File has been zipped without password and saved as: {new_file_path}")
    else:
        print("Your entry is not correct. Please try again.")

if __name__ == "__main__":
    main()
