import os
from datetime import datetime
from datetime import time
from datetime import timedelta
def convertDate(timestamp):
    return datetime(1970, 1, 1) + timedelta(seconds = timestamp)
oldestFile = ""
oldestTime = datetime.now().timestamp()
basepath = "."
entries = os.scandir(basepath)
for entry in entries:
    if entry.is_file():
        info = entry.stat()
        print(f"{entry.name} {info.st_mtime}")
        if info.st_mtime < oldestTime:
            oldest_time = info.st_mtime
            oldest_file = entry.name
print(f"The oldest file under {os.path.abspath(basepath)} is {oldest_file} {convertDate(oldest_time)}")