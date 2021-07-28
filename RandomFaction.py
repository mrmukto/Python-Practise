import random
guess = int(input())
randomNUmner = random.randint(1,8)
 
if guess == randomNUmner:
    print("OK")

else:
    print("Not Ok")