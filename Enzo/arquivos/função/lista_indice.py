# autor: Enzo
# projeto: trabalhando com indices
# programar um lê cinco números e armazenar em uma lista e depoois
#  solicita ao usuario que escolha um número a mostrar

números = [0] * 5
x = 0

while x <5:
    números[x] = int ( input (f"Número {x + 1}"))
    x = x + 1
    
    
while True :
    escolhido = int( input ("Que posição você quer imprimir (0 para sair)"))

    if escolhido == 0:
        break
    print(f" Você escolheu o número: {números[escolhido - 1]}")