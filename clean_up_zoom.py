import os
import time 

zoom = "/Users/morgan.oates/Documents/Zoom/"
filepath_zoom = os.listdir(zoom)
now = time.time()

if os.path.exists(zoom):
    for files in filepath_zoom:   
        file_time = os.stat(zoom).st_mtime 
        if file_time < now - 1209600:
            os.remove(zoom + files)