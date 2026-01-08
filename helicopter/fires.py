from emoji import Emoji, FIELD_GRASS, MOUNTAIN1, MOUNTAIN2, MOUNTAIN3, GOLF_FIELD, PINE, TREE, CHRISTMAS_TREE, PALM, RIVER, HOSPITAL, GARAGE, FIELD_FIRE, CLOUD, CLOUD_RAIN, CLOUD_LIGHTING, HELICOPTER, WATER_SCORE, DIAMOND_SCORE, LIFE_HEART, UNDER_CONSTRACTION, CONFLAGRATION, MOUNTAIN_START, MOUNTAIN_END, TREE_START, TREE_END, CLOUD_START, CLOUD_END
from utils import randbool, randcell, rnd
from settings import TICKS, WOOD_BURNING_TIME, FIRE_UPDATE, CLOUD_COVER_CHANCE, LIGHTING_CHANCE, FIRES_MIN, FIRES_MAX
from utils import pause

class Fire():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[0 for _ in range(width)] for _ in range(height)]
        self.ticks = TICKS

    def generate_new_fire(self, field, tick):
        new_fire_field = randcell(self.width, self.height)
        new_fire_fieldX = new_fire_field[0]
        new_fire_fieldY = new_fire_field[1]
        self.PosX = new_fire_fieldX
        self.PosY = new_fire_fieldY
        if field.cells[self.PosX][self.PosY] >= TREE_START and field.cells[self.PosX][self.PosY] <= TREE_END:
            self.cells[self.PosX][self.PosY] = 1
            self.ticks[str(new_fire_fieldX)+"-"+str(new_fire_fieldY)] = tick
        return (new_fire_fieldX, new_fire_fieldY)
            
    def update_fires(self, field, tick, field_cloud):
        tmp_list = []
        tmp_list = self.cells
        fields_arround = [(-1, 0), (-1, -1), (-1, 1), (0, 1), (1, 0), (1,-1), (0, -1), (1, 1)]
        for row in range(self.height):
            for column in range(self.width):
                # тушение пожара дождём
                if self.cells[row][column] == 1 and (field_cloud.cells[row][column] == 2 or field_cloud.cells[row][column] == 3):
                    if field.cells[row][column] == CONFLAGRATION:
                        field.cells[row][column] = FIELD_GRASS
                    self.cells[row][column] = 0
                    self.ticks[str(row)+"-"+str(column)] = 0
                # выжигание пепелища
                if self.cells[row][column] == 1 and self.ticks[str(row)+"-"+str(column)] != 0 and (tick - self.ticks[str(row)+"-"+str(column)]) >= WOOD_BURNING_TIME:
                    field.cells[row][column] = CONFLAGRATION
                    field.ticks[str(row)+"-"+str(column)] = tick
                    tmp_list[row][column] = 0
                    self.cells[row][column] = 0
                    self.ticks[str(row)+"-"+str(column)] = 0
                    # поджёг соседних деревьев
                    for i in range(8):
                        if self.checkXY(row+fields_arround[i][0], column+fields_arround[i][1]):
                            if field.cells[row+fields_arround[i][0]][column+fields_arround[i][1]] >= TREE_START and  field.cells[row+fields_arround[i][0]][column+fields_arround[i][1]] <= TREE_END:
                                if self.cells[row+fields_arround[i][0]][column+fields_arround[i][1]] != 1:
                                    tmp_list[row+fields_arround[i][0]][column+fields_arround[i][1]] = 1
                                    self.ticks[str(row+fields_arround[i][0])+"-"+str(column+fields_arround[i][1])] = tick
        for row in range(self.height):
            for column in range(self.width):
                if tmp_list[row][column] == 1:
                    self.cells[row][column] = 1
        # # генерация нескольих новых пожаров
        # for i in range(rnd(FIRES_MIN,FIRES_MAX)):
        #     self.generate_new_fire(field, tick)
        #     i += 1
    # проверка координат на предмет выхода за пределы области
    def checkXY(self, x, y):
        if (x < 0 or y < 0 or x >= self.height or y >= self.width):
            return False
        return True

    def export_data(self):
        return {'cells': self.cells, 'ticks': self.ticks}
    
    # def import_data(self, data):
    #     self.cells = data['cells'] or [[0 for _ in range(self.width)] for _ in range(self.height)]
    #     self.ticks = data['ticks'] or TICKS