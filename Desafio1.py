menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 2

while True:
    
    opcao = input(menu)
    
    if opcao == 'd':
        valor = float(input('Digite o valor a ser depositado: ').replace(',','.'))
        if valor > 0:
            resumo = f'Desposito: R${valor}\n'
            extrato += resumo 
            saldo += valor
            print('Valor depositado com sucesso!')
        else:
            print('Valor Incorreto Tente novamente!\n')
    
    elif opcao == 's':
        print('Saque')
        if numero_saques > limite_saques:
            print('Limite de saque atingido!')
        elif saldo <= 0:
            print('Saldo indisponivel!')
        else:
            valor_saque = float(input('Informe o valor desejado: ').replace(',','.'))
            if valor_saque > 500:
                print('Limite de R$500 por saque!')
            elif valor_saque > saldo:
                print('Saldo indisponivel!')
            else:
                numero_saques += 1
                resumo = f'Saque: R${valor_saque}\n'
                extrato += resumo
                saldo -= valor_saque
                print(f'Saque:{valor_saque}')
    
    elif opcao == 'e':
        print('Extrato')
        print(f'{extrato}\nSaldo Disponivel R$:{saldo}')
    
    elif opcao == 'q':
        break
    
    else:
        print('Operação invalida, por favor selecione novamente a opção desejada')
