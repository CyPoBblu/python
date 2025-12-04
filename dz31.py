print("что у вас за питомец?")
vid = input()
print("как его зовут?")
name = input()
print("сколько ему полных лет?")
age = int(input())


if age % 10 == 1 and (age % 100) // 10 != 1:
    let = "год"
elif age >= 10:
    k = (age % 100) // 10
    if k == 1:
        let = "лет"
    else:
        if age % 10 <= 4:
        #или
        #if age % 10 == 1 or age % 10 == 2 or age % 10 == 3 or age % 10 == 4:
            let = "года"
        else:
            let = "лет"
elif age == 2 or age == 3 or age == 4:
    let = "года"
else:
    let = "лет"
if age == 0:
    print ("Это ", vid, " по кличке \"", name,"\". Возраст: меньше года", sep="")
else:
    print ("Это ", vid, " по кличке \"", name,"\". Возраст: ", age, " ", let, sep="")
