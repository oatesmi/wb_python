import os
import shutil
import datetime 
from pathlib import Path

provisioning = "/Users/morgan.oates/Desktop/provisioning/"
filepath = os.listdir(provisioning)
now = str(datetime.datetime.now())

if os.path.exists(filepath):
    for files in filepath:
        files = filepath + files
       
        if ".xlsx" in files:
            newfile = Path(files).stem
            os.rename(files, newfile + "_" + now + ".xlsx")
            shutil.move(newfile + "_" + now + ".xlsx", filepath + "archive")