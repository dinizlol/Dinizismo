def validacao():
    vezes = 1
    lista = []
    while vezes != 3:
        continuar = False
        while not continuar:
            n = str(input(f'Digite a {vezes}ª chave: ')).strip()
            cont = 0
            if n.count(' ') > 0:
                print('Digite apenas uma palavra.')
                break
            for letra in n:
                if n.count(letra) > 1:
                    print('A palavra não pode conter letras iguais.')
                    break
                else:
                     cont += 1
                     if cont == len(n): #como poderia melhorar isso?
                        lista.append(n)
                        vezes += 1
                        continuar = True
                        if len(lista) == 2:
                            if len(lista[0]) != len(lista[1]):
                                print('As palavras devem ter o mesmo número de letras.')
                                vezes -= 1
                                del lista[-1]
                            else:
                                for c, letras in enumerate(lista[0]):
                                    if letras == lista[1][c]:
                                        print('As chaves tem letras iguais na mesma posição.')
                                        vezes -= 1
                                        del lista[-1]
                                        break
                                    else:
                                        if c+1 == len(lista[1]):
                                            return lista



def criptografar(chaves):
    from time import sleep
    texto = str(input('Digite uma frase para criptografar: '))
    for letras in texto:
        found = False
        for chave in chaves:
            for c, l in enumerate(chave):
                if l == letras:
                    print(chaves[0 if chaves.index(chave) == 1 else 1][c], end='')
                    found = True
                    break
            if found:
                break
        if not found:
            print(letras, end='')
    print('')
    sleep(3)










