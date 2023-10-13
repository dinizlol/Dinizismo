def abreviar(nome):
    lista_nome = nome.split()
    ignorar = ['da', 'dos', 'de', 'do']
    retornar = list()
    for i, k in enumerate(lista_nome):
        if k not in ignorar:
            retornar.append(k[0].upper())
    return retornar
