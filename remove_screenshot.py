import os

desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 
file = os.listdir(desktop)

if os.path.exists(desktop):
    for files in file:
        files = desktop + "/" + files
       
        if 'Screenshot' in files:
            os.remove(files)
        else:
            pass
