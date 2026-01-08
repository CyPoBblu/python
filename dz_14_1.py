# def recur(n):
#     if n > 16:
#         return
#     print(n, end=" ")
#     recur (n + 1)
    

# recur(0)
# print("конец списка")



my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def recur(list, n = 0):
    if n >= len(list):
        return
    print(list[n], end=" ")
    recur (list, n + 1)
    
# print(len(my_list))
recur(my_list)
print("конец списка")
