import os
from string import digits

def rename_folders():
    #(1) finding file names in a directory
    file_list = os.listdir("/Users/Ania/Desktop/prank")
    #print(file_list)
    os.chdir("/Users/Ania/Desktop/prank")
    #(2) changing file names
    for file_name in file_list:
        os.rename(file_name, file_name.translate({ord(k): None for k in digits}))
rename_folders()
