def cabeçalho(palavra):
    print('-' * 60)
    print(palavra)
    print('-' * 60)


def menu(lista):
    for i, p in enumerate(lista, start=1):
        print(f'{i} - {p}')
    while True:
        print('-' * 60)
        n = int(input('Digite uma opção:'))
        if n > 4:
            print('Opção invalida: digite 1, 2, 3 ou 4.')
        else:
            return n

