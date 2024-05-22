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
