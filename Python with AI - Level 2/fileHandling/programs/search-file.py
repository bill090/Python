import os
file_to_search = "datainparent.txt"
dir_to_search = "..//"
for dirpath, dirnames, files in os.walk(dir_to_search):
    print(f'\nFound directory: {dirpath}')
    for file_name in files:
        if file_name == file_to_search:
            print(file_name, "is in", os.path.abspath(dirpath))
            quit()
    print("Not Found")