import os
from pathlib import Path

import PyPDF3
import pyttsx3
import pdfplumber

def convertToMP3(path):


        file_path = Path(''.join(path))
        with open(file_path, 'rb') as file:
            pages = PyPDF3.PdfFileReader(file).numPages
            finalText = ""
            with pdfplumber.open(file) as pdf:
                for i in range(pages):
                    page = pdf.pages[i]
                    text = page.extract_text()
                    finalText += text
            engine = pyttsx3.init()
            test = file.name
            engine.save_to_file(finalText, f"./output/{file_path.stem}.mp3")
            engine.runAndWait()
            print("Done!")

