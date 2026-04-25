# escrever em file

'''
Comando para ler e escrever arquivos

with open(file="caminho do arquivo", mode='Modo de leitur ou Escrita',
    encoding='decodificador') as apelido:
        bloco de código
'''

'''
O modo de escrita - W
O modo de leitura - R
O modo de acrescimo - A
'''
nome_do_arquivo = "pepsico.txt"

with open(file=nome_do_arquivo, mode="w", encoding='utf8') as arquivos:
    print(f'''Em 1992 nas filipinas ocorreu o incidente 349, umas promoção da empresa pepsi se tornou 
          um desastre, tampinhas premidas com numeros diarios, resultariam em um
          grande premio. em 25 maio, o numero 349 foi anunciado como vencedor, mas um erro de programação
          fez com que inumeras tampinhas tivessem esse numero''', file=arquivos)
