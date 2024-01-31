# O objetivo deste exercício é criar um jogo simples de perguntas e respostas utilizando a linguagem de programação Python.
# usar while e for e função, nao pode sair com o control c tem q acertar no minimo 4 pergundas

perguntas_respostas = {
    'Qual tag podemos adicionar um texto negrito no html': 'strong',
    'Melhor time do brasil?': 'Corinthians',
    'Qual tag usada para o menu superior': 'nav',
    'Qual tag podemos adicionar uma imagem no htmal': 'img',
    'Qual tag podemos adicionar um paragrafo no html': 'p',
    'Qual tag podemos adicionar um texto pequeno no html': 'small'}

def jogo():
    pontuacao=0
    for pergunta, resposta in perguntas_respostas.items():
        print(pergunta)
        #print(resposta)
        resposta_usuario=input("Digite a resposta: ")
        if resposta_usuario.lower() == resposta.lower():
            print("Correto!")
            pontuacao += 1
        else:
            print(f"Incorreto! A resposta correta é: {resposta}")

    return pontuacao
    

def keep():
    try:
     while True:
        print("1 para jogar")
        print("2 para sair")
        op=input('Escolha a opção desejada: ')
        if op == '2':
            break
        elif op == '1':
            acertos = jogo()
            if acertos>=4:
                print(f'Parabens!!! vc passou e teve {acertos} acertos')
            else:
                print(f'Não foi dessa vez tente novamente vc só teve {acertos} acertos')
        else:
            print('Opção invalida')
    except KeyboardInterrupt:
        print(" Control+C não pemitido")
        keep()

keep()