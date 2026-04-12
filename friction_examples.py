
from fractions import Fraction

#float impreciso
sum_float = 0.1 + 0.2 # 0.30000000000000004
print(sum_float == 0.3)

# Fraction: esatto
sum_friction = Fraction(1,10) + Fraction(2,10)
print(sum_friction == Fraction(3,10))

Fraction(6, 8)   # Fraction(3, 4)
Fraction(-6, 8)  # Fraction(-3, 4) — segno al numeratore

# ⚠️ Da float — converte il valore binario esatto
Fraction(0.1)    # Fraction(3602879701896397, 36028797018963968)

# ✅ Da stringa — converte il valore decimale inteso
Fraction('0.1')  # Fraction(1, 10)

import math
pi = Fraction(math.pi)
pi.limit_denominator(10)   # Fraction(22, 7)
pi.limit_denominator(100)  # Fraction(311, 99)