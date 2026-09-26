import os
import time

def get_file_info(filepath):
    # Check if file exists
    if not os.path.exists(filepath):
        return " File not found! Please check the path and try again."

    # Extract file details
    file_name = os.path.basename(filepath)
    file_size = os.path.getsize(filepath)
    created_time = time.ctime(os.path.getctime(filepath))
    modified_time = time.ctime(os.path.getmtime(filepath))
    absolute_path = os.path.abspath(filepath)

    # Convert size to KB
    file_size_kb = file_size / 1024

    # Format output
    info = f"""
 FILE INFORMATION
---------------------------
File Name       : {file_name}
File Size       : {file_size_kb:.2f} KB
Created On      : {created_time}
Last Modified   : {modified_time}
Absolute Path   : {absolute_path}
---------------------------
"""
    return info


if __name__ == "__main__":
    print(" File Metadata Extractor")

    while True:
        filepath = input("\nEnter file path (or type 'exit' to quit): ")

        if filepath.lower() == "exit":
            print("Goodbye! ")
            break

        print(get_file_info(filepath))
