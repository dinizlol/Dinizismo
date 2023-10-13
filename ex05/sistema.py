from ex05.funções import *
from ex05.menu import *
from time import sleep

continuar = False
while not continuar:
    while True:
        palavra1 = str(input('Digite uma chave: '))
        chave1 = ChecarEspacos(palavra1)
        if chave1:
            while chave1:
                palavra2 = str(input('Digite a segunda chave: '))
                chave2 = ChecarEspacos(palavra2)
                if chave2:
                    chaves = ChecarLen(chave1, chave2)
                    if chaves:
                        while chaves:
                            linhas('CRIPTOGRAFADOR/DESCRIPTOGRAFADOR')
                            menu('DIGITAR NOVAS CHAVES', 'CRIPTOGRAFAR UMA MENSAGEM', 'DESCRIPTOGRAFAR UMA MENSAGEM',
                                 'SAIR DO PROGRAMA')
                            resp = int(input('Qual opção deseja fazer? '))
                            if resp == 1:
                                chaves = ''
                                chave1 = ''
                                chave2 = ''
                            elif resp == 2:
                                n = Criptografar(chaves)
                                print(n)
                            elif resp == 3:
                                n = Criptografar(chaves)
                                print(n)
                            elif resp == 4:
                                continuar = True
                                chaves = ''
                                chave1 = ''
                                chave2 = ''
                                linhas('OBRIGADO POR USAR ESTE PROGRAMA!')
                                break
                            elif resp == 0 or resp > 4:
                                print('Digite um número entre 1 e 4.')
                            sleep(3)
        break





