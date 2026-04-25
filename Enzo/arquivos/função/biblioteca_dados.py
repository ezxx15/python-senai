import faker as apelido

falso_dado = apelido.Faker("pt_BR")

apelido.Faker.seed(1)
for _ in range(100):
    nome = (falso_dado.name())
    print(f"Telefone: {falso_dado.phone_number()}")
    print(f'Endereço: {falso_dado.address()}')
