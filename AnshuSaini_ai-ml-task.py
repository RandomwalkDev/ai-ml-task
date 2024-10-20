# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17AyuY5Ocj8Whzke_L_m3nrYmWlQmF11S

**Submitted By:- Anshu Saini (IIITDM Kancheepuram Btech in CSE-AI)
Email:- anshucodes4u@gamil.com / cs22b2051@iiitdm.ac.in
**
"""

pip install pytesseract

pip install langchain_groq

!sudo apt install tesseract-ocr
!sudo apt install libtesseract-dev

import cv2
import pytesseract
from pytesseract import Output
from collections import defaultdict
from langchain_groq import ChatGroq
import json
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

# Preprocessing the image and performing OCR
def preprocessing(path):
    image = cv2.imread(path)  # reading the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # grayscaling
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)  # thresholding to binarize the image
    custom_config = r'--oem 3 --psm 6'  # Default config for structured output
    data = pytesseract.image_to_data(thresh, output_type=Output.DICT, config=custom_config)
    return data

def extract_text(text):
    llm = ChatGroq(
        temperature=0,
        groq_api_key='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',
        model_name="llama-3.1-70b-versatile"
    )
    prompt = f"""
    Given the following text, extract the relationship between glands and the hormones they secrete.
    Organize the output in proper JSON format with glands as keys and lists of hormones as values.

    The output should look like this:
    {{
        "Gland Name 1": ["Hormone A", "Hormone B"],
        "Gland Name 2": ["Hormone C", "Hormone D"]
    }}
    give only the output of script
    Text: {text}
    """
    response = llm.invoke(prompt)
    response_content = response.content

    # Parsing response as json (using error handling because it can also fail)
    try:
        formatted_response = json.loads(response_content)
        print("OUTPUT:-")
        print(json.dumps(formatted_response, indent=4))
        return formatted_response
    except json.JSONDecodeError:
        # If parsing fails
        print("OUTPUT:-")
        print(response_content)
        return response_content

def extract(path):
    ocr_data = preprocessing(path)
    organized_dict = extract_text(ocr_data)
    return organized_dict

path = "sample.jpeg"
output_dict = extract(path)