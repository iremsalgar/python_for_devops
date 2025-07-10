#dik açılı bir üçgenin hipotenüsünün hesaplanması

import math

a = float(input("enter a corner : "))
b = float(input("enter b corner : "))
a = pow(a, 2)
b = pow(b, 2)
d = a + b
c = math.sqrt(d)
print(c)

#other way
# c = math.sqrt(pow(a, 2) + pow(b, 2))