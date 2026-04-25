# Pergunta quantos alunos vieram
quantidade = int(input("Quantos alunos vieram hoje? "))

# Lista para armazenar nome e nota
lista_presenca = []

# Loop para coletar os dados
for i in range(quantidade):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    
    # Guarda nome e nota juntos (lista dentro de lista)
    lista_presenca.append([nome, nota])

# Mostra a lista final
print("\nLista de Presença com Notas:")
for i, aluno in enumerate(lista_presenca, start=1):
    print(f"{i}. Nome: {aluno[0]} | Nota: {aluno[1]}")