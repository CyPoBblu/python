
def age(age):
    #print(age)
    let = ''
    if age % 10 == 1 and (age % 100) // 10 != 1:
        let = str(age) + " год"
    elif age >= 10:
        k = (age % 100) // 10
        if k == 1:
            let = str(age) + " лет"
        else:
            if age % 10 <= 4 and age % 10 >= 1:
            #или
            #if age % 10 == 1 or age % 10 == 2 or age % 10 == 3 or age % 10 == 4:
                let = str(age) + " года"
            else:
                let = str(age) + " лет"
    elif age == 2 or age == 3 or age == 4:
        let = str(age) + " года"
    else:
        let = str(age) + " лет"
    if age == 0:
        let = "меньше года"
    return let

for n in range(105):
    print(f"возраст {n} - это {age(n)}")