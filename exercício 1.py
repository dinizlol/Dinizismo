from ex06.funções import *
chaves = ['ui', 'ca']
symbols =['%', '#']
texto = 'carauc incria'
print(chaves[0][0], chaves[1][0])
print(chaves[0][1], chaves[1][1])


for c in range(0, 2):
    texto = texto.replace(f'{chaves[0][c]}{chaves[1][c]}', f'{symbols[c]}')
    print(texto)

# teste1 = chaves()
# texto = 'quero muito andar de bicicleta antes de ir para paris'
#
# if 'ue' in texto:
#     print('oi')
