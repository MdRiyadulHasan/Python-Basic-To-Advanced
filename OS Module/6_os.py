import glob

# Find all .txt files in the current directory and its subdirectories
all_txt_files = glob.glob("**/*.py", recursive=True)
print("All Text Files:", all_txt_files)

