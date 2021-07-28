"""
set doesnot support duplicate value
"""
namelist1 = {1, 2, 3 , 4}
num2 = set([7, 5, 9 , 8])


namelist1.add(7)
namelist1.remove(3)
print(namelist1)
print(num2)
