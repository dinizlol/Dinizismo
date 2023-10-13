def chaves():
    from random import randint, shuffle
    numeros = ['1', '¹', '2', '²', '3', '³', '4', '5', '6', '7']
    #numeros = ['as', 'fg', 'de', 'ss', 'ie', 'oi', 'io', 'je', 'me', 'ee']
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'
                ,'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's',
                't', 'u', 'v', 'x', 'z']
    symbols = ['µ', '¥', 'Ʃ', 'Θ', 'Ƶ', 'Ĳ', 'ʬ', 'ɷ', '♘', 'ㅅ', '€', '⥉', '⥐', '㈩', '・']
    lista = []
    excluir = []
    espaços = []
    cont = 0
    while True:
        numero_aleatorio = randint(0, 23)
        if numero_aleatorio not in excluir:
            excluir.append(numero_aleatorio)
            lista.append(alfabeto[numero_aleatorio])
            cont += 1
        if cont == 10:
            break
    for c in range(0, 5):
        n_aleatorio = randint(0, 14-c)
        espaços.append(symbols[n_aleatorio])
        symbols.remove(symbols[n_aleatorio])
    shuffle(numeros)
    lista1 = ''.join(lista)
    numeros2 = ''.join(numeros)
    symbols2 = ''.join(symbols)
    espaços2 = ''.join(espaços)
    return lista1, numeros2, symbols2, espaços2

def CriptoEspaços(texto, espaços):
    from random import choice
    resultado = list()
    for letras in texto:
        if letras == ' ':
            resultado.append(choice(espaços))
        else:
            resultado.append(letras)

    return ''.join(resultado)

def DescriptEspaços(texto, espaços):
    for c in range(0, 5):
        texto = texto.replace(f'{espaços[c]}', ' ')
    #texto_alterado = texto.replace(f'{espaços[0]}', ' ').replace(f'{espaços[1]}',
    #' ').replace(f'{espaços[2]}', ' ').replace(f'{espaços[3]}', ' ').replace(f'{espaços[4]}', ' ')
    return texto



def criptografar(texto, chaves):
    texto_cript = ''
    chaves_cript = list(chaves[0:2])
    symbols = list(chaves[2])
    for letra in texto:
        subs = False
        for chave in chaves_cript:
            for c, l in enumerate(chave):
                if letra == l:
                    if not subs:
                        letra_cript = chaves_cript[0 if chaves_cript.index(chave) == 1 else 1][c]
                        texto_cript = texto_cript + letra_cript
                        subs = True
                        break
            if subs:
                break
        if not subs:
            texto_cript = texto_cript + letra
    return texto_cript

def CriptSymbols(texto, chave):
    for c in range(0, 10):
        texto = texto.replace(f'{chave[0][c]}{chave[1][c]}', f'{chave[2][c]}')
    return texto

