import random
from decimal import Decimal
import sys
sys.set_int_max_str_digits(0)

#let square = 2 * 2
#let r = 1

InC = Decimal(“0”)
OutC = Decimal(“0“)

while 1 :
    t1 = random.random()
    t2 = random.random()
    if (abs(t1 - 1) ** 2 + abs(t2 - 1) ** 2) ** 0.5 < 1 :
        InC += 1
    else :
        OutC += 1
    if InC + OutC % 573647 :
    print(((InC / (InC + OutC)) * 4), str(InC +OutC))


"""
from decimal import Decimal, getcontext
getcontext().prec = 10000000
#how many pi u need
pie = Decimal("0")
tt = Decimal("0.1")
t = Decimal("0")
for i in range(16901960) :
#nlog(n) (* 2 for must acc)
    tt = pie
    pie = Decimal(str((Decimal("1")/Decimal("16")**t)*((Decimal("4")/(Decimal("8")*t+Decimal("1"))) - (Decimal("2")/(Decimal("8")*t+Decimal("4"))) - (Decimal("1")/(Decimal("8")*t+Decimal("5"))) - (Decimal("1")/(Decimal("8")*t+Decimal("6"))))))
    pie = pie + tt
    t += 1
    if i % 156  == 0 :
        print(i / 16901960)
print(pie, t)

#way 2 in quiter

"""
