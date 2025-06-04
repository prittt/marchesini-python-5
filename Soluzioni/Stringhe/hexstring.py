def hexstring2vec(s: str) -> list[int]:
    #[oggetto for qualcosa in iterabile]
    
    values = [int(s[i:i+2], 16) for i in range(0, len(s), 2)]
    # values = []
    # for i in range(0, len(s), 2):
    #     values.append(int(s[i:i+2], 16)) # values += [int(chars, 16)]
    
    # while len(values) < 8:
    #     values.append(0)

    values += [0] * (8 - len(values))

    return values

def print_hex(lista: list[int]):
    print(f"[{hex(lista[0])}", end="")
    for i in range(1, len(lista)):
        print(f", {hex(lista[i])}", end="")
    print("]")

print_hex(hexstring2vec("12AB34CD56EF7890"))  
print(hexstring2vec("35AF"))              
print(hexstring2vec(""))                  