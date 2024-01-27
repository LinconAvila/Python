empresas = ['ALB','MM','CZB']
porcentagem = [10 , 8 , 5]
codigos = [1,2,3,4,5,6,0]
usuarios = []
saldos = []
while True:
    print('1 - Cadastrar Empresa\n2 - Cadastrar Usuário\n3 - Registrar Compra de um Usuário\n4 - Mostrar Saldo de um Usuário\n5 - Resgatar Saldo de um Usuário\n6 - Excluir Empresa\n0 - Sair ')    
    cod = input('Olá, digite o código referente ao que deseja realizar: ')
    try:
        cod = int(cod)
    except ValueError:
        print('Código inválido, tente novamente!')
    else:
        if cod not in codigos:
            print('Código inválido, tente novamente.')
        else:
            if cod == codigos[6]:
               saida = input('Você tem certeza que deseja sair? ')
               saida_upper = saida.upper()
               if saida_upper == 'SIM':
                  print('Ok, finalizando o programa!')
                  break
               else:
                  print('Ok, retornando ao menu!')
    if cod == codigos[0]:
        print('Bem-vindo(a) a seção de cadastramento de empresas!')
        while True:
            id_empresa = input('Digite o ID da empresa que deseja cadastrar (ou "sair" para voltar ao menu): ')
            id_empresa_upper = id_empresa.upper()
            if id_empresa.isdigit():
                print('Nome de empresa inválido, somente números não é permitido. Tente novamente.')
                continue
            elif id_empresa_upper == 'SAIR':
                break
            elif id_empresa_upper in empresas or id_empresa in usuarios:
               print('Empresa já cadastrada, tente novamente.')
               continue
            elif not id_empresa_upper:  # Verifica se o ID da empresa é vazio
                print('Nome de empresa inválido, tente novamente.')
                continue
            porcentagem_cashback = float(input('Digite a porcentagem, somente o número, de cashback oferecida pela empresa (ex.:8): '))
            empresas.append(id_empresa_upper)
            porcentagem.append(porcentagem_cashback)
            print('Empresa cadastrada com sucesso')
    elif cod == codigos[1]:
        print('Bem-vindo(a) a seção de cadastramento de usuários!')
        while True:
            id_usuario = str(input('Digite o ID de usuário que deseja cadastrar (ou "sair" para voltar ao menu): '))
            id_usuario_lower = id_usuario.lower()
            id_usuario_upper = id_usuario.upper()
            if id_usuario.isdigit():
                print('Nome de usuário inválido, somente números não é permitido. Tente novamente.')
                continue
            elif id_usuario_lower == 'sair':
                break
            elif id_usuario_lower in usuarios or id_usuario_upper in empresas:
                print('Usuário já cadastrado, tente novamente!')
                continue
            usuarios.append(id_usuario_lower)
            saldos.append(0.0)
            print('Usuário cadastrado com sucesso!')
    elif cod == codigos[2]:
        print('Bem-vindo(a) ao registro das compras!')
        while True:
            id_usuario2 = input('Digite seu ID de usuário (ou "sair" para voltar ao menu):')
            id_usuario2_lower = id_usuario2.lower()
            if id_usuario2_lower == 'sair':
                break
            if id_usuario2_lower not in usuarios:
                print('Usuário não encontrado, tente novamente.')
                continue
            valor_compra = float(input('Digite o valor da compra:'))
            local_compra = input('Digite o ID do local onde a compra foi realizada:')
            local_compra_upper = local_compra.upper()
            if local_compra_upper in empresas:
               indice_local_compra = empresas.index(local_compra_upper)
               desconto = valor_compra * (porcentagem[indice_local_compra]/ 100)
               saldo_indice = usuarios.index(id_usuario2)
               saldos[saldo_indice] += desconto
               print(f'Compra registrada!\nCashback de R${desconto:.2f} adicionado ao seu saldo.')
            else:
               print('Empresa não encontrada, tente novamente.')
    elif cod == codigos[3]:
        print('Seja bem-vindo(a) a seção de saldos de usuários!')
        while True:
            id_usuario3 = input('Digite o seu ID de usuário (ou "sair" para voltar ao menu):')
            id_usuario3_lower = id_usuario3.lower()
            if id_usuario3_lower == 'sair':
                break
            if id_usuario3 not in usuarios:
               print('Usuário não encontrado!')
            else:
               usuario_indice = usuarios.index(id_usuario3)
               print(f'O seu saldo atual é R${saldos[usuario_indice]:.2f}')
    elif cod == codigos[4]:
        print('Seja bem-vindo(a) a seção de resgate dos saldos dos usuários!')
        while True:
            id_usuario4 = input('Digite o ID do usuário (ou "sair" para voltar ao menu):')
            id_usuario4_lower = id_usuario4.lower()
            if id_usuario4_lower == 'sair':
                break
            if id_usuario4 not in usuarios:
               print('Usuário não encontrado!')
            else:
               usuario_indice = usuarios.index(id_usuario4)
               print(f'O seu saldo atual é R${saldos[usuario_indice]:.2f}')
               valor_saque = input('Digite o valor que você deseja trasferir:')
               try:
                   valor_saque = float(valor_saque)
               except ValueError:
                   print('Você nâo digitou um valor real, tente novamente.')
               confirmar = str(input('Tem certeza que deseja resgatar o saldo? '))
               confirmar_upper = confirmar.upper()
               if confirmar_upper == 'SIM':
                  novo_saldo = saldos[usuario_indice] - valor_saque
                  print(f'O dinheiro foi transferido e o novo saldo é de R$ {novo_saldo:.2f}')
    elif cod == codigos[5]:
        print('Seja bem-vindo(a) a seção de exclusão de empresas')
        while True:
            empresa_excluir = str(input('Digite o ID da empresa que deseja excluir (ou "sair" para voltar ao menu): '))
            empresa_excluir_upper = empresa_excluir.upper()
            if empresa_excluir == 'sair':
                break
            elif empresa_excluir_upper not in empresas:
               print('Empresa não encontrada!')
            else:
               confirmar_exclusao = str(input(f'Essa ação pode ser irreversível, tem certeza que deseja excluir a empresa {empresa_excluir_upper}? '))
               confirmar_exclusao_upper = confirmar_exclusao.upper()
               if confirmar_exclusao_upper == 'SIM':
                  empresas.remove(empresa_excluir_upper)
                  print('Empresa excluída com sucesso!')
               else:
                  print(f'A empresa {empresa_excluir} não foi excluída!')

