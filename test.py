import cv2
import pytesseract
import re

# Read the input image
img = cv2.imread("sample.jpeg")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply OTSU thresholding to convert the image to binary
_, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

# Define a rectangular structuring element for dilation
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

# Dilation to enhance contours
dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)

# Find contours from the dilated image
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Create a copy of the original image to draw rectangles on
im2 = img.copy()

# Function to filter valid hormone names
def filter_hormones(hormone_list):
    valid_hormones = []
    for hormone in hormone_list:
        # Remove any text that is too short (e.g., less than 3 characters) or has numbers or special characters
        if len(hormone) > 2 and hormone.isalpha():
            valid_hormones.append(hormone.strip())
    return valid_hormones

# Clear the contents of the text file or create a new one
file = open("recognized.txt", "w+")
file.write("")
file.close()

# List to store recognized hormone names
hormones = []

# Loop through all the contours found
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    
    # Draw a rectangle around each contour
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Crop the region of interest (ROI) from the image
    cropped = im2[y:y + h, x:x + w]

    # Open the file to append the extracted text
    file = open("recognized.txt", "a")
    
    # Use Tesseract to extract text from the cropped image
    text = pytesseract.image_to_string(cropped)
    
    # Clean up the extracted text
    cleaned_text = text.replace("\n", " ").strip()
    
    # Split the cleaned text based on commas and newlines
    hormone_list = re.split(r'[,\n]', cleaned_text)
    
    # Clean up any empty strings or excessive spaces
    hormone_list = [hormone.strip() for hormone in hormone_list if hormone.strip()]
    
    # Filter valid hormone names from the extracted text
    valid_hormones = filter_hormones(hormone_list)
    
    # If there are valid hormone names, write them to the file and add to the list
    if valid_hormones:
        hormones.extend(valid_hormones)
        file.write(" ".join(valid_hormones) + "\n")
    
    # Close the file after writing
    file.close()

# Print the recognized hormones
print(hormones)
