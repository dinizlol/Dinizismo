def validacao(palavra):
    while True:
        n = str(input(palavra))
        palavra1 = list(n)
        continuar = False
        if len(palavra1) == 5:
            while not continuar:
                n2 = str(input('Digite a segunda chave:  '))
                palavra2 = list(n2)
                if len(palavra1) != len(palavra2):
                    print('Não possui o mesmo número de letras.')
                else:
                    for um in range(0, 5):
                        if palavra1[um] == palavra2[um]:
                            print(f'As palavras possuem letras iguais na mesma posição.')
                            break
                        else:
                            if um == 4:
                                continuar = True
        else:
            print('A palavra não possui 5 letras.')
            continue
        break
    criptografia = list()
    palavra1 = ''.join(palavra1)
    palavra2 = ''.join(palavra2)
    criptografia.append(palavra1)
    criptografia.append(palavra2)
    return criptografia

def criptografar(lista):
    n = str(input('Digite uma frase para ser criptografada: '))
    n = n.split()
    for p in n:
        print(end=' ')
        for l in p:
            if l == lista[0][0]:
                l = lista[1][0]
            elif l == lista[0][1]:
                l = lista[1][1]
            elif l == lista[0][2]:
                l = lista[1][2]
            elif l == lista[0][3]:
                l = lista[1][3]
            elif l == lista[0][4]:
                l = lista[1][4]
            elif l == lista[1][0]:
                l = lista[0][0]
            elif l == lista[1][1]:
                l = lista[0][1]
            elif l == lista[1][2]:
                l = lista[0][2]
            elif l == lista[1][3]:
                l = lista[0][3]
            elif l == lista[1][4]:
                l = lista[0][4]
            print(l, end='')
    print()

def descriptografar(lista):
    n = str(input('Digite a frase que deseja descriptografar: '))
    n = n.split()
    for p in n:
        print(end=' ')
        for l in p:
            if l == lista[1][0]:
                l = lista[0][0]
            elif l == lista[1][1]:
                l = lista[0][1]
            elif l == lista[1][2]:
                l = lista[0][2]
            elif l == lista[1][3]:
                l = lista[0][3]
            elif l == lista[1][4]:
                l = lista[0][4]
            elif l == lista[0][0]:
                l = lista[1][0]
            elif l == lista[0][1]:
                l = lista[1][1]
            elif l == lista[0][2]:
                l = lista[1][2]
            elif l == lista[0][3]:
                l = lista[1][3]
            elif l == lista[0][4]:
                l = lista[1][4]
            print(l, end='')
    print()








