i = 2
n = 461335

while i*i <= n:
    if n % i == 0:
        n = n / i
        print(i)
        continue
    i += 1

print(n)

##solving for this
#1 is totally going to work, and does not really count.
#starting from 2, you check if that number timed does not go over the n,
#since it is futile to check having not a prime factor to be 
#solved, and adjusted the code a bit so that it is more general
#change in file
