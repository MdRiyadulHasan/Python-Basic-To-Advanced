import os

# Join paths correctly for the current OS
path = os.path.join("path", "to", "file.txt")
print("Joined Path:", path)

# Get the directory and filename from a path
dir_name, file_name = os.path.split(path)
print("Directory:", dir_name)
print("Filename:", file_name)
import os

# Run a shell command (e.g., listing files in the current directory)
os.system("ls")


# Get the value of an environment variable
python_path = os.getenv("PYTHONPATH")
print("PYTHONPATH:", python_path)

path1 = "folder1"
path2 = "file.txt"

full_path = os.path.join(path1, path2)
print("Full Path:", full_path)
