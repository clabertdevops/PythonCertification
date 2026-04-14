'''
import time
'''

a_bytes = bytes(3)
b_array = bytearray(3)
print(a_bytes)
print(b_array)
print(a_bytes == b_array) # sono uguali al confronto

try:
    a_bytes[0] = 1
except Exception as e:
    print(e)

b_array[0] = 1
print(b_array)

print('----------------------------------------------------')

import time
n = 100_000_000
start = time.time()
b = bytes(b'x' * n)
stop = time.time()
print('bytes()', stop - start)
start = time.time()
b = bytearray(b'x' * n)
stop = time.time()
print('bytearray()', stop - start)


#----------------------------------------------

# Da una stringa (serve l'encoding)
ba1 = bytearray("ciao", "utf-8")
print(ba1)          # bytearray(b'ciao')

# Da una lista di interi (0-255)
ba2 = bytearray([72, 101, 108, 108, 111])
print(ba2)          # bytearray(b'Hello')

# Bytearray di zeri, lunghezza 5
ba3 = bytearray(5)
print(ba3)          # bytearray(b'\x00\x00\x00\x00\x00')

ba4 = bytearray(b"Python")
print(ba4)          # bytearray(b'Python')

ba = bytearray(b"ciao")

# Modifica un singolo byte (serve un intero 0-255)
ba[0] = 67          # 67 = 'C' in ASCII
print(ba)           # bytearray(b'Ciao')

ba = bytearray(b"hello")

# Append di un byte
ba.append(33)       # 33 = '!'
print(ba)           # bytearray(b'hello!')

# Extend con altri byte
ba.extend(b" world")
print(ba)           # bytearray(b'hello! world')

# Insert
ba.insert(0, 42)    # 42 = '*'
print(ba)           # bytearray(b'*hello! world')

# Pop (rimuove e restituisce l'ultimo byte)
ultimo = ba.pop()
print(ultimo)       # 100 (= 'd')
print(ba)           # bytearray(b'*hello! worl')

# Remove (rimuove la prima occorrenza del valore)
ba.remove(42)       # toglie '*'
print(ba)           # bytearray(b'hello! worl')

ba = bytearray(b"Hello World")

# Slicing (come le liste)
print(ba[0:5])      # bytearray(b'Hello')

# Assegnamento a slice — potentissimo!
ba[6:11] = b"Python"
print(ba)           # bytearray(b'Hello Python')

# Si può anche cambiare lunghezza
ba[5:5] = b","      # inserisce una virgola
print(ba)           # bytearray(b'Hello,Python')

ba = bytearray(b"Ciao")

# → bytes (immutabile)
b = bytes(ba)
print(type(b))      # <class 'bytes'>

# → stringa
s = ba.decode("utf-8")
print(s)            # "Ciao"

# → lista di interi
lista = list(ba)
print(lista)        # [67, 105, 97, 111]

ba = bytearray(b"ABC")
for byte in ba:
    print(byte, chr(byte))

# Output:
# 65 A
# 66 B
# 67 C