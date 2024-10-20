**Overview**

I have performed Optical Character Recognition (OCR) on an input image followed by the use of a Large Language Model (LLM) to process the extracted text and identify relationships between glands and the hormones they secrete. The entire process leverages Tesseract for OCR, OpenCV for image preprocessing, and ChatGroq for natural language processing.

**Structure**

|-- README.md 

|-- sample.jpeg        # Example input image

|-- MyReadme.md  # My readme file

|-- Anshu Saini_ai-ml-task.py # Main script for the extraction process

|-- demonstartion.mp4 #video demonstarting the output

**Features**

1.) **Image Preprocessing:** The input image undergoes grayscale conversion and thresholding for better OCR results.

2.)**Optical Character Recognition (OCR):** Tesseract extracts textual data from the preprocessed image.

3.)**Text Parsing and Extraction:** The text extracted is passed to an LLM (ChatGroq) to identify glands and their corresponding hormones.

4.)**JSON Output:** The relationships between glands and hormones are organized and outputted in a structured JSON format.

**Technologies**

1.)**OpenCV:** Used for reading and preprocessing the input image.
2.)**Tesseract:** Optical Character Recognition (OCR) engine for extracting text from the image.
3.)**ChatGroq:** A powerful LLM-based API used for parsing the extracted text and identifying relevant gland-hormone relationships.
4.)**Python 3.x:** The language used for development.

**Installation Prerequisites**

1.)Python 3.x
2.)OpenCV
3.)Tesseract OCR
4.)ChatGroq API access

**Install Dependencies**

1.) Clone the repository:-  
use the commands:-  
git clone https://github.com/username/ai-ml-task.git

cd ai-ml-task

2.) Install required python libraries:-
pip install opencv-python pytesseract langchain_groq

3.) Install Tesseract:-
for windows download from the official [Tesseract Website](https://github.com/tesseract-ocr/tesseract)

4.) Add the Tesseract executable path to your Python script (Windows only):
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

**Usage**

1.)Place the input image (sample.jpeg) in the root directory.
2.)Modify the path variable in the script to point to your image.
3.)Run the script
4.)The output will be displayed in the JSON format.

**Example Output**

{
    "Hypothalamus": ["TRH", "CRH", "GHRH","Dopamine"],
    "Pineal gland": ["Melatonin"]
}