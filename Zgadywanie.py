import random

def generuj_szyfr(n):
return [random.randint(0,9) for _ in range(n)]

def sprawdzam(code,guess):
exact = sum(c == g for c, g in zip(code,guess))
partial = sum(min(code.count(x), guess.count(x)) for x in set(guess)) - exact
return exact,partial
"""
Praca w toku
"""