import os
import sys

from scripts.pdfToMp3 import convertToMP3
from scripts.yaml2json import convertYAMLtoJSON


def menu(script,*args):
    if script == "pdfmp3":
        convertToMP3(args)
    if script == "yamltojson":
        convertYAMLtoJSON(args)


try:
    if not os.path.exists("./output"):
        os.makedirs("./output")
    script = sys.argv[1]
    menu(script,sys.argv[2:][0])

except(IndexError):
    print('''> py main.py [script] path
    Available scripts: pdfmp3,yamltojson''')
    raise Exception("Enter a valid arguments")