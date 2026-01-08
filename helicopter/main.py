from map import Map
from pynput import keyboard
from helicopter import Helicopter
from fires import Fire, WOOD_BURNING_TIME, FIRE_UPDATE
from clouds import Clouds
from settings import MOVES, MAP_WIDTH, MAP_HEIGHT, TICK_SLEEP, TREE_UPDATE, CLOUDS_UPDATE, FIRES_MIN, FIRES_MAX, HELICOPTER_LIVE_DEFAULT, HELICOPTER_TANK_DEFAULT, TICKS
import time
import os
import json
from utils import rnd
from utils import pause

game_paused = False

def save_game():
    time.sleep(2)
    pause(5)
    global game_paused
    data = {
        "helicopt": helicopt.export_data(),
        'fires': field_fire.export_data(),        
        "field": field.export_data(),        
        "clouds": field_cloud.export_data(),
        "tick": tick
    }
    with open("savegame.json", "w", encoding='utf-8') as sf:
        json.dump(data, sf)
    pause(10)
    print("Игра сохранена!")
    game_paused = True
    pause(2)

def load_game():
    global helicopt, field, field_cloud, tick, game_paused
    try:
        with open("savegame.json", "r", encoding='utf-8') as rf:
            data = json.load(rf)
        # данные вертолёта
        helicopt.score = data["helicopt"]["score"] or 0
        helicopt.lives = data["helicopt"]["lives"] or HELICOPTER_LIVE_DEFAULT
        helicopt.PosX = data["helicopt"]["PosX"] or 0
        helicopt.PosY = data["helicopt"]["PosY"] or 0
        helicopt.tank = data["helicopt"]["tank"] or 0
        helicopt.maxtank = data["helicopt"]["maxtank"] or HELICOPTER_TANK_DEFAULT
        
        # данные карты местности
        field.cells = data["field"]["cells"] or [[0 for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
        field.ticks = data["field"]["ticks"] or TICKS

        # данные слоя пожаров
        field_fire.cells = data["fires"]["cells"] or [[0 for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
        field_fire.ticks = data["fires"]['ticks'] or TICKS

        # данные слоя облаков
        field_cloud.cells = data["clouds"]["cells"] or [[0 for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]

        # данные времени
        tick = data["tick"]
        
        print("Игра загружена!")
        game_paused = True
        time.sleep(2)
    except FileNotFoundError:
        print("Сохранение не найдено!")
        time.sleep(1)
    except Exception as e:
        print(f"Ошибка загрузки: {e}")
        time.sleep(1)


def process_key(key):
    global helicopt, field, field_cloud, field_fire, tick
    try:
        button = key.char.lower()
        if button in MOVES.keys():
            dx, dy = MOVES[button][0], MOVES[button][1]
            helicopt.move(dx, dy)
        elif button == 't':
            save_game()
        elif button == 'p':
            load_game()
    except AttributeError:
        pass

listener = keyboard.Listener(
    on_press=None,
    on_release=process_key)
listener.start()

#генерация поля
field = Map(MAP_WIDTH, MAP_HEIGHT)

# #генерация пожаров
field_fire = Fire(MAP_WIDTH, MAP_HEIGHT)

# #генерация облаков
field_cloud = Clouds(MAP_WIDTH, MAP_HEIGHT)

#генерация вертолёта
helicopt = Helicopter(MAP_WIDTH, MAP_HEIGHT)

tick = 1

def save_load_menu():
    print()
    print('Нажмите t - сохранить. p - загрузить.')

while True:
    if game_paused:
        input("Нажмите Enter чтобы продолжить...")
        game_paused = False
    os.system("cls" if os.name == 'nt' else "clear")
    # os.system("clear") #для *nix-base систем
    # os.system("cls") #для windows систем
    print("Tick", tick)

    # Map.printmap(field, helicopt)

    helicopt.print_status()
    field.printmap(field_fire, helicopt, field_cloud)
    helicopt.process_helicopter(field, field_cloud, field_fire)
    # field.printmap(field_fire, helicopt, field_cloud)
    helicopt.print_status_messages()
    save_load_menu()
    time.sleep(0.2)
    tick += 1
    if tick % TREE_UPDATE == 0:
        field.generate_new_trees(tick)
    # создание новых пожаров
    if tick % FIRE_UPDATE == 0:
        for i in range(rnd(FIRES_MIN,FIRES_MAX)):
            field_fire.generate_new_fire(field, tick)
            i += 1
    # обновление пепелищ и новые пожары
    if tick % (WOOD_BURNING_TIME) == 0:
        field_fire.update_fires(field, tick, field_cloud)
        for i in range(rnd(FIRES_MIN,FIRES_MAX)):
            field_fire.generate_new_fire(field, tick)
            i += 1
    # обновление облаков
    if tick % (CLOUDS_UPDATE) == 0:
        field_cloud.update_clouds()