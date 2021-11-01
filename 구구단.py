for x in range(1,19):
    for y in range(1, 10):
        print(x, "x", y, "=", x*y)

i = 2
while(i<=18):
    j = 1
    while(j < 10):
        print("{} * {} = {}".format(i, j, i*j))
        j += 1
    i += 1 

for i in range(1, 19):
    for j in range(1, 10): 
        print(i, "X", j, "=", i * j) 
        if(j == 9): 
            print()