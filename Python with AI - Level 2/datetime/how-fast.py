import datetime
max_i = 1000
max_j = 5000
start = datetime.datetime.now()
for i in range(max_i):
    for j in range(max_j):
        a = i * j
end = datetime.datetime.now()
duration = end - start
print(f"Your computer took {duration} seconds to do {max_i * max_j} times of multiplication")