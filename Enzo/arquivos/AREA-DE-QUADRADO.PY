def obter_valores():
    "Solicita ao usuário os valores do dólar e do real."
    dolar = float(input('Digite o valor do dólar hoje: '))
    real = float(input('Qual o valor em real que deseja converter: '))
    return dolar, real

def converter_para_dolar(real, dolar):
    "Converte o valor em real para dólares."
    return real / dolar

def mostrar_resultado(valor_em_dolar):
    "Exibe o valor convertido com duas casas decimais."
    print(f'Valor convertido para dólar U$: {valor_em_dolar:.2f}')
    print(f'Valor em dólares: US$ {valor_em_dolar:.2f}')

# Programa principal
dolar, real = obter_valores()
valor_em_dolar = converter_para_dolar(real, dolar)
mostrar_resultado(valor_em_dolar)