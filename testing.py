import os

def get_directory_structure(rootdir):
    """
    Creates a nested dictionary that represents the folder structure of rootdir
    """
    dir = {}
    rootdir = rootdir.rstrip(os.sep)
    start = rootdir.rfind(os.sep) + 1
    for path, dirs, files in os.walk(rootdir):
        folders = path[start:].split(os.sep)
        subdir = dict.fromkeys(files)
        parent = reduce(dict.get, folders[:-1], dir)
        parent[folders[-1]] = subdir
    return dir

for i in range(0, modlistsize):
        if not os.path.exists(servermodpath_list[i]):
                os.system( 'mklink /J '  + servermodpath_list[i] + ' ' + steammod_list[i] ) 
                print(steammod_list[i] + ' ' + servermodpath_list[i] )
# makes Junctions on a loop checks if they were already made
# need to check if there are extra junctions that the user did not select
# need to ignore spaces in the path 

from tkinter import Tk
from tkinter import filedialog
import os

root = Tk()
root.withdraw()

current_directory = filedialog.askdirectory()
file_name = "test.txt"

file_path = os.path.join(current_directory,file_name)
print(file_path)
# use the os.path.join method to join paths rather than a simple + string concatenation. This way the code will work on multiple platforms (Windows/Mac/Linux)
# For example
listbox = Listbox(frame)
for name in files(dir):
    listbox.insert('end', name)