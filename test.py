
#TODO implement this maximum into Divide.py

import sys

import decimal
from tracemalloc import reset_peak


ramUsage = 200  # this is the amount of ram in mb for each variable to use
maxDigits = 19 * ((ramUsage * 1024**2) // 8) 

decimal.setcontext(decimal.Context(prec=maxDigits))

res = decimal.Decimal(5) / decimal.Decimal(1.1)

with open('number', 'w') as f:
    f.write(str(res))
    f.close()

print(sys.getsizeof(res))
print(maxDigits)

