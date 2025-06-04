
# import re

# def conta_parole(s: str) -> int:
#     parole = re.findall(r'\S+', s)
#     return len(parole)

def conta_parole_v2(s: str) -> int:
    in_parola = False
    conta = 0
    for c in s:
        if not c.isspace():
            if not in_parola:
                conta += 1
                in_parola = True
        else:
            in_parola = False
    return conta


def conta_parole_v1(s: str) -> int:
    # Usa split() senza argomenti per dividere la stringa su sequenze di spazi bianchi
    parole = s.split()
    return len(parole)

s = "  Questa e' una  stringa lunga 45 caratteri.  "
print(conta_parole_v1(s))
print(conta_parole_v2(s))

s = "1 2 3 a b c"
print(conta_parole_v1(s))
print(conta_parole_v2(s))

s = "! @?$ ciao,prova"
print(conta_parole_v1(s))
print(conta_parole_v2(s))