def linhas(mensagem):
    print('><' * 20)
    print(mensagem.center(40))
    print('><' * 20)

def menu(*palavras):
    for c, palavra in enumerate(palavras, start=1):
        print(c, end='  -  ')
        print(palavra)
    print('><' * 20)
    print('><' * 20)


