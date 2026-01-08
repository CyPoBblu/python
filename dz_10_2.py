my_dict = {}

for n in range(10, -6, -1): #-6 = -5-1 (для "включительно")
    my_dict[n] = n**n
print(my_dict)