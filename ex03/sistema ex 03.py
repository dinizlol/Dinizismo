from ex03.funções import *
from ex03.menu import *
cabeçalho('CRIPTOGRAFADOR/DESCRIPTOGRAFADOR'.center(60))
continuar = False
while not continuar:
    chave = validacao('Digite a primeira chave: ')
    while True:
        cabeçalho('OQUE DESEJA FAZER?'.center(60))
        resp = menu(['Utilizar chaves diferentes', 'criptografar uma mensagem', 'descriptografar uma mensagem',
                     'sair do programa'])
        if resp == 1:
            break
        elif resp == 2:
            criptografar(chave)
        elif resp == 3:
            descriptografar(chave)
        elif resp == 4:
            break
    if resp == 1:
        continue
    else:
        continuar = True
print('Obrigado por usar esse programa!')








