#задача 9.2
#превращаем полученный от пользователя список1 в множество
#plenty1 = set(map(int, input().split()))

#превращаем полученный от пользователя список2 в множество
#plenty2 = set(map(int, input().split()))





#============================================
#тест с рандомом без ввода пользователя
#============================================

import random
import time
from datetime import datetime

random.seed(datetime.now().timestamp())
number1 = random.randint(1, 100000)
#test print number1
#print(f"number1={number1}")
time.sleep(random.uniform(0.1, 0.6))
#time.sleep(0.3)
random.seed(datetime.now().timestamp())
number2 = random.randint(1, 100000) 
#test print number2
#print(f"number2={number2}")

plenty1 = set()
plenty2 = set()
#Генерируем первый список (множество)
for n in range(number1):
    plenty1.add(random.randint(1,100000))
print(plenty1)
#Генерируем второй список (множество)
for n in range(number2):
    plenty2.add(random.randint(1,100000))
print(plenty2)

#=======================================================
#окончание блока теста с рандомом без ввода пользователя
#=======================================================


# Находим пересечение множеств
peresechenie = plenty1.intersection(plenty2)
#print(peresechenie)
#test
print(f"\nКоличество введённых чисел в первом списке {number1}, из них уникальных {len(plenty1)}")
print(f"Количество введённых чисел во втором списке {number2}, из них уникальных {len(plenty2)}")
# Выводим количество общих элементов  
print(f"\nКоличество одинаковых элементов в строках: {len(peresechenie)}\n")








