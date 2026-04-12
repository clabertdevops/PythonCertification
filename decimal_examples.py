from decimal import Decimal

wrong = Decimal(0.1) # errore creare il float
right = Decimal("0.1")

print(wrong)
print(right)

# Con float: DISASTRO
prezzo = 19.99
quantita = 3
totale_float = prezzo * quantita
print(f"Float: {totale_float}")  # 59.97000000000001

prezzo_d = Decimal("19.99")
quantita_d = Decimal("3")
totale_decimal = prezzo_d * quantita_d
print(f"Decimal: {totale_decimal}")  # 59.97

from decimal import Decimal, getcontext, ROUND_HALF_UP, ROUND_HALF_EVEN

# imposta precisione globale
getcontext().prec = 6

# Diversi modi di arrotondare
valore = Decimal("2.675")

# Arrotondamento "bancario" (default): ROUND_HALF_EVEN
print(valore.quantize(Decimal("0.01"), rounding=ROUND_HALF_EVEN)) #2.68

# Arrotondamento "classico": ROUND_HALF_UP
print(valore.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))  # 2.68

import timeit
# i Float sono più veloci perchè sono operazioni in Hardware

time_float = timeit.timeit("a * b",
                           setup="a = 3.14159; b = 2.71828",
                           number=1_000_000_000
                           )

#Decimal

tempo_float  = timeit.timeit(
    "a * b", 
    setup="from decimal import Decimal; a = Decimal('3.14159'); b = Decimal('2.71828')", 
    number=1_000_000_000
)


# Test con Decimal
tempo_decimal = timeit.timeit(
    "a * b", 
    setup="from decimal import Decimal; a = Decimal('3.14159'); b = Decimal('2.71828')", 
    number=1_000_000
)

print(f"Float:   {tempo_float:.4f} secondi")
print(f"Decimal: {tempo_decimal:.4f} secondi")
print(f"Decimal è ~{tempo_decimal/tempo_float:.0f}x più lento")
