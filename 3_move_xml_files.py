import glob
import os
import ntpath
import shutil

# os.rename("/home/naz/Desktop/Untitled Document","/home/naz/Desktop/Untitled Document2")

for name in glob.glob('/home/naz/Desktop/avto_6500/Annotations/*/*'):

    shutil.copy(name, '/home/naz/Desktop/avto_6500/all_xml')
    print name
