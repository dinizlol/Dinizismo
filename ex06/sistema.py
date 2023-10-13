from ex06.funções import *
from ex06.menu import *
from time import sleep
# teste1 = chaves()
# print(teste1)
# teste2 = CriptoEspaços('o caminhao é mais rápido que a bicicleta', teste1[-1])
# teste3 = criptografar(teste2, teste1)
#
# print(teste3)


continuar = True
while continuar:
    Chavesfuncao = chaves()
    chavess = list(Chavesfuncao)
    MenuChaves(chavess)
    while True:
        menu('NOVA CHAVE', 'CRIPTOGRAFAR', 'DESCRIPTOGRAFAR', 'SAIR')
        resp = int(input('Oque deseja fazer? '))
        if resp == 1:
            print('Gerando novas chaves...')
            sleep(4)
            break
        if resp == 2:
            texto = str(input('Que frase deseja criptografar? ')).lower()
            espaços = CriptoEspaços(texto, chavess[-1])
            criptografado = criptografar(espaços, chavess)
            symbols = CriptSymbols(criptografado, chavess)
            print(symbols)
        if resp == 3:
            texto = str(input('Que frase deseja descriptografar? ')).lower()
            texto_sespaços = DescriptEspaços(texto, chavess[-1])
            descriptografado = criptografar(texto_sespaços, chavess)
            print(descriptografado)
        if resp == 4:
            linhas('GG')
            continuar = False
            break
        if resp == 0 or resp > 4:
            print('Digite um número entre 1 e 4')









