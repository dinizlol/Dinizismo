def criptografar(msg):
    lista_teste = msg.split()
    principal = list()
    for p in lista_teste:
        temp = list()
        for l in p:
            if l == 's':
                l = 't'
            elif l == 'u':
                l = 'e'
            elif l == 'b':
                l = 'c'
            elif l == 'i':
                l = 'l'
            elif l == 'r':
                l = 'a'
            elif l == 't':
                l = 's'
            elif l == 'e':
                l = 'u'
            elif l == 'c':
                l = 'b'
            elif l == 'l':
                l = 'i'
            elif l == 'a':
                l = 'r'
            temp.append(l)
        temp = ''.join(temp)
        principal.append(temp)
    return principal
def descriptografar(msg):
    principal = list()
    cript = msg.split()
    for p in cript:
        temp = list()
        for l in p:
            if l == 't':
                l = 's'
            elif l == 'e':
                l = 'u'
            elif l == 'c':
                l = 'b'
            elif l == 'l':
                l = 'i'
            elif l == 'a':
                l = 'r'
            elif l == 's':
                l = 't'
            elif l == 'u':
                l = 'e'
            elif l == 'b':
                l = 'c'
            elif l == 'i':
                l = 'l'
            elif l == 'r':
                l = 'a'
            temp.append(l)
        temp = ''.join(temp)
        principal.append(temp)
    return principal
