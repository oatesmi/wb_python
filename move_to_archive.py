import os
import shutil
import datetime 
from pathlib import Path

provisioning = "/Users/morgan.oates/Desktop/provisioning/"
filepath = os.listdir(provisioning)

pythonf = "/Users/morgan.oates/Desktop/python/"
filepath_py = os.listdir(pythonf)

now = str(datetime.datetime.now())

if os.path.exists(provisioning):
    counter = 0
    while counter <= len(filepath):
        for files in filepath:
            files = provisioning + files
            counter += 1

            if ".xlsx" in files:
                newfile = Path(files).stem
                os.rename(files, newfile + "_" + now + ".xlsx")
                shutil.move(newfile + "_" + now + ".xlsx", provisioning + "archive")

if os.path.exists(pythonf):
    counter = 0
    while counter <= len(filepath_py):
        for files in filepath_py:
            files = pythonf + files
            counter += 1
            
            if ".xlsx" in files:
                newfile = Path(files).stem
                os.rename(files, newfile + "_" + now + ".xlsx")
                shutil.move(newfile + "_" + now + ".xlsx", pythonf + "archive")
