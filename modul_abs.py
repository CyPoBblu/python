def modul(x1, x2):
    if x1 > x2:
        if x1 <= 0:
            return (-1 * x2) - (-1 * x1)
        else:
            if x2 <= 0:
                return x1 + (-1 * x2)
            else:
                return x1 - x2
    elif x1 < x2:
        if x2 <= 0:
            return (-1 * x1) - (-1 * x2)
        else:
            if x1 <= 0:
                return x2 + (-1 * x1)
            else:
                return x2 - x1
    else:
        return 0
    

print(f"modul(5,4) = {modul(5,4)}")
print(f"modul(5,3) = {modul(5,3)}")
print(f"modul(5,0) = {modul(5,0)}")
print(f"modul(5,-3) = {modul(5,-3)}")
print(f"modul(5,-10) = {modul(5,-10)}")
print(f"modul(0,0) = {modul(0,0)}")
print(f"modul(-1,-4) = {modul(-1,-4)}")
print(f"modul(-4,-1) = {modul(-4,-1)}")
print(f"modul(-10,5) = {modul(-10,5)}")
print(f"modul(-3,5) = {modul(-3,5)}")
print(f"modul(0,5) = {modul(0,5)}")
print(f"modul(3,5) = {modul(3,5)}")