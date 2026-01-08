import os
os.system("cls")

print("\033[H\033[J", end="")

#=====================================================================================================================================
#функция rand - для автоматической генерации данных по животным
#=====================================================================================================================================
import random
import time
from datetime import datetime
def rand():    
    time.sleep(random.uniform(0.001, 0.006))
    random.seed(datetime.now().timestamp())
    number = random.randint(-50, 50) #TODO можно запрашивать у пользователя степень разнообразия чисел матриц
    return(number)

#=====================================================================================================================================
#функция generate - для автоматической генерации матрицы размером m [строк] на n [столбцов]
#=====================================================================================================================================
def generate(m,n):
    matrix = []
    for i in range(m):
        matrix.append([])
        for j in range(n):
            matrix[i].append(rand())
    return(matrix)


#=====================================================================================================================================
#функция print_matrix - для автоматической генерации матрицы размером m на n
#=====================================================================================================================================
import pprint  
def print_matrix_pretty(matrix):  
    # Использовать pprint для печати матрицы  
    pprint.pprint(matrix)  

def pl(matrix):
    for o in matrix:
        for p in o:
            print(f"{p}\t", end="")
            # print(f"\t{p}", end="")
        print()

def pl2(matrix):
    row = len(matrix)
    column = len(matrix[0])
    for i in range(0, row, 1):
        for j in range(0, column, 1):
            print(f"{matrix[i][j]} {"\t"}", end="")
        print()
        print("")


        
strok = 10
stolb = 10
matrix_1 = generate(strok,stolb)
print(f"матрица 1 сгенерирована:")
print_matrix_pretty(matrix_1)
# pl(matrix_1)
# pl2(matrix_1)
matrix_2 = generate(strok,stolb)
print(f"матрица 2 сгенерирована:")
# print_matrix_pretty(matrix_2)
pl(matrix_2)
# pl2(matrix_2)

#TODO если матрицы задаются вводом - ввести проверку на совпадение размеров матриц для сложения

addition = []
for i in range(len(matrix_1)):    
    addition.append([])
    for j in range(len(matrix_1)): 
        # add = matrix_1[i][j] + matrix_2[i][j]
        # addition[i].append(add)
        addition[i].append(matrix_1[i][j] + matrix_2[i][j])

print(f"сумма матрицы 1 и матрицы 2:")
# print_matrix_pretty(addition)
# pl(addition)
pl2(addition)