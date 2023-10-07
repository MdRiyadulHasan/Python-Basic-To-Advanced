from pathlib import Path

path = Path("OS Module/2_os.py")

print("Name:", path.name)
print("Parent Directory:", path.parent)
print("Suffix:", path.suffix)
print("Stem:", path.stem)
print("Exists:", path.exists())
print("Is File:", path.is_file())
print("Is Directory:", path.is_dir())
