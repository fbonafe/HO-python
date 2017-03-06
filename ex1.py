# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a = range(1,1000)
mults = []
for i in a:
    if i % 3 == 0 or i % 5 == 0:
        mults.append(i)
print('Resultado 1 = {}'.format(sum(mults)))

fib0 = 1
fib1 = 1
suma = 0
while fib1 < 4000000: #Para Euler Project es 4 millones, el ejercicio era 1 millon
    if fib1 % 2 == 0: # Para euler eran pares, en el ejercicio eran impares
        suma += fib1
    aux = fib0 + fib1
    fib0 = fib1
    fib1 = aux
print('Resultado 2 = {}'.format(suma))

def factor(a):
    i=2
    while i<a:
        if (a % i == 0):
            break
        i += 1
    return a/i, i

n0 = 600851475143
n = n0
fact = [1]
i = fact[0]
while i < n:
    n, i = factor(n)
    fact.append(i)
#print(fact)
#prod = 1
#for f in fact:
#    prod = prod * f
#print(prod-n0)
print('Resultado 3 = {}'.format(max(fact)))

