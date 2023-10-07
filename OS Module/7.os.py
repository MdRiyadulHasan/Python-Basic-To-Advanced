import glob

# Find files starting with "file" and having numeric extensions
numeric_files = glob.glob("[0-9]*.[a-zA-Z]*")
print("Numeric Files:", numeric_files)


# Iterate through all .txt files and print their names
txt_files = glob.glob("*.py")
for file in txt_files:
    pass

    # print("File:", file)


# Find and sort all .txt files in the current directory
txt_files = sorted(glob.glob("*.py"))
print("Sorted Text Files:", txt_files)
