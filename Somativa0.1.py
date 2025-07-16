# programa para gerenciamento pessoal de ingressos

# Mensagem de boas-vindas
print("Bem-vindo ao gerenciador de ingressos!🎟️")

# Lista de filmes disponíveis, cada um com nome, ano e gênero
filmes = [
    {"nome": "Como Treinar seu Dragão", "ano": 2025, "genero": "Aventura/Fantasia"},
    {"nome": "F1", "ano": 2025, "genero": "Ação/Esporte"},
    {"nome": "Smurfs", "ano": 2025, "genero": "Animação/Aventura"},
    {"nome": "Superman", "ano": 2025, "genero": "Ação/Ficção Científica"}
]

# Lista para armazenar os ingressos registrados pelo usuário
meus_ingressos = []

# Loop principal do programa
while True:
    # Pergunta ao usuário se deseja incluir um novo ingresso
    resposta = input("Deseja incluir um novo registro de ingresso? (Sim/Não): ")
    # Valida a resposta, só aceita 'Sim', 'sim', 'Não', 'nao', 'Nao', 'não'
    while resposta not in ["Sim", "sim", "Não", "nao", "Nao", "não"]:
        print("Tente novamente, sua resposta está inválida.")
        print("Por favor, responda com 'Sim' ou 'Não'.")
        resposta = input("Deseja incluir um novo registro de ingresso? (Sim/Não): ")
    # Se a resposta for negativa, encerra o programa
    if resposta in ["Não", "nao", "Nao", "não"]:
        print("Obrigado por usar o gerenciador de ingressos, Mangecine! Até logo! 👋")
        break

    # Exibe a lista de filmes disponíveis com seus dados
    print("\n🎥Filmes disponíveis:")
    for i, filme in enumerate(filmes, 1):
        print(f"{i}. {filme['nome']} ({filme['ano']}) - {filme['genero']}")
    print()

    # Solicita ao usuário o nome exato do filme para registrar o ingresso
    escolha = input("Digite o nome exato do filme que deseja registrar: ")
    # Cria uma lista apenas com os nomes dos filmes para validação
    nomes_filmes = [filme['nome'] for filme in filmes]
    # Enquanto o nome digitado não estiver na lista, pede novamente
    while escolha not in nomes_filmes:
        print("Tente novamente, sua resposta está inválida.")
        print("Filme não encontrado. Por favor, verifique o nome e tente novamente.")
        escolha = input("Digite o nome exato do filme que deseja registrar: ")

    # Adiciona o ingresso à lista de ingressos do usuário
    meus_ingressos.append(escolha)
    # Mostra a lista atualizada de ingressos
    print("\nSeus ingressos atualizados:")
    for ingresso in meus_ingressos:
        print(f"- {ingresso}")
    print()

# Espaçamento visual para o formulário de satisfação
print("="*40)
# Pergunta de satisfação ao usuário
satisfacao = input("Como você avalia o nosso serviço? (1-5): ")
# Valida a resposta, só aceita números de 1 a 5
while satisfacao not in ["1", "2", "3", "4", "5"]:
    print("Tente novamente, sua resposta está inválida.")
    print("Por favor, responda com um número de 1 a 5.")
    satisfacao = input("Como você avalia o nosso serviço? (1-5): ")
# Agradece pela avaliação
print(f"Obrigado pela sua avaliação! Você deu nota {satisfacao} ao nosso serviço.")
# Exibe um versículo bíblico
print('Versiculo do dia:')
print('“E conhecereis a verdade, e a verdade vos libertará.” - João 8:32')
print("="*40)

