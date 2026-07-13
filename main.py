# Dicionário de filmes:
#     - Dicionário vazio entre [] para registro pelo usuário.

dicionario_filmes=[]

# Funções:

# Função - Menu:

def menu():
    print("""
    _______________________________________
    
    ●●●                    ツ MyMoveList ツ  
    _______________________________________

    ▶ 1 - Listar um filme e classficar.
    ▶ 2 - Exibir todos os filmes listados.
    ▶ 3 - Sair.
    _______________________________________
    """)

    opc=input("\n ● Digite uma opção (1-3): ")
    return opc

# Função - Registrar um filme e classificar:
#   - A função utiliza input para o usuário digitar o filme, diretor e review;

def registrar():
    filme_registro=input("\n ➜ Registre o nome do filme: ")
    diretor_registro=input(" ➜ Registre o nome do diretor: ")
    review_registro=input(" ➜ Escreva sua review: ")
    classificar_registro=int(input(" ➜ Digite um número de 0 a 5, essa será a quantidade de estrelas do filme: "))
    estrelas_classificar=("★"*classificar_registro)

#   - O que o usuário digitar será registrado na lista "infos" e adicionado em dicionário_filmes (que está vazio).

    infos={
    "filme":filme_registro,
    "diretor":diretor_registro,
    "review":review_registro,
    "estrelas":estrelas_classificar
    }
    
#   - append é utilizado para adicionar a lista no dicionário vazio (não pode ser utilizado como função em dicionários).
#   - No fim há um print que exibe o filme registrado pelo usuário.
#   - Há um if/else para tratamento de informação. Caso o usuário digite uma nota menor do que 0 and maior que 6 será mostrado uma mensagem de erro.

    dicionario_filmes.append(infos)
    
    if classificar_registro<6 and classificar_registro>0:
        print(f"\n ✷ {filme_registro} adicionado a sua lista! ✷")
    else:
        print(" ✷ Erro! Digite um número de 0 a 5!")

# Função - Exibir todos os filmes registrados
#   - Utiliza o for para ler o dicionário constatemente e exibir os registros (pois nosso dicionário está vazio).

def exibir():
    for filmes in dicionario_filmes:
        print(f"""
    _______________________________________
              
    ●●●             Seus últimos registros:
    _______________________________________
        
    ▶ Filme: {filmes['filme']}
    ▶ Diretor: {filmes['diretor']}
    ▶ Review: {filmes['review']}
    ▶ Estrelas: {filmes['estrelas']}
    _______________________________________
    """)

# Função - Sair

def sair():
    print("\n ✷ Volte sempre!✷")

# Seleção

while True:
    opcs=menu()
    if opcs=="1":
        registrar()
    elif opcs=="2":
        exibir()
    elif opcs=="3":
        sair()
        break
    else:
        print("\n ✷ Erro! Digite uma opção válida.")