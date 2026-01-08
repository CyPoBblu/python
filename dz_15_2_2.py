class Transport(object):
   def __init__(self, name, max_speed, mileage):
       self.name = name
       self.max_speed = max_speed
       self.mileage = mileage

   def seating_capacity(self, capacity):
       return f"Вместимость одного автобуса {self.name}  {capacity} пассажиров"


class Autobus(Transport):
    capacity = 50
    def seating_capacity(self):
        return f"Вместимость одного автобуса {self.name}  {self.capacity} пассажиров"

auto = Autobus("Renault Logan", 180, 12) #по-умолчанию, вес равен 50
# auto = Autobus("Renault Logan", 180, 12, 75) #вес не прописан в __init__(self для класса Autobus, поэтому конструкция ошибочна - задача не требует изменение параметра
print(auto.seating_capacity())

# Создайте класс Autobus, который наследуется от класса Transport. 
# Дайте аргументу Autobus.seating_capacity() значение по умолчанию 50.
# Используйте переопределение метода.
# Используйте следующий код для родительского класса транспортного средства:
# class Transport:
#    def __init__(self, name, max_speed, mileage):
#        self.name = name
#        self.max_speed = max_speed
#        self.mileage = mileage

#    def seating_capacity(self, capacity):
#        return f"Вместимость одного автобуса {self.name}  {capacity} пассажиров"
# Ожидаемый результат вывода:
# Вместимость одного автобуса Renault Logan: 50 пассажиров