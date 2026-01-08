n = int(input("Введите количество задаваемых натуральных чисел N массива: "))
#TODO проверка на дурака на ввод
spisok = []

#тест
#n = 10
#spisok = [6, -1, 0, 5, -7, 0, 1, 2, 0, 4]
for i in range(n):
    spisok.append(int(input(f"введите {i+1} натуральное число N, где 1 ≤ N ≤ 10000: ")))
    #TODO проверка на дурака на ввод
print("Изначальный массив:")
print(spisok)
spisok.reverse()

print("Перевёрнутый массив:")
print(spisok)


