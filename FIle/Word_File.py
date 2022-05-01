def Excel_File():

    path = '/home/malware/Desktop/InFeCtEd/Excel'


    for entry in os.listdir(path):
        os.chdir(path)
        md5sum = os.system("md5sum" + entry)
        file_check = os.system("file" + entry)
        oleid = os.system("oleid" + entry)
        if (oleid.find('file contains VBA macros') != -1):
            olevba = os.system("olevba" + entry)