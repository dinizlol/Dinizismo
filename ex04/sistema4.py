from ex04.funções4 import *
from ex04.menu import *
cabeçalho('CRIPTOGRAFADOR/DESCRIPTOGRAFADOR'.center(60))
continuar = False
while not continuar:
    chave = validacao()
    while True:
        cabeçalho('OQUE DESEJA FAZER?'.center(60))
        resp = menu(['Utilizar chaves diferentes', 'criptografar uma mensagem', 'descriptografar uma mensagem',
                     'sair do programa'])
        if resp == 1:
            break
        elif resp == 2:
            criptografar(chave)
        elif resp == 3:
            criptografar(chave)
        elif resp == 4:
            break
    if resp == 1:
        continue
    else:
        continuar = True
print('Obrigado por usar esse programa!')








