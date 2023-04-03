# Criando uma lista vazia para guardar os itens de compra
lista_de_compras = []

# Loop principal que executa até que o usuário escolha sair
while True:
    # Exibe as opções disponíveis para o usuário
    print("\nEscolha uma opção:")
    print("1 - Adicionar item à lista")
    print("2 - Remover item da lista")
    print("3 - Ver lista de compras")
    print("4 - Sair")

    # Pergunta ao usuário qual opção deseja escolher
    opcao = input("> ")

    # Adicionar item à lista
    if opcao == "1":
        item = input("Digite o item que deseja adicionar: ")
        lista_de_compras.append(item)
        print(f"{item} adicionado à lista de compras.")

    # Remover item da lista
    elif opcao == "2":
        item = input("Digite o item que deseja remover: ")
        if item in lista_de_compras:
            lista_de_compras.remove(item)
            print(f"{item} removido da lista de compras.")
        else:
            print(f"{item} não está na lista de compras.")

    # Ver lista de compras
    elif opcao == "3":
        print("\nLista de compras:")
        if lista_de_compras:
            for item in lista_de_compras:
                print("- " + item)
        else:
            print("A lista de compras está vazia.")

    # Sair do programa
    elif opcao == "4":
        print("Saindo...")
        break

    # Opção inválida
    else:
        print("Opção inválida. Tente novamente.")
