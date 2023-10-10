import pytesseract
from PIL import Image

# Load the image
image = Image.open(r"C:\Users\wempro1\Downloads\1.png")

# Perform OCR
text = pytesseract.image_to_string(image, lang="eng", config="--psm 6")

# Print the extracted text
print(text)
