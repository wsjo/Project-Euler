eachSquared = 0
addAndSquared = 0
for i in range(1,101):
    eachSquared += i*i

for i in range(1,101):
    addAndSquared += i

addAndSquared *= addAndSquared 

print(addAndSquared-eachSquared)


