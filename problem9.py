b = 2
c = 997

while True:
    for b in range(2,1000-c+1):
        print(c)
        for a in range(1,1000-c-b+1):
            da = a**2
            db = b**2
            dc = c**2
            if da+db == dc and a + b + c == 1000:
                print('found pythagorean triplet')
                print(a,b,c)
                print(a*b*c)
                exit()
    c -= 1
