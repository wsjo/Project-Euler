primeCounter = 2 #2,3 is included 
number = 5
while True:
    isPrime = True
    for divider in range(2,number):
        if number % divider == 0:
            isPrime = False
            break
    number +=1
    if isPrime:
        primeCounter += 1
        print(primeCounter)
    if primeCounter == 10001:
        print(number-1)
        break
     
#solved this brute-force way
#need to reduce the amount of computation by doing it smarter.
#manually finding that way requires mathematical knowledge for sure.
