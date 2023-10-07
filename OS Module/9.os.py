from pathlib import Path

directory = Path("OS Module")

# List all files in the directory
for file in directory.iterdir():

    print(file)

# List all Python files in the directory
for file in directory.glob("*.py"):
    pass
    # print(file)
