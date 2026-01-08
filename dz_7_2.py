


words = input("Введите предложение до 1000 символов, состоящее из маленьких латинских букв: ")
#TODO проверка на количество символов и на заглавные 
#test
#words = "ifdgi sdioi g   oisg   osiogi osig"


def delete_double_spaces(string):
    string1 = string.split()
    string2 = " ".join(string1)
    #или
    #string2 = " ".join(string.split())
    return string2
    #или
    #return " ".join(string.split())
    
output_string = delete_double_spaces(words)
print (f"Было:\n{words}")
print (f"Стало:\n{output_string}")