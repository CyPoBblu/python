# Создайте класс Черепашка, который хранит позиции x и y черепашки, а также s - количество клеточек, на которое она перемещается за ход
# у этого класс есть методы:
# ●	go_up() - увеличивает y на s
# ●	go_down() - уменьшает y на s
# ●	go_left() - уменьшает x на s
# ●	go_right() - увеличивает y на s
# ●	evolve() - увеличивает s на 1
# ●	degrade() - уменьшает s на 1 или выкидывает ошибку, когда s может стать ≤ 0
# ●	count_moves(x2, y2) - возвращает минимальное количество действий, за которое черепашка сможет добраться до x2 y2 от текущей позиции

import sys


# import sys
sys.setrecursionlimit(5000)
plenty_check = set()
dict_ways = {}
count_moves = 0

def minway (way, speed):
    count = 0
    global the_way
    global count_moves
    global plenty_check
    global dict_ways
    if (str(way)+"-"+str(speed)) in plenty_check: #прерываем зацикливание одних и тех же путей(loop'ы)
        if (str(way)+"-"+str(speed)) not in dict_ways.keys():
            count += the_way
        else:
            count = dict_ways[str(way)+"-"+str(speed)]
        return count
    else:
        if str(way)+"-"+str(speed) not in plenty_check:
            plenty_check.add(str(way)+"-"+str(speed))
        if way < 0 or speed <= 0:
            count = the_way
            return count
            # return 0
        elif way == 0:
            return 0
        elif way == speed:
            count = 1
            if str(way)+"-"+str(speed) not in dict_ways.keys():
                dict_ways[str(way)+"-"+str(speed)] = 0
            dict_ways[str(way)+"-"+str(speed)] += 1
            if str(way)+"-"+str(speed) not in plenty_check:
                plenty_check.add(str(way)+"-"+str(speed))
            return count
        elif speed > way:
            count = (speed - way) + 1
            if str(way)+"-"+str(speed) not in dict_ways.keys():
                dict_ways[str(way)+"-"+str(speed)] = 0
            dict_ways[str(way)+"-"+str(speed)] += count
            if str(way)+"-"+str(speed) not in plenty_check:
                plenty_check.add(str(way)+"-"+str(speed))
            return count
        elif speed < way:
            a = minway (way-speed, speed)
            b = minway (way, speed + 1)
            c = minway (way, speed - 1)
            count = min(a, b, c) + 1
            count_moves += min(a, b, c) + 1
            if str(way)+"-"+str(speed) not in dict_ways.keys():
                dict_ways[str(way)+"-"+str(speed)] = 0
            dict_ways[str(way)+"-"+str(speed)] += count
            if str(way)+"-"+str(speed) not in plenty_check:
                plenty_check.add(str(way)+"-"+str(speed))
            return count

class Черепашка(object):  # хранит позиции x и y черепашки, а также s - количество клеточек, на которое она перемещается за ход [её скорость]
    positionX = 0
    positionY = 0
    speed = 0

    def __init__(self, x, y, s):
        self.positionX = x
        self.positionY = y
        self.speed = s

    def go_up(self): # ●	go_up() - увеличивает y на s
        self.positionY += self.speed
        self.position()
    
    def go_down(self): # ●	go_down() - уменьшает y на s
        self.positionY -= self.speed
        self.position()

    def go_left(self): # ●	go_left() - уменьшает x на s
        self.positionX -= self.speed
        self.position()
    
    def go_right(self): # ●	go_right() - увеличивает y на s
        self.positionX += self.speed
        self.position()

    def evolve(self): # ●	evolve() - увеличивает s на 1
        self.speed += 1
        self.position()

    def degrade(self): # ●	degrade() - уменьшает s на 1 или выкидывает ошибку, когда s может стать ≤ 0
        if self.speed <= 1: #или if self.speed - 1 <= 0
            # return (print(f"Ошибка! s [скорость черепахи] не может быть меньше либо равна нулю, оставляем 1"))
            sys.exit("Скорость не может быть равна 0 или меньше!!!")
        self.speed -= 1
        self.position()
    
    def count_moves(self, x2, y2): # ●	count_moves(x2, y2) - возвращает минимальное количество действий, за которое черепашка сможет добраться до x2 y2 от текущей позиции
        if self.positionX == x2 and self.positionY == y2:
            return print(f"Черепаха уже находится в необходимой позиции, действий не требуется [минимальное количество действий = 0]")
        else:
            wayX = minway (modul(self.positionX, x2), self.speed)
            print(f"Черепаха пройдёт путь по оси X за {wayX} ходов")
            # wayY = minway (modul(self.positionY, y2), self.speed)
            # print(f"Черепаха пройдёт путь по оси X за {wayY} ходов")
            wayY = minway (modul(self.positionY, y2), 1) + 1
            print(f"Черепаха пройдёт путь по оси Y за {wayY} ходов")
            print(f"общее количество ходов черепахи до места назначения составит: {wayX+wayY}")
    
    #добавим функцию вывода позиции черепашки
    def position(self):
        print (f"координаты черепашки: ({self.positionX}, {self.positionY}), скорость {self.speed}")


#=====================================================================================================================================
#либо импорт библиотеки math и использование abs, либо пишем своё
#=====================================================================================================================================
def modul(x1, x2):
    if x1 > x2:
        if x1 <= 0:
            return (-1 * x2) - (-1 * x1)
        else:
            if x2 <= 0:
                return x1 + (-1 * x2)
            else:
                return x1 - x2
    elif x1 < x2:
        if x2 <= 0:
            return (-1 * x1) - (-1 * x2)
        else:
            if x1 <= 0:
                return x2 + (-1 * x1)
            else:
                return x2 - x1
    else:
        return 0
#=====================================================================================================================================
#=====================================================================================================================================




import random
#зададим рандомно положение черепашки на декартовых координатах (ограничения возьмём 500) и ограниение скорости до 1/20 поля [можно другие ограничениея]
posX = 50
posY = 50
the_way = 2 * max(posX, posY)
#на случай задания маленького поля
if (int(the_way/20) == 0):
    # print(f"{int(the_way/20)} = 0")
    startspeed = 1
else:
    startspeed = int(the_way/20)
    # print(int(the_way/20))
черепашка1 = Черепашка(random.randint(-posX, posX), random.randint(-posY, posY), random.randint(1, startspeed))
#выведем координаты
черепашка1.position()
#зададим координаты точки назначения (суммой )
destinationX = random.randint(-posX, posX)
destinationY = random.randint(-posY, posY)
print(f"Точка назначения черепашки ({destinationX}, {destinationY})")
#посчитаем сколько ходов надо для достижения точки
черепашка1.count_moves(destinationX, destinationY)

#TODO проблема - при достижении конечной точки при минимальном количестве ходов по прямой- скорость будет равна 0
