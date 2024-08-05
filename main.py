# entrada  de dados inicio da lista!
lista_tarefas = []

# inicio do loop
while True:
    # menu de escolha do usuário
    print('\n1 - Adicionar tarefa. ')
    print('2 - Exibir tarefas da lista. ')
    print('3 - Encerrar o Programa. ')

    # opção do usuário
    tarefa = input('\nDigite uma opção: ')

    # verifica a opção dititada
    match tarefa:
        case '1':
            nova_tarefa = input('Insira a tarefa para incluir na lista: ').capitalize()
            lista_tarefas.append(nova_tarefa)
            print(f'\n{nova_tarefa} inserido na lista!\n')
            continue
        case '2':
            print('\n Lista de Tarefas!\n')
            for lista in lista_tarefas:
                print(f'{lista}.')
            continue
        case '3':
            print('\nPrograma Encerrado!')
            break
        case _:
            print('Opção Inválida!')