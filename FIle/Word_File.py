from datetime import datetime
import os
import shutil




def Word_File():

    path = '/home/malware/Desktop/InFeCtEd/Word/'

    time = datetime.now()
    
    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            print(entry)
            os.mkdir(path + entry + " Report")
            os.chdir(path + entry + " Report")
            os.system("touch " + "Report.txt" )
            os.chdir(path)
            
            md5sum = os.system("md5sum '" + path + entry + "' >> '"+  path + entry + " Report/Report.txt'")
            file_check = os.system("file '" + path + entry + "' >> '"+  path + entry + " Report/Report.txt'")
            
            
            
            oleid = os.system("oleid '" + path + entry + "' >> '"+  path + entry + " Report/Report.txt'")
            #if oleid.find('file contains VBA macros'):
            olevba = os.system("olevba '" + path + entry + "' >> '"+  path + entry + " Report/Report.txt'")
                       
            
            shutil.move(path + entry, '/home/malware/Desktop/InFeCtEd/Word/' + entry+ " Report")