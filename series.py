
# 2 + 4 + ______ + n

n = int(input())
sum = 0
for x in range(2, n+1, 2):
    sum = sum + x*x

print(sum) 