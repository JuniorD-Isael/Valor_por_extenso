from centenas import Centenas
from unidadeDezena import Unidade_Dezena
from dicionarioNumerico import Dicionario_numerico
from time import sleep

# Código principal
dic_numeros = Dicionario_numerico.dic_numerico_valores()


valor = input('Digite um numero entre 1 e 999: ').strip()


while valor != 1000 or int(valor) > 999 or int(valor) < 0:

    if int(valor) > 999 or int(valor) < 0:
        print('-' * 10)
        print('Limite definido entre 1 e 999')
        sleep(1)
        print('-' * 10)

    if valor == 'sair':
        break

    while not valor.isnumeric():
        print('-' * 10)
        print('Você deve digitar um número.')
        print('-' * 10)
        sleep(1)
        valor = input('Digite um numero entre 1 e 999: ')

    if valor.isnumeric():
        valor = valor.lstrip('0')
        tamanho_valor = len(valor)
    else:
        break
    Unidade_Dezena.valores(tamanho_valor, valor, dic_numeros)
    Centenas.valores(tamanho_valor, valor, dic_numeros)

    valor = input('Digite um numero entre 1 e 999: ').strip()
