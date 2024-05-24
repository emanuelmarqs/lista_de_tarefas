
#lista vazia
tarefas = []

#laço de repetição - para quando não sei quantos itens terão a lista.
while True:
    #usuário informa os itens da lista de tarefas
    nova_tarefa = input('Informe a nova tarefa ou deixe vazio para encerrar e exibir a lista: ')

    #verifica se o usuário inseriu uma nova tarefa
    if nova_tarefa != '':  #se a tarefa for diferente de vazio ele continua o loop
        tarefas.append(nova_tarefa) #adiciona a nova tarefa à lista
        continue
    else:     #se não
        break #o loop será finalizado

#exibe a lista de tarefas
for tarefa in tarefas:
    print(tarefa)