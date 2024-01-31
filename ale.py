def adicionar_tarefas(lista_tarefas, mensagem="digite a nova tarefa: "):
    while True:
        nova_tarefa = input(mensagem)

        if nova_tarefa.strip() != "":
            lista_tarefas.append(nova_tarefa)
            print(f"Tarefa '{nova_tarefa}' adicionado com sucesso")

            continuar = input("Deseja adicionar outra tarefa: (S/N): ").lower()
            if continuar != 's':
                break
        else:
            print("Por favor, insira uma tarefa válida")

lista_de_tarefas = []

adicionar_tarefas(lista_de_tarefas, "insira a tarefa: ")

print("lista de tarefas")
for i in range(len(lista_de_tarefas)):
    tarefa = lista_de_tarefas[i]
    print(f"{i +1}. {tarefa}")