from utils import randcell, rnd
from emoji import Emoji, FIELD_GRASS, MOUNTAIN1, MOUNTAIN2, MOUNTAIN3, GOLF_FIELD, PINE, TREE, CHRISTMAS_TREE, PALM, RIVER, HOSPITAL, GARAGE, FIELD_FIRE, CLOUD, CLOUD_RAIN, CLOUD_LIGHTING, HELICOPTER, WATER_SCORE, DIAMOND_SCORE, LIFE_HEART, UNDER_CONSTRACTION, CONFLAGRATION, MOUNTAIN_START, MOUNTAIN_END, TREE_START, TREE_END, CLOUD_START, CLOUD_END, CLOUD_FIELD, CLOUD_RAIN_FIELD, CLOUD_LIGHTING_FIELD
from settings import HELICOPTER_TANK_DEFAULT, HELICOPTER_LIVE_DEFAULT, HELICOTPER_BONUS_FOR_SAVE_TREE, HELICOPTER_UPGRADE_TANK_COST, HELICOPTER_LIVE_COST
# from main import game_over
# global game_over
import os
# from os import system
from utils import pause
class Helicopter:

    def __init__(self, width, height):
        self.height = height
        self.width = width
        
        helicopter_field = randcell(width, height)
        tmpX = helicopter_field[0]
        tmpY = helicopter_field[1]
        self.PosX = tmpX
        self.PosY = tmpY

        self.tank = 0
        self.maxtank = HELICOPTER_TANK_DEFAULT
        self.score = 0
        self.lives = HELICOPTER_LIVE_DEFAULT
        self.TREE_BONUS = HELICOTPER_BONUS_FOR_SAVE_TREE
        self.UPGRADE_COST = HELICOPTER_UPGRADE_TANK_COST
        self.LIVE_COST = HELICOPTER_LIVE_COST

    def process_helicopter(self, field, field_cloud, field_fire):
        cell_field = field.cells[self.PosX][self.PosY]
        fire_field = field_fire.cells[self.PosX][self.PosY]
        cell_clouds = field_cloud.cells[self.PosX][self.PosY]
        if cell_field == RIVER:
            self.tank = self.maxtank
        if fire_field == 1 and self.tank > 0:
            self.tank -= 1
            self.score += self.TREE_BONUS
            field_fire.cells[self.PosX][self.PosY] = 0
        if cell_field == GARAGE and self.score >= self.UPGRADE_COST:
            self.maxtank += 1
            self.score -= self.UPGRADE_COST
        if cell_field == HOSPITAL and self.score >= self.LIVE_COST:
            self.lives += 10
            self.score -= self.LIVE_COST
        if cell_clouds == 3:
            self.lives -= 1
            if self.lives <= 0:
                self.game_over()    

    def move(self, move_x, move_y):
        # print("boom-boom")
        new_PosX = move_x + self.PosX
        new_PosY = move_y + self.PosY
        if 0 <= new_PosX < self.height and 0 <= new_PosY < self.width:
            self.PosX = new_PosX
            self.PosY = new_PosY

    def print_status(self):
        print(Emoji.CELL_TYPES[WATER_SCORE], " ", self.tank, "/", self.maxtank, sep="", end=" | ")
        print(Emoji.CELL_TYPES[LIFE_HEART], self.lives, end=" | ")
        print(Emoji.CELL_TYPES[DIAMOND_SCORE], self.score)        

    def print_status_messages(self):
        if self.score >= self.UPGRADE_COST:
            print("Можно увеличить запас воды!")
        if self.score >= self.LIVE_COST:
            print("Можно увеличить количество жизней!")

    # from os import system
    def game_over(self):
        while True:
            os.system("cls" if os.name == 'nt' else "clear")
            # os.system("clear") #для *nix-base систем
            # os.system("cls") #для windows систем
            print("========================================")
            print("========================================")
            print(f"                GAME OVER!")
            print(f"                 Ваш счёт:")
            print(f"                   {self.score}")
            print("========================================")
            print("========================================")

            print(f"")
            exit(0)
            #TODO выводить предложение загрузить игру, не заканчивая её, завершать при нажатии определённой клавиши

    def export_data(self):
        return {
            "score": self.score,
            "lives": self.lives,
            "PosX": self.PosX,
            "PosY": self.PosY,
            "tank": self.tank,
            "maxtank": self.maxtank,
        }

    # def import_date(self, data):
    #     self.PosY = data["PosX"] or 0
    #     self.PosY = data["PosY"] or 0
    #     self.tank = data["tank"] or 0
    #     self.maxtank = data["maxtank"] or HELICOPTER_TANK_DEFAULT
    #     self.lives = data["lives"] or HELICOPTER_LIVE_DEFAULT
    #     self.score = data["score"] or 0


#TODO ввести жизни на карте или добавление "брони" поверх жизней, которую можно ремонтировать, к примеру, бесплатно на базе
#по N пунктов за тик