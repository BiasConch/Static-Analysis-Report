import os
import shutil

def Word_File():

    path = '/home/malware/Desktop/InFeCtEd/Word/'


    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            os.mkdir(path + entry)
            os.system("touch " + entry + ".txt" )
            os.chdir(path)
            md5sum = os.system("md5sum " + entry)
            file_check = os.system("file " + entry)
            oleid = os.system("oleid " + entry)
            
            if (oleid.find('file contains VBA macros') != -1):
                olevba = os.system("olevba " + entry)
            
            
            shutil.move(path + entry, '/home/malware/Desktop/InFeCtEd/Word/' + entry)