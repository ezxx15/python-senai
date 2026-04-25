# autor: Enzo
# projeto: Cópia de listas

# Em python as listas são um recursos muito poderoso mas todo poder 
# traz responsabilidades, vamos ver um efeito colateral ao cópiar
# uma lista

L = [1 , 2 , 3 , 4 , 5]

V = L

print("essa é a lista L: " , L)
print("essa é a lista V: " , V)

V[0] = 6

print("Esta é a lista V modificada: ", V)
print("Esta é a lista L modificada: ", L)

L = [1 , 2 , 3 , 4 , 5]
V = L [:]
V[0] = 6

print("Esta é a lista V modificada: ", V)
print("Esta é a lista L modificada: ", L)
