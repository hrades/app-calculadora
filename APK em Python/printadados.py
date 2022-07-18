from datetime import datetime

print('Ola! Bem-vindo ao teste')
nome = str(input('Digite seu nome: '))
print("\x1b[2J\x1b[1;1H")
idade = int(input('Digite sua idade: '))
print("\x1b[2J\x1b[1;1H")
mes = int(input('Digite o mês de nascimento(número): '))
print("\x1b[2J\x1b[1;1H")

meses = {1:'janeiro', 2:'fevereiro', 3:'março', 4:'abril', 5:'maio', 6:'junho', 7:'julho', 8:'agosto', 9:'setembro', 10:'outubro', 11:'novembro', 12:'dezembro'}
ano = int(datetime.today().strftime('%Y'))
meshoje = int(datetime.today().strftime('%m'))

if mes <= meshoje:
    ano = ano-idade
else:
    ano = ano-(idade+1)
print(f'Seu nome é {nome}, você tem {idade} anos e nasceu em {meses[mes].capitalize()} de {ano}')