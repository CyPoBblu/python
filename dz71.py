def palindrome(word):  
    # Сравниваем исходную строку с её реверсом  
    if word == word[::-1]:  
        return "Yes"  
    else:  
        return "No"  


word = input("Введите слово из маленьких латинских букв: ")

print(palindrome(word))
#test
#print(palindrome("gkdfhluldfjkbdvipaodophjidyfujrnkfgk"))
#print(palindrome("abggba"))
