import os
import pathlib
import shutil


def before():
    if os.path.exists("./output"):
        path = pathlib.Path('./output')
        shutil.rmtree(path)

def test_mp3():
    before()
    assert os.path.exists("./output/dummy.mp3") == False
    os.system("py main.py pdfmp3 static/dummy.pdf")
    assert os.path.exists("./output/dummy.mp3") == True
def test_yaml():
    before()
    assert os.path.exists("./output/config.json") == False
    os.system("py main.py yamltojson static/config.yml")
    assert os.path.exists("./output/config.json") == True
