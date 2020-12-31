def fibbonacciCheck(x):
    if x == 1 or x == 0:
        return True
    else:
        seq = 2
        seqPrev = 1
        while True:
            if x == seq:
                return True
            elif x > seq:
                seq += seqPrev
                seqPrev = seq - seqPrev
            else:
                return False
print(fibbonacciCheck(2))
print(fibbonacciCheck(5))
print(fibbonacciCheck(10))