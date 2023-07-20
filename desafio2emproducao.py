menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar Usuário
[c] Criar Conta
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
users = {}
conta = {}
num_conta = 0
agencia = '0001'

def cad_users(cpf,/):
    nome = input('Nome: ')
    dt_nascimento = input('Data de Nascimento: ')
    rua = input('Rua: ')
    numero_rua = input('Numero: ')
    bairro = input('Bairro: ')
    cidade = input('Cidade: ')
    estado = input('Estado: ')
    users[cpf] = {'Nome':nome,'Data de Nascimento: ':dt_nascimento,'Rua: ':rua,'Numero: ':numero_rua,'Bairro: ':bairro,'Cidade: ':cidade,'Estado: ':estado}
    return users

def criar_conta(*,conta,num_conta):
    global users
    #global num_conta
    AG = agencia
    num_conta += 1  
    usuario = input('CPF: ')
    if usuario in users:
        conta[num_conta] = {'Agencia':AG,'Cliente: ':usuario}
        print(f'Conta: {num_conta} foi criada com sucesso!' )
        return (conta,num_conta)
    else:
        print('CPF não encontrado!')

#def listar_contas():

def depositar(valor,saldo,extrato,/):
    if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return (saldo, extrato)

def sacar(*,saldo,valor,extrato,limite,numero_saques,LIMITE_SAQUES):
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        
    else:
        print("Operação falhou! O valor informado é inválido.")

    return (saldo, extrato,numero_saques)    

def rel(saldo,/,extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

    

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(valor,saldo,extrato)
    
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = sacar(saldo=saldo,valor=valor,extrato=extrato,limite=limite,numero_saques=numero_saques,LIMITE_SAQUES=LIMITE_SAQUES)
        
    elif opcao == 'u':
        cpf = input('Informe o CPF: ').replace('.','')
        cpf.replace('-','')
        if int(cpf) in users:
            print('CPF ja cadastrado!')
        else:
            users = cad_users(cpf)
    
    elif opcao == 'c':
        conta,num_conta = criar_conta(conta=conta,num_conta=num_conta)

            

    elif opcao == "e":
        rel(saldo,extrato=extrato)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
