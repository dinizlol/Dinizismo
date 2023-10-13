def linhas(mensagem):
    print('\/' * 20)
    print(mensagem.center(40))
    print('\/' * 20)

def menu(*palavras):
    print(':><:' * 20)
    for c, palavra in enumerate(palavras, start=1):
        print(c, '  <>  ', palavra)
    print(':><:' * 20)



def MenuChaves(chaves):
    from time import sleep
    print(':/\:' * 15 )
    print('SUAS CHAVES'.center(60))
    for c, chave in enumerate(chaves, start=1):
        print(chave, end=' >< ')
    print()
    print(':/\:' * 15)
    sleep(2)
