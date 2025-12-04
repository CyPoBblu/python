print("Введите целое число")
#string = str(46275)
string = input()
#print(string)
zero = 0
#
#   Проверка на дурака
#
if len(string) == 0:
    print ("Введённо пустое значение, смотрите условие задачи")
    exit()
    #number = 0
elif len(string) == 1:
    
    if str.isdigit(string):
        number = 1
        if string == "0":
            zero = 1
        else:
            zero = 0
    else:

        number = 0
elif string[0] == "-":
    string2 = string[1::]
    #TODO удалить печать строки
    #print(string2)
    if str.isdigit(string2):
        znak = "Отрицательное"
        number = 1
    else:
        number = 0
else:
    if str.isdigit(string):
        number = 1
        znak = "Положительное"
    else:
        number = 0
#
#   основной алгоритм программы на основе проверки дурака
#
if zero == 1:
    print("нулевое число")
elif number == 1:
    a = int(string)
    if a % 2 == 0:
        even = "чётное"
        print(f'{znak} {even} число')
    else:
        even = "нечётное"
        print(f"{znak} {even} число")
        print("Число не является чётным") #зачем это дополнительное сообщение в условиях задачи - хз
else:
    print ("Введённое значение не является целым числом, смотрите условие задачи")