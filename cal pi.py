import random

#let square = 2 * 2
#let r = 1

InC = 0
OutC = 0

for i in range(1000000000) :
    t1 = random.random()
    t2 = random.random()
    if (abs(t1 - 1) ** 2 + abs(t2 - 1) ** 2) ** 0.5 < 1 :
        InC += 1
    else :
        OutC += 1

print(((InC / (InC + OutC)) * 4))