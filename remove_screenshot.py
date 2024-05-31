import os

desktop = "/Users/morgan.oates/Desktop/"
file = os.listdir(desktop)

if os.path.exists(desktop):
    for files in file:
        files = desktop + files
       
        if 'Screenshot' in files:
            os.remove(files)
        else:
            pass
