
n= int(3)

check = {True: "Weird", False: "Not Weird"}

print(check[n%2==1 or n in range(6,21)])