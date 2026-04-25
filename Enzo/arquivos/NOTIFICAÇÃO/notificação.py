import requests

nome = input("Qual o seu nome? ")
topico = "labubu" # Peça o tópico para o seu colega!
url = f"https://ntfy.sh/{topico}"

mensagem = f"O {nome} mandou um beijo na xrc"

requests.post(url, data=mensagem.encode('utf-8'))

print(f"Salve enviado para {topico}!")