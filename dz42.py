print("Введите пятизначное число")
#string = str(46275)
string = input()
#print(string)
if len(string) > 5:
    print("введено более пяти символов, смотрите условие задачи")
elif len(string) < 5:
    print("введено менее пяти символов, смотрите условие задачи")
else:
    if str.isdigit(string):
        numberone = int(string[0])
        if numberone == 0:
            print("Введённое число равно начинается с 0, то есть не является пятизначным числом, смотрите условие задачи")
        elif numberone != 0:
            numberone = int(string[0])
            numbertwo = int(string[1])
            if numberone == numbertwo:
                print("Введённое число корректно, но действие программы при делении на разность 1 и 2 цифры, равной нулю, не описаны в ТЗ преподавателя")
            else:
                #print(((float(string[3])**float(string[4]))*float(string[2]))/(float(string[0])-float(string[1])))
                print(((float(string[3]) ** float(string[4])) * float(string[2])) / (float(string[0]) - float(string[1])))
            
