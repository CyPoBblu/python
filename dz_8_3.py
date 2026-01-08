ribak = []
count = 0

#test
# lodka = 130
# ribak = [60, 48, 58, 59, 48, 90, 116, 105, 90, 75, 82]
# kolvo = len(ribak)

lodka = int(input("Введите максимальную массу m, перевозимую лодкой, где 1 ≤ m ≤ 10e6: "))
kolvo = int(input("Введите количество рыбаков n, где 1 ≤ n ≤ 100: "))
for i in range(kolvo):
    ribak.append(int(input(f"введите A{i} вес {i+1} рыбака, где 1 ≤ N ≤ {lodka}: ")))
    #TODO проверка на дурака на ввод kolvo За пределами допустимых значений
#print(ribak)

perevozchik = min(ribak)
#print(lodka-perevozchik)
for i in range(len(ribak)):
    if ribak[i] == perevozchik:
        ribak.pop(i)
        #print(ribak)
        count += 1 # самый мелкий перевозит всех, кого может, на одной лодке туда-сюда
        break

for i in range(len(ribak)):
    if ribak[i] + perevozchik > lodka:
        count += 1 # "толстяки" сами себя перевозят каждый на своей лодке

print(f"Минимальное необходимое число лодок для перевозки всех рыбаков с одного берега на другой равно {count}")
























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
lodka = 130
ribak = [60, 48, 58, 59, 90, 116, 105, 90, 75]
#print(f"Введите в строку через пробел {n} натуральных чисел Ai, где 1 ≤ Ai ≤ 10e9:")
#spisok = input().split()
#TODO проверка на дурака на ввод (меньше ввели чисел - добиваем нулями, больше - обрезаем, не числа - прерываем)


#reversef(ribak)

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




