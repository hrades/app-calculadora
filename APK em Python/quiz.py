
acertos = 0
erros = 0
#Perguntas do Quiz
print('Pergunta 1: Onde nasceu Salvador Arena? \nDigite: \n[1]Brasil\n[2]Estados Unidos\n[3]Libia')
p1 = int(input('Resposta: '))
print("\x1b[2J\x1b[1;1H") #função para limpar o terminal

print('''Pergunta 2: Qual o nome da primeira empresa fundada por Salvador Arena? \nDigite:
[1]Light\n[2]Termomecanica\n[3]Fundacao Salvador Arena''')
p2 = int(input('Resposta: '))
print("\x1b[2J\x1b[1;1H")

print('''Pergunta 3: Qual faculdade Salvador Arena se formou? \nDigite:
[1]USP\n[2]Faculdade Termomecanica\n[3]UNICAMP''')
p3 = int(input('Resposta: '))
print("\x1b[2J\x1b[1;1H")

#Comparativos que avaliam as respostas
if p1 == 3:
    acertos+=1
else:
    erros+=1
if p2 == 2:
    acertos+=1
else:
    erros+=1
if p3 == 1:
    acertos+=1
else:
    erros+=1

#Confere os acertos e erros e imprime uma mensagem de acordo com eles
if acertos == 3:
    print('\nParabéns! Você acertou todas as perguntas')
elif acertos == 2 or acertos == 1:
    print(f'\nVocê errou {erros} perguntas. \nAs perguntas foram:')
    if p1 != 3:
        print('A pergunta 1. ', end='')
    if p2 != 2:
        print('A pergunta 2. ', end='')
    if p3 != 1:
        print('A pergunta 3')
else:
    print(f'\nQue pena! Você teve {erros} erros')