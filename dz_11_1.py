#number = int(input())
#test без ручного ввода
import random
from datetime import datetime
random.seed(datetime.now().timestamp())
number = random.randint(1, 7)



def factorial(x):
    fac = 1
    for n in range(1, x+1):
        fac = fac * n
    return fac

#print(f"факториал числа {number} равен {factorial(number)}")
list = []
for n in range(factorial(number),0,-1):
    list.append(factorial(n))
print(list)