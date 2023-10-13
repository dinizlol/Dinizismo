def ChecarEspacos(a):
    a = a.strip()
    if a.count(' ') > 0:
        print('Digite apenas uma palavra.')
        return False
    else:
        return ChecarRepetição(a)

def ChecarRepetição(a):
    cont = 0
    for letras in a:
        if a.count(letras) > 1:
            print('A palavra possui letras repetidas')
            return False
        else:
            cont += 1
            if cont == len(a):
                return a

def ChecarLen(a, b):
    if len(a) != len(b):
        print('As palavras precisam ter o mesmo número de letras.')
    else:
        return ChecarLetras(a, b)

def ChecarLetras(a, b):
    for c, letras in enumerate(a):
        if letras == b[c]:
            print('Letras iguais na mesma posição!')
            break
        else:
            if c+1 == len(a):
                return a, b

def Criptografar(chaves):
    Texto = str(input('Digite um texto para ser criptografado: '))
    TextoCriptografado = ''
    for letras in Texto:
        found = False
        for chave in chaves:
            for c, l in enumerate(chave):
                if l == letras:
                    letra_subs = chaves[0 if chaves.index(chave) == 1 else 1][c]
                    TextoCriptografado += letra_subs
                    found = True
                    break
            if found:
                break
        if not found:
            TextoCriptografado += letras
    return TextoCriptografado







