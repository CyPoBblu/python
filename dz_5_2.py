#проверка
#word = "gkdfhluldfjkbdvipaodophjidyfujrnkfgk"
word = input("Введите слово из маленьких латинских букв: ")

#TODO проверка на дурака на наличие символов - не букв латинского языка или больших букв

vowels = 0  # количество гласных
consonants = 0  # количество согласных

# Счётчики
a = 0
e = 0
i = 0
o = 0
u = 0

for letter in word:
    if letter in 'aeiou':
        vowels += 1
        if letter == 'a':
            a += 1
        elif letter == 'e':
            e += 1
        elif letter == 'i':
            i += 1
        elif letter == 'o':
            o += 1
        elif letter == 'u':
            u += 1
    else:
        consonants += 1

# Выводим результаты
print(f"Количество гласных: {vowels}")
print(f"Количество согласных: {consonants}")
#или без ввода переменной consonants
print("Количество согласных:", (len(word)-vowels))


# if a > 0:
#     print(f"Количество букв 'a': {a}")
# else:
#     print("Количество букв 'a': False")

# if e > 0:
#     print(f"Количество букв 'a': {e}")
# else:
#     print("Количество букв 'a': False")

# if i > 0:
#     print(f"Количество букв 'a': {i}")
# else:
#     print("Количество букв 'a': False")

# if o > 0:
#     print(f"Количество букв 'a': {o}")
# else:
#     print("Количество букв 'a': False")

# if u > 0:
#     print(f"Количество букв 'a': {u}")
# else:
#     print("Количество букв 'a': False")

# или 
print(f"Количество букв 'a': {a if a > 0 else False}")
print(f"Количество букв 'e': {e if e > 0 else False}")
print(f"Количество букв 'i': {i if i > 0 else False}")
print(f"Количество букв 'o': {o if o > 0 else False}")
print(f"Количество букв 'u': {u if u > 0 else False}") 