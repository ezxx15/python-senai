# autor: Enzo
# projeto: fazer uma função que indica que o número é par 

numero = int(input('insira o número: '))

def ehpar (numero):
   print ('o numero digitado é par? \n', numero % 2 == 0)

(ehpar(numero))

def par_ou_impar (valor):
   if valor  % 2 == 0:
      print('o numero é par')
   else:
      print('o numero é impar')
par_ou_impar(numero)