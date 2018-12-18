#4,000,000 not exceed -> includes 4m.
import time
prev = 1
temp = 0
current = 1
total = 0
while current<4000000:
    temp = current
    current += prev
    prev = temp
    if current%2 == 0:
        total += current

print(total)
  
#tips for solving this question
#you need to store prev value somewhere, and i used temp to put current which will be prev of next one here.
#after storing temp, you add current with prev and then put prev the current value, which will be prev value for next.
#a step by step value inputting method will help you to gain more understandings.
