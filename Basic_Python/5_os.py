import os

path = "/home/user/documents/file.txt"

dir_name, file_name = os.path.split(path)
print("Directory:", dir_name)
print("Filename:", file_name)

filename = "document.pdf"

root, extension = os.path.splitext(filename)
print("Root:", root)
print("Extension:", extension)

file_path = "3_os.py"

if os.path.exists(file_path):
    print(f"{file_path} exists")
else:
    print(f"{file_path} does not exist")
