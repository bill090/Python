import os
if os.path.exists("/home/bill/Documents/Python/Python with AI - Level 2/fileHandling/files/demofile.txt"):
    os.remove("/home/bill/Documents/Python/Python with AI - Level 2/fileHandling/files/demofile.txt")
    print("The file has been deleted")
else:
    print("The file does not exist")