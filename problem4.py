maximum = 0
for i in range(100,1000):
    for j in range(100,1000):
        result = i*j
        str_result = str(result)
        str_reverse = str_result[::-1]
        if(str_result == str_reverse):
            if(maximum<result):
                maximum = result
                print(i,j)
        
print(maximum)
