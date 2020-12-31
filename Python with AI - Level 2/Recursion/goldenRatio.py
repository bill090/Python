fibbonaciSeq = []
for n in range(50):
    if n == 0:
        f = 0
    elif n == 1:
        f = 1
    else:
        f = fibbonaciSeq[n - 1] + fibbonaciSeq[n-2]
    fibbonaciSeq.append(f)
print(fibbonaciSeq)
for j in range(2, len(fibbonaciSeq)):
    print(fibbonaciSeq[j] / fibbonaciSeq[j - 1])
    