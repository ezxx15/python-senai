# criando lista vazia
lista = []
# criando lista com a função List()
lista_com_funcao = list ()
# lista de valores heterogêneos
aleatorio = [2 , "a" , 5.44, True]

# lista de notas
notas = [0] * 7
soma = 0
x = 0

# entrada das 7 notas
while x < 7:
 notas[x] = float(input(f'Nota {x}: '))
 soma += notas[x]
 x += 1

x = 0

while x < 7:
   print(f'Nota {x}: {notas[x]:.2f}')
   x += 1

   print(f"Média: {soma / 7:.2f}")



