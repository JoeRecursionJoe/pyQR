from img2table.document import PDF
from img2table.ocr import TesseractOCR
import pytesseract

#from img2table.document import Image
# Instantiation of the image
#img = Image(src=r"C:\Data\sheet2.jpg")
# Table identification
#img_tables = img.extract_tables()
# Result of table identification
#img_tables


pytesseract.pytesseract.tesseract_cmd = r'"C:\Program Files\Tesseract-OCR\tesseract.exe"'


# Instantiation of the pdf
pdf = PDF(src=r'C:\data\PRCAFB33.pdf')

# Instantiation of the OCR, Tesseract, which requires prior installation
# ocr = TesseractOCR(lang="eng")
ocr = TesseractOCR(lang="deu")


# Table identification and extraction
pdf_tables = pdf.extract_tables(ocr=ocr, min_confidence=1)

# We can also create an excel file with the tables
pdf.to_xlsx('C:\Data\PRCAFB33.xlsx', ocr=ocr)

