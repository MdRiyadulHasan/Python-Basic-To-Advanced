import os

# Create a directory
os.mkdir("my_directory")

# Rename a directory
os.rename("my_directory", "new_directory")

# Remove a directory
# os.rmdir("new_directory")

# Get the current working directory
cwd = os.getcwd()
print("Current Directory:", cwd)

# List files and directories in a directory
files_and_dirs = os.listdir(cwd)
print("Files and Directories:", files_and_dirs)
