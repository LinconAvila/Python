#Define 3 listas: para os códigos, produtos e preços
codigos = [10, 20, 21, 30, 45]
nomes = ["Caderno pautado", "Caneta azul", "Caneta vermelha", "Borracha", "Lápis macio"]
precos = [10.00, 3.00, 3.00, 2.00, 1.00]
#Inicia um loop para rodar o programa indefinidamente, define uma lista vazia para o pedido do cliente, requisita do usuário o nome do cliente
while True:
    pedido = []
    nome_cliente = input("Digite o nome do cliente (ou 'sair' para encerrar): ")
#Se o usuário digitar sair, o programa encerra
    if nome_cliente == 'sair':
        break
#Cria um loop infinito para o usuário digitar o código do produto e sua respectiva quantidade, exibindo um menu com os códigos, produtos e preços    
    while True:
        for i in range(len(codigos)):
            print(f"{codigos[i]} - {nomes[i]} - R${precos[i]:.2f}")
        codigo = int(input("Digite o código do produto (0 para finalizar a compra): "))
#Se o código digitado for zero, o loop acaba e o programa exibe o total da compra
        if codigo == 0:
            break
#Se o código não estiver na lista, exibe uma mensagem de erro e requisita ao usuário digitar o código novamente
        if codigo not in codigos:
            print("Código inválido. Tente novamente.")
#Caso contrário, requisita a quantidade do produto e adiciona as informações a lista do pedido           
        else:
            quantidade = int(input("Digite a quantidade: "))
            item_pedido = (codigo, quantidade)
            pedido.append(item_pedido)
#Imprime o nome do cliente
    print(f"\nCliente: {nome_cliente}")
    total = 0
#Inicia um loop for em relação a lista 'pedido' e armazena as informações em diferentes variáveis, realiza a soma total e depois as imprime no formato requisitado
    for item in pedido:
        codigo = item[0]
        quantidade = item[1]
        indice = codigos.index(codigo)
        preco_unitario = precos[indice]
        preco_total = preco_unitario * quantidade
        total = total + preco_total
        print(f"{preco_total:.2f} {quantidade:02d} x {nomes[indice]}")
    print("-----------")
    print(f"{total:.2f} valor total")
    print("\n")
#Exibe uma mensagem de encerramento do programa
print("Encerrando o programa.")
