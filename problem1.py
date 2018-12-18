sum = 0

for i in range(1000):
    if i%3 == 0:
        sum += i
    elif i%5 == 0:
        sum += i

print(sum)

##where i made mistake
#i thought that mod 3 and mod 5 at the same time will be duplicate, but
#the key was to make sure that they get added once and moved on to the next level.
