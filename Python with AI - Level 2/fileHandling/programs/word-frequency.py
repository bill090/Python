from collections import Counter
def word_count(fname):
    f = open(fname)
    return Counter(f.read().split())
print("Number of words in the file /home/bill/Documents/Python/Python with AI - Level 2/fileHandling/files/demofile.txt:", word_count("/home/bill/Documents/Python/Python with AI - Level 2/fileHandling/files/demofile.txt"))