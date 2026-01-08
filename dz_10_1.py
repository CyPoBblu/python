pets = {}
name = input("Введите имя питомца: ")
#test
#name = "Мухтар"
pets[name] = {"Вид питомца": input("Введите вид питомца: "),"Возраст питомца": int(input("Сколько полных лет питомцу?: ")),"Имя владельца": input("Введите имя владельца: ")}
#test 
#pets[name] = {"Вид питомца": "собака","Возраст питомца": 30,"Имя владельца": "Иван"}

#print (pets)
# pet = str(pets.keys())
# print (pet)
# print (pets[inp]['Возраст питомца'])

age = pets[name]['Возраст питомца']
#print(age)

if age % 10 == 1 and (age % 100) // 10 != 1:
    let = "год"
elif age >= 10:
    k = (age % 100) // 10
    if k == 1:
        let = "лет"
    else:
        if age % 10 <= 4 and age % 10 >= 1:
        #или
        #if age % 10 == 1 or age % 10 == 2 or age % 10 == 3 or age % 10 == 4:
            let = "года"
        else:
            let = "лет"
elif age == 2 or age == 3 or age == 4:
    let = "года"
else:
    let = "лет"

print(pets[name].keys())
print(f"Это ", end="")
for k in pets[name].keys():
    if k == "Вид питомца":
        print(f"{pets[name][k]} по кличке \"{name}\". ", end="")
        #print(f" по кличке \"", name,"\". ", end="")
    elif k == "Возраст питомца":
        if pets[name][k] == 0:
            print(f"{k}: меньше года. ", end="")
        else:
            print(f"{k}: {age} {let}. ", end="")
    else:        
        print(f"{k}: ", end="")
        print(pets[name][k], end="")

#или проще вывести так без метода .keys()
#if age == 0:
    #print ("Это ", pets[name]["Вид питомца"], " по кличке \"", name,"\". Возраст питомца: меньше года. Имя владельца: ", pets[name]["Имя владельца"], sep="")
#else:
    #print ("Это ", pets[name]["Вид питомца"], " по кличке \"", name,"\". Возраст питомца: ", age, " ", let, ". Имя владельца: ", pets[name]["Имя владельца"], sep="")


#необходим результат подобного рода
#Это желторотый питон по кличке "Каа". Возраст питомца: 19 лет. Имя владельца: Саша


#TODO выяснить, как можно использовать метод .values() для решения задачи (кроме как выводить значения, а по ним искать и выводить наименование ключа(лишний for))