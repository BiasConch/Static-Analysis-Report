import os

    
def unzip():

    path = '/home/malware/Desktop/InFeCtEd/'
    valid_entry = []

    """for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            #print(entry)
            valid_entry.append(entry)
    """
    for entry in os.listdir(path):
        if entry.endswith('.zip'):
            os.chdir(path)
            os.system("7za x -pinfected " + entry)
            valid_entry.append(entry)