# Ejercicio 1
# 1.1) Si se implementa con tipos genericos sirve para buscar una caracter en una string
def pertenece (s:list, e:int) -> bool:
    for i in s:
        if i == e:
            return True
    return False

# 1.2)
def divideATodos (s:list, e:int) -> bool:
    for i in s:
        if not i % e == 0:
            return False
    return True

# 1.3)
def sumaTotal (s:list) -> int:
    total = 0
    for i in s:
        total += i
    return total

# 1.4)
def ordenados (s:list) -> bool:
    for i in range(len(s)-1):
        if not s[i] < s[i+1]:
            return False
    return True

# 1.5)
def palabraLarga (s:list) -> bool:
    for i in s:
        if len(i) > 7:
            return True
    return False

# 1.6)
def esPalindroma (p:str) -> bool:
    i = 0
    while i < (len(p))/2:
        if p[i] != p[len(p)-1-i]:
            return False
        i += 1
    return True

print(esPalindroma('nuen'))