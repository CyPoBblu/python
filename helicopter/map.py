global HELICOPTER
from emoji import Emoji, FIELD_GRASS, MOUNTAIN1, MOUNTAIN2, MOUNTAIN3, GOLF_FIELD, PINE, TREE, CHRISTMAS_TREE, PALM, RIVER, HOSPITAL, GARAGE, FIELD_FIRE, CLOUD, CLOUD_RAIN, CLOUD_LIGHTING, HELICOPTER, WATER_SCORE, DIAMOND_SCORE, LIFE_HEART, UNDER_CONSTRACTION, CONFLAGRATION, MOUNTAIN_START, MOUNTAIN_END, TREE_START, TREE_END, CLOUD_START, CLOUD_END, CLOUD_FIELD, CLOUD_RAIN_FIELD, CLOUD_LIGHTING_FIELD
# import utils
from utils import randbool, rnd, randcell
from fires import Fire
from clouds import Clouds
from settings import TICKS, GRASS_UPDATE, FOREST_CHANCE, MOUNTAIN_CHANCE, RIVERS_MIN, RIVERS_MAX, RIVERS_MIN_LENGTH, RIVERS_MAX_LENGTH
# from utils import neighbour
# from time import time
# import time



# 0 - пустая клетка
# 1-4 - горы
# 5-8 - деревья
# 9 - река
# 10 - госпиталь
# 11 - магазин
class Map(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[0 for i in range(width)] for j in range(height)]
        self.ticks = TICKS

        # генерация лесов
        self.generate_forest(FOREST_CHANCE)
        # генерация гор 
        self.generate_mountain(MOUNTAIN_CHANCE)
        # генерация рек
        global MAP_WIDTH, MAP_HEIGHT
        for i in range (rnd(RIVERS_MIN,RIVERS_MAX)):
            tmp_random = rnd(int(RIVERS_MIN_LENGTH), int(RIVERS_MAX_LENGTH))
            # print(f"длина реки {i} = {tmp_random}")
            self.generate_river(tmp_random)
            i += 1
        # генерация гаража
        self.generate_upgrade_shop()
        # генерация больницы
        self.generate_hospital()

    def printmap(self, field_fire, helicopt, field_cloud):
        print(Emoji.CELL_TYPES[UNDER_CONSTRACTION] * (self.width + 2)) # верхняя строка ограничителя поля
        for row in range(self.height):
            print(Emoji.CELL_TYPES[UNDER_CONSTRACTION], end = "") # левый ограничитель поля
            for column in range(self.width):
                cell = self.cells[row][column]
                # вертолёт
                if (helicopt.PosX == row and helicopt.PosY == column):
                    print(Emoji.CELL_TYPES[HELICOPTER], end = "")
                
                # облака
                elif (field_cloud.cells[row][column] == CLOUD_LIGHTING_FIELD):                    
                    print(Emoji.CELL_TYPES[CLOUD_LIGHTING], end = "") # грозовые облака
                elif (field_cloud.cells[row][column] == CLOUD_FIELD):
                    print(Emoji.CELL_TYPES[CLOUD], end = "") # облака
                elif (field_cloud.cells[row][column] == CLOUD_RAIN_FIELD):
                    print(Emoji.CELL_TYPES[CLOUD_RAIN], end = "")  # дождевые облака
                # пожар
                elif (field_fire.cells[row][column] == 1 and (self.cells[row][column] >= TREE_START and self.cells[row][column] <= TREE_END)):
                    print(Emoji.CELL_TYPES[FIELD_FIRE], end = "") # пожар
                elif cell >= 0 and cell <= len(Emoji.CELL_TYPES):
                    print(Emoji.CELL_TYPES[cell], end = "")
            print(Emoji.CELL_TYPES[UNDER_CONSTRACTION])  # правый ограничитель поля
        print(Emoji.CELL_TYPES[UNDER_CONSTRACTION] * (self.width + 2))  # нижняя строка ограничителя поля

    def generate_forest(self, percent):
        for forestX in range(self.height):
            for forestY in range(self.width):
                if randbool(percent):
                    self.cells[forestX][forestY] = rnd(TREE_START, TREE_END)

    def generate_new_trees(self, tick):
        new_tree_field = randcell(self.width, self.height)
        new_tree_fieldX = new_tree_field[0]
        new_tree_fieldY = new_tree_field[1]
        if (self.checkXY(new_tree_fieldX, new_tree_fieldY) and self.cells[new_tree_fieldX][new_tree_fieldY] == FIELD_GRASS):
            self.cells[new_tree_fieldX][new_tree_fieldY] = rnd(TREE_START, TREE_END)
        for row in range(self.height):
            for column in range(self.width):
                if self.cells[row][column] == CONFLAGRATION: # пожарище
                    if (tick - self.ticks[str(row)+"-"+str(column)]) >= GRASS_UPDATE:
                        self.cells[row][column] = FIELD_GRASS

    def generate_mountain(self, percent):
        for forestX in range(self.height):
            for forestY in range(self.width):
                if randbool(percent):
                    self.cells[forestX][forestY] = rnd(MOUNTAIN_START, MOUNTAIN_END)

    # генерация рек
    def generate_river(self, length):
        rc = randcell(self.width, self.height)
        rcX = rc[0]
        rcY = rc[1]
        # print(f"rcX = {rcX}, rxY = {rcY}")
        while self.cells[rcX][rcY] == RIVER:
            rc = randcell(self.width, self.height)
            rcX = rc[0]
            rcY = rc[1]
        self.cells[rcX][rcY] = RIVER
        # print(f"координаты первой точки реки {rcX},{rcY}")
        wow = 0

        while length > 0 and wow == 0:
            if self.nh_rivers(rcX, rcY):
                wow = 1
                break
            nh = self.neighbour(rcX, rcY)
            while (not self.checkXY(nh[0],nh[1])) or ((rcX == nh[0] and rcY == nh[1]) or self.cells[nh[0]][nh[1]] == RIVER):
                nh = self.neighbour(rcX, rcY)
                if self.nh_rivers(rcX, rcY):
                    wow = 1
                    break
            if self.nh_rivers(rcX, rcY):
                wow = 1
                break
            rcX2 = nh[0]
            rcY2 = nh[1]

            if (self.checkXY(rcX2,rcY2)):
                self.cells[rcX2][rcY2] = RIVER
                # field.printmap()
                rcX = rcX2
                rcY = rcY2
                length -= 1

    def generate_upgrade_shop(self):
        random_cell = randcell(self.width, self.height)
        rand_coordinate_x = random_cell[0]
        rand_coordinate_y = random_cell[1]
        if self.cells[rand_coordinate_x][rand_coordinate_y] == FIELD_GRASS:
            self.cells[rand_coordinate_x][rand_coordinate_y] = GARAGE
        else:
            self.generate_upgrade_shop()

    def generate_hospital(self):
        random_cell = randcell(self.width, self.height)
        rand_coordinate_x = random_cell[0]
        rand_coordinate_y = random_cell[1]
        if self.cells[rand_coordinate_x][rand_coordinate_y] == FIELD_GRASS:
            self.cells[rand_coordinate_x][rand_coordinate_y] = HOSPITAL
        else:
            self.generate_hospital()

    def checkXY(self, x, y):
        if (x < 0 or y < 0 or x >= self.height or y >= self.width):
            return False
        return True

    def neighbour(self, x, y):
        if self.checkXY (x, y):
            # moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            # field = rnd(0,3)
            moves = [(-1, 0), (-1, -1), (-1, 1), (0, 1), (1, 0), (1,-1), (0, -1), (1, 1)]

            field = rnd(0,len(moves)-1)
            dx = moves[field][0]
            dy = moves[field][1]
            while not self.checkXY (x + dx, y + dy):
                moves.pop(field)
                field = rnd(0,len(moves)-1)
                dx = moves[field][0]
                dy = moves[field][1]
            return (x + dx, y + dy)
        else:
            return (x, y)

    # проверка "соседей" для розлива реки - если нельзя, то обрубаем реку
    def nh_rivers(self, rcX, rcY):
        k = 0
        try:
            if self.cells[rcX+1][rcY] == RIVER:
                k += 1
        except IndexError:
            k += 1
        try:
            if self.cells[rcX+1][rcY+1] == RIVER:
                k += 1
        except IndexError:
            k += 1
        try:
            if self.cells[rcX][rcY+1] == RIVER:
                k += 1
        except IndexError:
            k += 1
        try:
            if self.cells[rcX-1][rcY+1] == RIVER or rcX-1:
                k += 1
        except IndexError:
            k += 1
        try:
            if self.cells[rcX-1][rcY] == RIVER or rcX-1 < 0:
                k += 1
        except IndexError:
            k += 1
        try:
            if self.cells[rcX-1][rcY-1] == RIVER or rcX-1< 0 or rcY-1 < 0:
                k += 1
        except IndexError:
            k += 1
        try:
            if self.cells[rcX][rcY-1] == RIVER or rcY-1 < 0:
                k += 1
        except IndexError:
            k += 1
        try:
            if self.cells[rcX+1][rcY-1]== RIVER or rcY-1 < 0:
                k += 1
        except IndexError:
            k += 1
        # print(f"k = {k}")
        if k == 8:
            return True

    def export_data(self):
        return {'cells': self.cells, 'ticks': self.ticks}
    
    # def import_data(self, data):
    #     self.cells = data['cells'] or [[0 for _ in range(self.width)] for _ in range(self.height)]
    #     self.ticks = data['ticks'] or TICKS

# TODO ввести вышки с проводами, над которыми пролетать нельзя, или небоскрёбы

