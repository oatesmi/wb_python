import os
import time 

downloads = "/Users/morgan.oates/Downloads/"
filepath_downloads = os.listdir(downloads)
now = time.time()

if os.path.exists(downloads):
    for files in filepath_downloads:   
        file_time = os.stat(downloads).st_mtime 
        if file_time < now - 1209600:
            os.remove(downloads + files)