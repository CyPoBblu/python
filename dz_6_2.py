def divider(N):
    count = 0
    for i in range(1, N+1):
        if N % i == 0:
            count += 1

    #print(count)
    return count

X = int(input("Введите натуральное число [<=2 млрд], делители которого нужно найти: "))
#TODO проверка на ввод именно числа
#X = 40
if X > 2e9:
    print("введённое число больше 2 миллиардов, прочитайте условие задачи")
    exit()


print(divider(X))

#проверка
# for k in range(1,100+1):
#     print(f"Количество делителей числа {k} - {divider(k)} {"- это простое число" if divider(k) == 2 else ""}")