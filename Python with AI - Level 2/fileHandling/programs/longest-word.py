def longest_word(filename):
    infile = open(filename, "r")
    words = infile.read().split()
    word = max(words, key = len)
    infile.close()
    return word
print("The longest word in /home/bill/Documents/Python/Python with AI - Level 2/fileHandling/files/demofile.txt is", longest_word("/home/bill/Documents/Python/Python with AI - Level 2/fileHandling/files/demofile.txt"))