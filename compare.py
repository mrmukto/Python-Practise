nimberofdegit = 0
numofchracter = 0

textt = input()

for x in textt:
     x = x.lower()
     if textt >= 'a' and textt <= "z":
        numofchracter = numofchracter +1

     elif (textt >= '1' and textt <= '9'):
          nimberofdegit = nimberofdegit + 1

print(numofchracter)
print(nimberofdegit)






