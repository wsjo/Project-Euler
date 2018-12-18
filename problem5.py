import array as arr

primeCounter = arr.array('d',[0]*21)
maxCounter = arr.array('d',[0]*21)

for i in range(2,21):
    j = 2
    while j * j <= i:
        if i % j == 0:
            i = i/j
            primeCounter[j] += 1
            continue
        j += 1
    primeCounter[int(i)] += 1
    for i in range(21):
        if primeCounter[i] > maxCounter[i]:
            maxCounter[i] = primeCounter[i]
    primeCounter = arr.array('d',[0]*21)

result = 1

for i in range(21):
    print(maxCounter[i])
    if maxCounter[i] != 0:
        result = result * (i ** maxCounter[i])

print(result)

