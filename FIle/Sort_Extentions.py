import os
import shutil
    
def sort_extentions():

    path = '/home/malware/Desktop/InFeCtEd/'


    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            
            if entry.endswith(('.doc' , '.docm' , '.docx' , '.dot' , '.dotm' , '.dotx' , '.xlm' , '.odt')):
                print("Word folder")
                shutil.move(path + entry, '/home/malware/Desktop/InFeCtEd/Word')
            elif entry.endswith(('.xlsx' , '.xls')):
                print("Excel")
                shutil.move(path + entry, '/home/malware/Desktop/InFeCtEd/Excel')
            elif entry.endswith('.pdf'):
                print("PDF")