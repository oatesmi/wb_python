import os
import shutil
import datetime 
from pathlib import Path

pythonf = "/Users/morgan.oates/Desktop/python/"
filepath_py = os.listdir(pythonf)
now = str(datetime.datetime.now())

if os.path.exists(pythonf):
    for files in filepath_py:
        files = pythonf + files
       
        if ".xlsx" in files:
            newfile = Path(files).stem
            os.rename(files, newfile + "_" + now + ".xlsx")
            shutil.move(newfile + "_" + now + ".xlsx", pythonf + "archive")