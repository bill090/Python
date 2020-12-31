import os
print("List directory")
basepath = '..//'
directories = os.listdir(basepath)
for d in directories:
    print(d)