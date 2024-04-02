import time 
starttime = time.time()

#outer loop
for i in range(10):
    #inner loop
    for j in range(10):
        print('me', end= " ")
    print()

print(round((time.time() - starttime), 2))