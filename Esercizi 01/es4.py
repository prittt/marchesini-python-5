n = int(input("Inserisci un numero:"))
i = 2
primo = True
while i <= int(n ** 0.5):
    if n % i == 0:
        primo = False
        break
    i += 1

primo_text = "è primo" if primo else "non è primo"
print(f"Il numero {n} {primo_text}")
