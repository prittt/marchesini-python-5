def rimuovi_singoli_spazi_v01(s: str) -> str:
    result = ""
    i = 0
    while i < len(s):
        if s[i] == ' ':
            start = i
            while i < len(s) and s[i] == ' ':
                i += 1
            if i - start > 1:
                result += s[start:i] # result += " "* (i - start) 
        else:
            result += s[i]
            i += 1
    return result


print(rimuovi_singoli_spazi_v01(" a b c "))
print(rimuovi_singoli_spazi_v01("  a  b  c  "))
print(rimuovi_singoli_spazi_v01("  abc   def ghi   jkl    mno pqr  s "))  