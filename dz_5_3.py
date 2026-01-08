X = input("Введите, сколько долларов нужно для инвестиций: ")
mike = input("Введите, сколько долларов есть у Майкла: ")
ivan = input("Введите, сколько долларов есть у Ивана: ")
#test для заданных заранее параметров
# X = 500
# mike = 100
# ivan = 700
def investment(X, mike, ivan):
    if mike >= X and ivan >= X:
        print("И у Майкла и у Ивана хватает денег на инвестиции")
        return 2
    elif mike >= X and ivan < X:
        print("Только у Майкла хватает денег на инвестиции")
        return "Mike"
    elif mike < X and ivan >= X:
        print("Только у Ивана хватает денег на инвестиции")
        return "Ivan"
    elif mike+ivan>=X:
        print("И у Майкла и у Ивана не хватает денег на инвестиции по-отдельности, но вместе они могут вложиться")
        return 1
    else:
        print("Ни у кого не хватает денег на ивестиции, кризис, Аднака")
        return 0

print(investment(X, mike, ivan))

#test
# print(investment(500, 600, 700))
# print(investment(500, 200, 700))
# print(investment(500, 600, 300))
# print(investment(500, 300, 200))
# print(investment(500, 100, 200))