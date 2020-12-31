import os
basepath = '..//'
entries = os.scandir(basepath)
max_file = ""
max_size = 0
print("List all files:")
for entry in entries:
    if entry.is_file():
        info = entry.stat()
        print((f'{entry.name} {info.st_size}'))
        if max_size < info.st_size:
            max_size = info.st_size
            max_file = entry.name
print(f"The largest file in {os.path.abspath(basepath)} is {max_file}, with a size of {max_size}")