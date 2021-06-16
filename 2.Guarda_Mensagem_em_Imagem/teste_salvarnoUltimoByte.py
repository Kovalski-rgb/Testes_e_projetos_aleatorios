array_bytes = []
decimais = [
    13,
    14,
    30,
    13,
    14,
    30,
    13,
    14,
    14,
    14,
    30,
    13,
    14,
    30,
    13,
    14,
    14,
    14,
    30,
    13,
    14,
    30,
    13,
    14,
    14,
    13,
    14,
    30,
    13,
    14,
    14,
    14,
    30,
    13,
    14,
    30,
    13,
    14,
    14,
    13,
    14,
    14,
    14,
    30,
    13,
    14,
    30,
    13,
    14,
    14,
    14,
    30,
    13,
    14,
    30,
    13,
    14,
    14,
    13,
    14,
    30,
    13,
    14,
    14,
    14,
    30,
    13,
    14,
    30,
    13,
    14,
    14
]

mensagem = 23015234
mensagemSTR = [] #STRING DE CADA NUMERO DA MENSAGEM

def guardar(mensagem):
    #contador de quantos bytes da mensagem ja foram alocados
    contadorMSG = 0
    #contador de qual posição a mensagem ta alocando
    contadorMSGpos = 0

    for i in str(mensagem):
        mensagemSTR.append("{0:04b}".format(int(i)))

    print(mensagemSTR)
    #mensagem = "{0:08b}".format(mensagem)
    for i in range(len(decimais)):
        array_bytes.append("{0:08b}".format(decimais[i]))
        try:
            if(contadorMSG==4):
                contadorMSGpos += 1
                contadorMSG = 0
            array_bytes[i] = (array_bytes[i])[:-1] + (mensagemSTR[contadorMSGpos])[contadorMSG]
        except IndexError:
            array_bytes[i] = (array_bytes[i])[:-1] + '0'
        contadorMSG += 1
    print('mensagem:',mensagem)

def ler(array_bytes):
    print('recuperd: ', end='')
    oito = 0
    cod = ''
    for i in range(len(array_bytes)):
        if(oito==4):
            print(int(cod, 2), end = '')
            cod = ''
            oito = 0
        cod += array_bytes[i][-1:]
        oito += 1

guardar(mensagem)
ler(array_bytes)

