def funcao_add(entrada_tarefa):
    tarefas.append(entrada_tarefa)

tarefas = []

while (True):
    print("1 - Para adicionar tarefas")
    print("2 - Para exibir tarefas")
    print("3 - Para sair")
    op = input("Entre com o numero")
    ##try
    if (op=="3"):
     break  
    if(op=="1"):
        elem = input("Digite uma tarefa")
        funcao_add(elem)
    
    if(op=="2"):
       for i in range(len(tarefas)):
          print(tarefas[i])
