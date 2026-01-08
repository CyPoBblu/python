#задача 9.2
#превращаем полученный от пользователя список1 в множество
#spisok1 = set(map(int, input().split()))

#превращаем полученный от пользователя список2 в множество
#spisok2 = set(map(int, input().split()))





#============================================
#тест с рандомом без ввода пользователя
#============================================

import random
from datetime import datetime

random.seed(datetime.now().timestamp())
number1 = random.randint(1, 100)
#test print number1
#print(f"number1={number1}")

def yn(a,b,c):
    #print(f"len(a)={len(a)}")
    if b == 0:
        return "NO"
    else:
        for k in range(0,b):
            #print(f"k={k}")
            if b-1 >= 0 and a[k] == a[b]:
                return "YES"
        return "NO"

spisok1 = []
#print(spisok1)
spisok2 = []
#Генерируем первый список
for n in range(number1):
    spisok1.append(random.randint(1,50))
#test ручной
#spisok1 = [12, 15, 15, 10, 31, 12]
print(spisok1)
#Генерируем второй список (множество)
for n in range(len(spisok1)):
    #yn(spisok1,n)
    #print(f"\nn={n}")
    #print(f"len(spisok1)={len(spisok1)}")
    spisok2.append(yn(spisok1,n,len(spisok1)-1))
print(spisok2)

#=======================================================
#окончание блока теста с рандомом без ввода пользователя
#=======================================================


# Находим пересечение множеств
#peresechenie = spisok1.intersection(spisok2)
#print(peresechenie)
#test
#print(f"\nКоличество введённых чисел в первом списке {number1}, из них уникальных {len(spisok1)}")
#print(f"Количество введённых чисел во втором списке {number2}, из них уникальных {len(spisok2)}")
# Выводим количество общих элементов  
#print(f"\nКоличество одинаковых элементов в строках: {len(peresechenie)}\n")








