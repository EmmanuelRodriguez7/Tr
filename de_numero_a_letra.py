# Rebir un numero y cambiarlo a letras
# Emmanuel Rodriguez Montes

numeros = {
    1: 'uno',
    2: 'dos',
    3: 'tres',
    4: 'cuatro',
    5: 'cinco',
    6: 'seis',
    7: 'siete',
    8: 'ocho',
    9: 'nueve',
    10: 'diez',
    11: 'once',
    12: 'doce',
    13: 'trece',
    14: 'catorce',
    15: 'quince',
    16: 'dieciseis',
    17: 'diecisiete',
    18: 'dieciocho',
    19: 'diecinueve',
    20: 'veinte',
    30: 'treinta',
    40: 'cuarenta',
    50: 'cincuenta',
    60: 'sesenta',
    70: 'setenta',
    80: 'ochenta',
    90: 'noventa',
    100: 'cien'
}
decenas = {
    1: 'diez',
    2: 'veinte',
    3: 'treinta',
    4: 'cuarenta',
    5: 'cincuenta',
    6: 'sesenta',
    7: 'setenta',
    8: 'ochenta',
    9: 'noventa',
    10: 'cien',
}
def tres_digitos(number):
    if int(number) in numeros:
        return numeros[int(number)]
    if len(number) == 2:
        if int(number[-2]) == 2:
            return 'veinti' + numeros[int(number[-1])]
        if int(number[-2]) > 2:
            return decenas[int(number[-2])] + ' y ' + numeros[int(number[-1])]
    if len(number) == 3:
        if number[-1] != 0:
            if int(number[-3]) == 1:
                if int(number[-2]) > 2 and int(number[-1]) != 0:
                    num = int(number[-2])
                    return 'ciento ' + decenas[num] + ' y ' + numeros[int(number[-1])]
                if int(number[-2]) == 2 and int(number[-1]) != 0:
                    return 'ciento veinti' + numeros[int(number[-1])]
                num = int(number[-2:])
                return 'ciento ' + numeros[num]
            else:
                if int(number[-2]) > 2 and int(number[-1]) != 0:
                    num = int(number[-2])
                    return numeros[int(number[-3])] + 'cientos ' + decenas[num] + ' y ' + numeros[int(number[-1])]
                if int(number[-2]) == 2 and int(number[-1]) != 0:
                    return numeros[int(number[-3])] + 'cientos veinti' + numeros[int(number[-1])]
                num = int(number[-2:])
                return numeros[int(number[-3])] + 'cientos ' + numeros[num]

def seis_digitos(number):
    if int(number) == 1:
        return 'mil '
    if int(number) in numeros:
        return numeros[int(number)] + ' mil '
    if len(number) == 2:
        if int(number[-2]) == 2 and int(number[-1]) != 0:
            return 'veinti' + numeros[int(number[-1])] + ' mil '
        if int(number[-2]) > 2 and int(number[-1]) != 0:
            return decenas[int(number[-2])] + ' y ' + numeros[int(number[-1])] + ' mil '
    if len(number) == 3:
        if number[-1] != 0:
            if int(number[-3]) == 1:
                if int(number[-2]) > 2 and int(number[-1]) != 0:
                    num = int(number[-2])
                    return 'ciento ' + decenas[num] + ' y ' + numeros[int(number[-1])] + ' mil '
                if int(number[-2]) == 2 and int(number[-1]) != 0:
                    return 'ciento veinti' + numeros[int(number[-1])] + ' mil '
                num = int(number[-2:])
                return 'ciento ' + numeros[num] + ' mil '
            else:
                if int(number[-2]) > 2 and int(number[-1]) != 0:
                    num = int(number[-2])
                    return numeros[int(number[-3])] + 'cientos ' + decenas[num] + ' y ' + numeros[int(number[-1])] + ' mil '
                if int(number[-2]) == 2 and int(number[-1]) != 0:
                    return numeros[int(number[-3])] + 'cientos veinti' + numeros[int(number[-1])] + ' mil '
                num = int(number[-2:])
                return numeros[int(number[-3])] + 'cientos ' + numeros[num]

def nueve_digitos(number):
    if int(number) == 1:
        return 'un millon '
    if int(number) in numeros:
        return numeros[int(number)] + ' millones '
    if len(number) == 2:
        if int(number[-2]) == 2 and int(number[-1]) != 0:
            return 'veinti' + numeros[int(number[-1])] + ' millones '
        if int(number[-2]) > 2 and int(number[-1]) != 0:
            return decenas[int(number[-2])] + ' y ' + numeros[int(number[-1])] + ' millones '
    if len(number) == 3:
        if number[-1] != 0:
            if int(number[-3]) == 1:
                if int(number[-2]) > 2 and int(number[-1]) != 0:
                    num = int(number[-2])
                    return 'ciento ' + decenas[num] + ' y ' + numeros[int(number[-1])] + ' millones '
                if int(number[-2]) == 2 and int(number[-1]) != 0:
                    return 'ciento veinti' + numeros[int(number[-1])] + ' millones '
                num = int(number[-2:])
                return 'ciento ' + numeros[num] + ' millones '
            else:
                if int(number[-2]) > 2 and int(number[-1]) != 0:
                    num = int(number[-2])
                    return numeros[int(number[-3])] + 'cientos ' + decenas[num] + ' y ' + numeros[int(number[-1])] + ' millones '
                if int(number[-2]) == 2 and int(number[-1]) != 0:
                    return numeros[int(number[-3])] + 'cientos veinti' + numeros[int(number[-1])] + ' millones '
                num = int(number[-2:])
                return numeros[int(number[-3])] + 'cientos ' + numeros[num]

def doce_digitos(number):
    if int(number) == 1:
        return ' mil  '
    if int(number) in numeros:
        return numeros[int(number)] + ' mil '
    if len(number) == 2:
        if int(number[-2]) == 2 and int(number[-1]) != 0:
            return 'veinti' + numeros[int(number[-1])] + ' mil '
        if int(number[-2]) > 2 and int(number[-1]) != 0:
            return decenas[int(number[-2])] + ' y ' + numeros[int(number[-1])] + ' mil '
    if len(number) == 3:
        if number[-1] != 0:
            if int(number[-3]) == 1:
                if int(number[-2]) > 2 and int(number[-1]) != 0:
                    num = int(number[-2])
                    return 'ciento ' + decenas[num] + ' y ' + numeros[int(number[-1])] + ' mil '
                if int(number[-2]) == 2 and int(number[-1]) != 0:
                    return 'ciento veinti' + numeros[int(number[-1])] + ' mil '
                num = int(number[-2:])
                return 'ciento ' + numeros[num] + ' mil '
            else:
                if int(number[-2]) > 2 and int(number[-1]) != 0:
                    num = int(number[-2])
                    return numeros[int(number[-3])] + 'cientos ' + decenas[num] + ' y ' + numeros[int(number[-1])] + ' mil '
                if int(number[-2]) == 2 and int(number[-1]) != 0:
                    return numeros[int(number[-3])] + 'cientos veinti' + numeros[int(number[-1])] + ' mil '
                num = int(number[-2:])
                return numeros[int(number[-3])] + 'cientos ' + numeros[num]

def quince_digitos(number):
    if int(number) == 1:
        return 'un billon '
    if int(number) in numeros:
        return numeros[int(number)] + ' billones '
    if len(number) == 2:
        if int(number[-2]) == 2 and int(number[-1]) != 0:
            return 'veinti' + numeros[int(number[-1])] + ' billones '
        if int(number[-2]) > 2 and int(number[-1]) != 0:
            return decenas[int(number[-2])] + ' y ' + numeros[int(number[-1])] + ' billones '
    if len(number) == 3:
        if number[-1] != 0:
            if int(number[-3]) == 1:
                if int(number[-2]) > 2 and int(number[-1]) != 0:
                    num = int(number[-2])
                    return 'ciento ' + decenas[num] + ' y ' + numeros[int(number[-1])] + ' billones '
                if int(number[-2]) == 2 and int(number[-1]) != 0:
                    return 'ciento veinti' + numeros[int(number[-1])] + ' billones '
                num = int(number[-2:])
                return 'ciento ' + numeros[num] + ' billones '
            else:
                if int(number[-2]) > 2 and int(number[-1]) != 0:
                    num = int(number[-2])
                    return numeros[int(number[-3])] + 'cientos ' + decenas[num] + ' y ' + numeros[int(number[-1])] + ' billones '
                if int(number[-2]) == 2 and int(number[-1]) != 0:
                    return numeros[int(number[-3])] + 'cientos veinti' + numeros[int(number[-1])] + ' billones '
                num = int(number[-2:])
                return numeros[int(number[-3])] + 'cientos ' + numeros[num]

def a_numero(number):
    sum = 0
    for i in range(len(number)):
        num = int(number[i])
        sum = sum + num
    if sum == 0:
        return 'cero'

    _tres = number[-3:]
    primera = tres_digitos(_tres)
    _seis = number[-6:-3]
    segunda = seis_digitos(_seis)
    _nueve = number[-9:-6]
    tercera = nueve_digitos(_nueve)
    _doce = number[-12:-9]
    cuarta = doce_digitos(_doce)
    _quince = number[-15:-12]
    quinta = quince_digitos(_quince)
    #_dieciocho = number[-18:-15]
    #sexta = seis_digitos(_dieciocho)
    
    word = [quinta, cuarta, tercera, segunda, primera]
    if _seis == '':
        word.remove(segunda)
    if _nueve == '':
        word.remove(tercera)
    if _doce == '':
        word.remove(cuarta)
    if _quince == '':
        word.remove(quinta)
    #if _dieciocho == '':
    #    word.remove(sexta)

    return ''.join(word)
