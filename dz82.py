n = int(input("Введите количество задаваемых натуральных чисел n массива, где 1 ≤ n ≤ 100 000: "))
#TODO проверка на дурака на ввод n За пределами допустимых значений
spisok = []

def reversef(list):
    length = int(len(list))
    if length % 2 == 0:
        k = int(length/2)
        for i in range(0,k):
            a = list[i]
            list[i] = list[0-i-1]
            list[0-i-1] = a
        print(list)
    else:
        k = int((length-1)/2)
        for i in range(0,k):
            a = list[i]
            list[i] = list[0-i-1]
            list[0-i-1] = a
        print(list)
    return(length)



#тест
#n = 10
#spisok = [6, -1, 0, 5, -7, 0, 1, 2, 0]
print(f"Введите в строку через пробел {n} натуральных чисел Ai, где 1 ≤ Ai ≤ 10e9:")
spisok = input().split()
#TODO проверка на дурака на ввод (меньше ввели чисел - добиваем нулями, больше - обрезаем, не числа - прерываем)


reversef(spisok)

# reverse
# for i in range(n):
#     print()
#     #spisok = int(input().split())
#     # spisok.append(int(input().split()))
# print("Изначальный массив:")
# print(spisok)
# spisok.reverse()

# print("Перевёрнутый массив:")
# print(spisok)




