Agenda = [] #Recebe uma lista vazia

def add_contato(nome, numero): #funcao para adicionar os contatos
    if verificar_contato(numero):
        print(f'O contato já existe na Agenda')
    else:
        novo_contato = {
            'nome': nome,
            'numero': numero
        }

        Agenda.append(novo_contato)
        print('O contato foi adicionado')

def atualizar_arquivo_nome(nome, Agenda):
    for contato in Agenda:
        if contato['nome'] == nome:
            n_nome = input(f'Escreva o novo nome para o contato {nome}: ')
            contato['nome'] = n_nome  
            print('O nome do contato foi atualizado')

def atualizar_arquivo_numero(numero, Agenda):
    for contato in Agenda:
        if contato['numero'] == numero:
            n_numero = input(f'Escreva o novo número para o contato {numero}: ')
            contato['numero'] = n_numero
            print('O número do contato foi atualizado')

def verificar_contato(numero):
    for contato in Agenda:
        if contato['número'] == numero:
            return True
    return False

def ordenar_agenda(agenda):
    if len(agenda) > 2:
        for i in range(1, len(agenda)):
            contador = i
            while agenda[contador]['nome'] < agenda[contador-1]['nome'] and contador > 0:
                agenda[contador-1], agenda[contador] = agenda[contador], agenda[contador-1]
                contador -= 1
    exibir_agenda(agenda)

def exibir_agenda(agenda):
    print('TODOS OS CONTATOS:')
    print('*'*20)
    print(f'NOME: --- Número ')
    for contato in agenda:
        print(f'| {contato["nome"].title()} --- {contato["número"]} |')

'''def apagar_por_contato(Agenda,nome):
    for i in Agenda:
        if Agenda['nome'] == nome:
            del Agenda[i]
            print(f' O seu contato foi apagado com sucesso')'''
            


try:
    while True:
        print('Escolha:')
        print('1º -Ver contatos \n2º-Adicionar contatos \n3º-Atualizar dados de um Contato \n4º -Apagar contato \n5°-Sair')
        resultado = input('O que você quer acessar? (escreva o número específico)\n ')
        if resultado == '1':
            exibir_agenda(Agenda)
        elif resultado == '2':
            n_nome = input('Digite o nome que você quer adicionar: ')
            n_numero = input('Digite o número que você quer adicionar (11 dígitos contando o DDD): ')
            add_contato(n_nome, n_numero)
            ordenar_agenda(Agenda)
        elif resultado == '3':
            escolha = input('Você quer atualizar o nome ou o número? (nome ou numero)').lower()
            if escolha == 'nome':
                nome = input('Qual nome você quer atualizar?')
                atualizar_arquivo_nome(nome, Agenda)
            else:
                numero = input('Qual número você quer atualizar? ')
                atualizar_arquivo_numero(numero, Agenda)
            ordenar_agenda(Agenda)
        elif resultado =='4':
            #nome = input('Qual contato em especifico você quer apagar?')
            #apagar_por_contato(Agenda,nome)
            print('Opção está em implementação. Volte mais tarde!')
        elif resultado == '5':
            print('Obrigado por vir')
            break
        else:
            print('Opa, essa opção não existe :(')
except :
    print('Erro no menu')