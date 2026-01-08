from utils import randbool

from settings import CLOUD_COVER_CHANCE, LIGHTING_CHANCE
from emoji import CLOUD_FIELD, CLOUD_RAIN_FIELD, CLOUD_LIGHTING_FIELD

class Clouds():
    def __init__(self, width, height):
        # print("бах-бах, зашли")
        self.width = width
        self.height = height
        self.cells = [[0 for j in range(width)] for i in range(height)]
        # 0 - нет облаков
        # 1 - облако
        # 2 - тучи с дождями [тушат огонь]
        # 3 - тучи с грозами [тушат огонь, повреждают вертолёт]

    def update_clouds(self):
        # print("бах, зашли")
        for row_index in range(self.height):
            for cell_index in range(self.width):
                if randbool(CLOUD_COVER_CHANCE):
                    if randbool(50):
                        self.cells[row_index][cell_index] = CLOUD_FIELD
                    else:
                        self.cells[row_index][cell_index] = CLOUD_RAIN_FIELD
                elif randbool(LIGHTING_CHANCE):
                        self.cells[row_index][cell_index] = CLOUD_LIGHTING_FIELD
                else:
                    self.cells[row_index][cell_index] = 0
                    
#TODO ввести ветер с движением уже существующих облаков, раномно изменяя направление, можно ещё мешать вертолёту, свдигая его

    def export_data(self):
        return {
            'cells': self.cells,
        }

    # def import_date(self, data):
    #     self.cells = data['cells'] or [[0 for _ in range(self.width)] for _ in range(self.height)]
