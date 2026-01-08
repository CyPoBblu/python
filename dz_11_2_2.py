import os
os.system("cls")


import collections
pets = dict()

print("\033[H\033[J", end="")

#=====================================================================================================================================
#функция rand - для автоматической генерации данных по животным
#=====================================================================================================================================
import random
import time
from datetime import datetime
def rand():
    
    time.sleep(random.uniform(0.001, 0.006))
    random.seed(datetime.now().timestamp())
    number = random.randint(1, 50) #TODO можно запрашивать у пользователя степень разнообразия базы для теста
    #test print number1
    #print(f"number1={number1}")
    # time.sleep(random.uniform(0.1, 0.6))
    #time.sleep(0.3)
    # random.seed(datetime.now().timestamp())
    # number2 = random.randint(1, 100) 
    #test print number2
    #print(f"number2={number2}")

    # plenty1 = set()
    # plenty2 = set()
    # #Генерируем первый список (множество)
    # for n in range(number1):
    #     plenty1.add(random.randint(1,100000))
    # print(plenty1)
    # #Генерируем второй список (множество)
    # for n in range(number2):
    #     plenty2.add(random.randint(1,100000))
    # print(plenty2)
    return(number)


#=====================================================================================================================================
#функция get_suffix
#=====================================================================================================================================
def get_suffix(age):
    #print(age)
    let = ""
    if age % 10 == 1 and (age % 100) // 10 != 1:
        let = ": " + str(age) + " год"
    elif age >= 10:
        k = (age % 100) // 10
        if k == 1:
            let = ": " + str(age) + " лет"
        else:
            if age % 10 <= 4 and age % 10 >= 1:
            #или
            #if age % 10 == 1 or age % 10 == 2 or age % 10 == 3 or age % 10 == 4:
                let = ": " + str(age) + " года"
            else:
                let = ": " + str(age) + " лет"
    elif age == 2 or age == 3 or age == 4:
        let = ": " + str(age) + " года"
    else:
        let = ": " + str(age) + " лет"
    if age == 0:
        let = " меньше года"
    return let


#=====================================================================================================================================
#функция get_pet проверит, есть ли животное с таким ID в базе
#=====================================================================================================================================
def get_pet(id):
    return pets[id] if id in pets.keys() else False

#=====================================================================================================================================
#test
#функция unique_pet проверит, есть ли животное с такими параметрами как имя/тип/возраст/владелец в базе
#TODO составить версию, где могут быть схожие питомцы с одинаковыми данными
#=====================================================================================================================================
#def unique_pet(name,type1,age,owner)




#=====================================================================================================================================
#функция create_auto создаст в базе запись о животном
#=====================================================================================================================================
def create_auto():
    #print("Введите информацию о питомце:")
    #name = input("Введите имя питомца: ")
    #type1 = input("Введите вид питомца: ")
    #age = int(input("Введите возраст питомца: "))
    #owner = input("Введите имя владельца питомца: ")
    #============
    #test
    rondo = rand()
    name = str(rondo) + "_name"
    type1 = str(rondo) + "_type1"
    age = rondo
    owner = str(rondo) + "_owner"
    #============

    #проверка на пустой словарь
    if not pets:
        
        #print(f"len(pets.keys) == {len(pets.keys())}")
        new_id = 1
        # print(pets)
        pets[new_id] = {name : ""}
        # print(pets)
        #pets[new_id][name] = {"вид": type1, "возраст": age, "владелец": owner}
        pets[new_id][name] = {
            "вид" : type1,
            "возраст" : age,
            "владелец" : owner
        }
        # pets[new_id][name]["вид"] = type1
        # print(pets)
        # pets[new_id][name]["возраст"] = age
        # print(pets)
        # pets[new_id][name]["владелец"] = owner
        # print(f"test0 {pets}")
        
        #print(f"len(pets.keys) == {len(pets.keys())}")
        #print(f"rondo={rondo}")
        #print(pets)
        
    else:
        #print(f"rondo={rondo}")
        last_id = collections.deque(pets, maxlen=1)[0]
        #print(last_id)
        new_id = last_id + 1
        
        # print(f"test2 {pets}")
        # print(f"new_id={new_id}")
        # print(f"test1 {pets.keys()}")
        
        
        #TODO неправильная проверка в случае, если возможны одинаковые данные при разных ID - нужно переделать
        #print(f"len(pets.keys) == {len(pets.keys())}")
        signal = 0
        # print(f"len(pets)={len(pets)}")
        for i in range(1, len(pets)+1):
            #print(f"i={i}")
            #key = pets[i].keys()
            #print(f"key={key}")
            
            #print(f"name={name}")
            #print(f"pets[i][name]={pets[i][str(name)]}")


            #print(pets[new_id])
                # pets[new_id] = {name : ""}
            # print(pets)
                #pets[new_id][name] = {"вид": type1, "возраст": age, "владелец": owner}
                # pets[new_id][name] = {
                #     "вид" : type1,
                #     "возраст" : age,
                #     "владелец" : owner
                # }

            # print(f"test {pets[i].keys()}")
            # print(f"test3 name= {pets[i]}")
            # print(f"test4 name= {name}")
            if name == pets[i].keys():
                if pets[i][name]["вид"] == type1 and pets[i][name]["владелец"] == owner and pets[i][name]["возраст"] == age:
                    return
                
            #if name in pets.keys() and type1 in pets.keys() and owner in pets.keys():
        pets[new_id] = {name: ""}
        # print(f"test5 new_id= {new_id}")
        # print(f"test6 pets[new_id]= {pets[new_id]}")
        # print(f"test7 name= {name}")
        
        pets[new_id][name] = {"вид": type1, "возраст": age, "владелец": owner}

        #print(f"len(pets.keys) == {len(pets.keys())}")
        #print(pets)
        #print(f"len(pets.keys()))={len(pets)}")

#=====================================================================================================================================
#функция create_auto создаст в базе запись о животном
#=====================================================================================================================================
def create():
    print("Введите информацию о питомце:")
    name = input("Введите имя питомца: ")
    type1 = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    owner = input("Введите имя владельца питомца: ")
    #============
    #test
    # rondo = rand()
    # name = str(rondo) + "_name"
    # type1 = str(rondo) + "_type1"
    # age = str(rondo) + "_age"
    # owner = str(rondo) + "_owner"
    #============

    #проверка на пустой словарь
    if not pets:
        
        #print(f"len(pets.keys) == {len(pets.keys())}")
        new_id = 1

        pets[new_id] = {name : ""}
        pets[new_id][name] = {
            "вид" : type1,
            "возраст" : age,
            "владелец" : owner
        }
        
        #print(f"len(pets.keys) == {len(pets.keys())}")
        #print(f"rondo={rondo}")
        #print(pets)
        
    else:
        #print(f"rondo={rondo}")
        last_id = collections.deque(pets, maxlen=1)[0]
        #print(last_id)
        new_id = last_id + 1
    
        #print(new_id)
        #print(pets.keys())
        
        
        #TODO неправильная проверка в случае, если возможны одинаковые данные при разных ID - нужно переделать
        #print(f"len(pets.keys) == {len(pets.keys())}")
        signal = 0
        for i in range(1, len(pets)+1):
            #print(f"i={i}")
            #key = pets[i].keys()
            #print(f"key={key}")





            if name == pets[i].keys():
                if pets[i][name]["вид"] == type1 and pets[i][name]["владелец"] == owner and pets[i][name]["возраст"] == age:
                    print(f"неправильная команда, для обновления записи животного используйте команду update") #по идее меняется только возраст... хотя, может, ещё и хозяин поменятся
                    return
            signal = 1    
            #if name in pets.keys() and type1 in pets.keys() and owner in pets.keys():
        pets[new_id] = {name: ""}
        # print(f"test5 new_id= {new_id}")
        # print(f"test6 pets[new_id]= {pets[new_id]}")
        # print(f"test7 name= {name}")
        
        pets[new_id][name] = {"вид": type1, "возраст": age, "владелец": owner}
        print("Данные успешно записаны в базу данных")
        tmp2 = list(pets[new_id])
        #print(f"tmp={tmp2[0]}")
        print(f"Добавлено животное {pets[new_id][name]["вид"]} по кличке \"{tmp2[0]}\". Возраст питомца{get_suffix(pets[new_id][name]["возраст"])}. Имя владельца: {pets[new_id][name]["владелец"]}")
        




        #print(f"len(pets.keys) == {len(pets.keys())}")
        #print(pets)
        #print(f"len(pets.keys()))={len(pets)}")


#=====================================================================================================================================
#функция read выведет информацию о животном
#TODO усовершенствовать функцию до read(id,a) и в зависимости от a - выводить строки с информацией разные, чтобы избавиться от write
#пример:
#Это желторотый питон по кличке "Каа". Возраст питомца: 19 лет. Имя владельца: Саша
#=====================================================================================================================================
def read():
    id = int(input("Введите ID записи для вывода информации: "))
    if not get_pet(id):
        print(f"Запись животного с ID: {id} не найдена в базе данных клиники. Проверьте и попробуйте снова")
        return
    else:        
        name = list(pets[id].keys())[0]
        print(f"Это {pets[id][name]["вид"]} по кличке \"{name}\". Возраст питомца{get_suffix(pets[id][name]["возраст"])}. Имя владельца: {pets[id][name]["владелец"]}")
        
    return False

#=====================================================================================================================================
#функция write выведет информацию о животном
#пример:
#ID: 777 Животное: желторотый питон по кличке "Каа". Возраст питомца меньше года. Имя владельца: Петя
#=====================================================================================================================================
def write(id):
    if not get_pet(id):
        return
    else:
        #name = str(list(pets[id].keys())[0])
        name = list(pets[id].keys())[0]
        print(f"ID: {id} Животное: {pets[id][name]["вид"]} по кличке \"{name}\". Возраст питомца{get_suffix(pets[id][name]["возраст"])}. Имя владельца: {pets[id][name]["владелец"]}")
    return False


#=====================================================================================================================================
#функция update обновит данные по животному в базе
#=====================================================================================================================================
def update():
    id = int(input("Введите ID записи для изменения информации: "))
    if not get_pet(id):
        print(f"Запись животного с ID: {id} не найдена в базе данных клиники. Проверьте и попробуйте снова")
        return
    else:
        print(f"Введите данные для обновления записи:")
        name = input("Введите имя питомца: ")
        type1 = input("Введите вид питомца: ")
        age = int(input("Введите возраст питомца: ")) #TODO добавить проверку на число 
        owner = input("Введите имя владельца питомца: ")
        pets[id] = {name: {}}

        pets[id][name]["вид"] = type1
        # pets[id]["имя"] = name
        pets[id][name]["возраст"] = age
        pets[id][name]["владелец"] = owner
        print(f"Запись животного с ID: {id} обновлена в базе данных")
        print(f"Новые данные в базе данных:")
        write(id)
        return

#=====================================================================================================================================
#функция delete удалит данные по животному из базы
#=====================================================================================================================================
def delete():
    id = int(input("Введите ID записи для удаления из базы данных: "))
    if not get_pet(id):
        print(f"Запись животного с ID: {id} не найдена в базе данных клиники. Проверьте и попробуйте снова")
        return
    else:
        del pets[id]
        print(f"Запись животного с ID: {id} удалена из базы клиники.")
        return
        


#=====================================================================================================================================
#функция menu
#=====================================================================================================================================
def menu():
    
    print("")
    print("==========Menu=========")
    print("Введите команду:")
    print("\033[33mtest - будет сгенерирова база рандомными записями для теста (максимум 30 записей):) \033[0m\033[1;31m[для тестов]\033[0m")
    print("create - создать запись о животном в базе данных")
    print("update - обновить запись о животном в базе данных")
    print("read - вывести запись о животном из базы данных")
    print("delete - удалить запись о животном из базы данных клиники")
    print("base - вывести все записи из базы данных клиники")
    print("\033[33mclear - очистить все записи из базы данных клиники \033[0m\033[1;31m[для тестов]\033[0m")
    print("stop - завершить работу программы")

    command = input()
    return command

#=====================================================================================================================================
#функция pets_list выведет все записи в базе
#=====================================================================================================================================
def pets_list():
    if pets.keys():
        print("Весь список животных клиники:")
        for pet in pets.keys():
            for pet2 in pets[pet].keys():
                write(pet)
    else:        
        print("В клинике нет животных на данный момент. Все здоровы, аднака!")



#============
#test создание базы данных
#============
def test_base():    
    pets.clear()
    for n in range(5,25):
        create_auto()
    print("сгенерированная база данных животных:")
    print(pets)


def clear():
    pets.clear()
    print("база данных очищена")



#=====================================================================================================================================
#основная программа
#=====================================================================================================================================

while True:
    command = menu()
    if command.lower() == "stop":
        print("\033[H\033[J", end="")
        print("stop")
        print(f"Команда \"stop\" получена. Завершение программы.")
        break
    elif command.lower() == "test":
        print("\033[H\033[J", end="")
        print("test")
        print("")
        test_base()
    elif command.lower() == "create":
        print("\033[H\033[J", end="")
        print("create")
        print("")
        create()
    elif command.lower() == "update":
        print("\033[H\033[J", end="")
        print("update")
        print("")
        update()
    elif command.lower() == "read":
        print("\033[H\033[J", end="")
        print("read")
        print("")
        read()
    elif command.lower() == "delete":
        print("\033[H\033[J", end="")
        print("delete")
        print("")
        delete()
    elif command.lower() == "base":
        print("\033[H\033[J", end="")
        print("base")
        print("")
        pets_list()
    elif command.lower() == "clear":
        print("\033[H\033[J", end="")
        print("clear")
        print("")
        clear()
    else:
        print("")
        print(f"Такой команды не существует, повторите ввод")
