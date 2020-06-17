# Hand_writing_recognition
Code uses tesseract library for OCR. 

Packages:
More information can be found https://github.com/tesseract-ocr/
Tesseract-OCR package for Windows is installed.
pytesseract is installed through pip install.


Source code:
pytesseract and cv2 packages are imported.
pytesseract.pytesseract.tesseract_cmd is set to installed tesseract.exe path.
Image is read and converted to gray scale.
Noise is cleared out before using tesseract library function.
Image content is output in string format.
