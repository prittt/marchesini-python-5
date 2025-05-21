print("Dammi due numeri m e n")
m = input("m: ")
m = int(m)
n = int(input("n: "))

# Versione 1
# min = m
# if n < m:
#     min = n
# mymin = min(n, m)
MCD = 1
i = 2
while i < min(n, m): # Sarebbe meglio evitare questa chiamata a funzione ripetuta 
    if m % i == 0 and n % i == 0:
        MCD = i
    i += 1

print(f"Il M.C.D. tra {m} e {n} è {MCD}")

# Versione 2
i = min(n, m)
while i > 0:
    if m % i == 0 and n % i == 0:
        MCD = i
        break
    i -= 1

print(f"Il M.C.D. tra {m} e {n} è {MCD}")

# a < b
# MCD(a, b) = MCD(a, b - a)
# MCD(7, 14) = MCD(7, 7) = MCD(7, 0)
# MCD(15, 6) = MCD(6, 9) = MCD(6, 3) = MCD(3, 3) = MCD(3, 0) 
a, b = m, n 
while a != b:
    # if a > b:
    #     a, b = b, a
    # b = b - a

    if a < b:
        b = b - a
    else:
        a = a - b 
print(f"Il M.C.D. tra {m} e {n} è {MCD}")

# MCD(a, b) = MCD(b, a % b)
# MCD(15, 6) = MCD(6, 3) = MCD(3, 0)
# MCD(6, 15) = MCD(15, 6) = MCD(6, 3) = MCD(3, 0)
a, b = m, n 
while b != 0:
    a, b = b, a % b 
print(f"Il M.C.D. tra {m} e {n} è {MCD}")


gcd(m, n)
