# __Author__ __Lencof__
# load.py

import requests

def save_file_from_www(link):
    filename = link.split('/')[-1]
    r = requests.get(link, allow_redirects=True)
    open(filename, 'wb').write(r.content)

link = 'https://raw.githubusercontent.com/Lencof/Shutdown-Python/main/Shutdown.py' # file directory

save_file_from_www(link)

import runpy
runpy.run_module(mod_name="Shutdown.py") 
