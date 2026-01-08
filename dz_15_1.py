class Transport:
   def __init__(self, name, max_speed, mileage):
       self.name = name
       self.max_speed = max_speed
       self.mileage = mileage


# Создайте объект Autobus, который унаследует все переменные и методы родительского класса Transport и выведете его.
# Ожидаемый результат вывода:
# Название автомобиля: Renault Logan Скорость: 180 Пробег: 12

Autobus = Transport ("Renault Logan", 180, 12)
# print (f"Название автомобиля: {auto.name} Скорость: {auto.max_speed} Пробег: {auto.mileage}")  #вывод по заданию
print (f"Название автомобиля: {Autobus.name}. Скорость: {Autobus.max_speed} км/ч. Пробег: {Autobus.mileage} км.")
# print (f"Название автомобиля: {auto.name}. \nСкорость: {auto.max_speed} км/ч. \nПробег: {auto.mileage} км.")