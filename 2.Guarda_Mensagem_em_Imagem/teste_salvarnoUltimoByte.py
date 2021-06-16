array_bytes = []
decimais = range(0, 160)

letras = { #o 1° byte indica se é número ou letra, o segundo indica se é simbolo ou não
    "10000001": "a",
    "10000010": "b",
    "10000011": "c",
    "10000100": "d",
    "10000101": "e",
    "10000110": "f",
    "10000111": "g",
    "10001000": "h",
    "10001001": "i",
    "10001010": "j",
    "10001011": "k",
    "10001100": "l",
    "10001101": "m",
    "10001110": "n",
    "10001111": "o",
    "10010000": "p",
    "10010001": "q",
    "10010010": "r",
    "10010011": "s",
    "10010100": "t",
    "10010101": "u",
    "10010110": "v",
    "10010111": "w",
    "10011000": "x",
    "10011001": "y",
    "10011010": "z",

    "11000001": " ",
    "11001111": "'",
    "11010001": "(",
    "11011101": ".",
    "11010011": ")",
    "11011001": ",",
    "11011100": "\"",
    "11011111": "/",
    "11111111": "?",
    "11110101": ":",
    "11110111": ";",
    "11011011": "-",
    "11010111": "+",
    "11111011": "=",
    "11010101": "*",
    "11000011": "!",
    "11000000": "@",
    "11000111": "#",
    "11001001": "$",
    "11001011": "%",
    "11001101": "&",
    "11111100": "|",
    "11011110": "^",
    "11111110": "~",
    "11011010": "´",
    "11100000": "`" 
}

mensagem = 'Bom dia!!! 123123 ' 
mensagemSTR = [] #STRING DE CADA NUMERO DA MENSAGEM

def STRtoBIN(cont):
    string = ''
    byteSTR = bytearray(cont, "utf8")

        #converte em byte o valor acima
    for caraquelinhos in byteSTR:
        string = bin(caraquelinhos)
    return string

def guardar(mensagem):
    #contador de quantos bytes da mensagem ja foram alocados
    contadorMSG = 0
    #contador de qual posição a mensagem ta alocando
    contadorMSGpos = 0

    for caracolis in str(mensagem):
        try:
            eval(caracolis)             #numero
            mensagemSTR.append("{0:08b}".format(int(caracolis)))

        except NameError:       #letras - caracteres
            #print('LETRA')
    
            #converte string em binario
            string = STRtoBIN(caracolis)
            #print(string)
    
            #converte do jeito que eu preciso
            stringFinal = ''
            for caraquelinhos in string:
                try:
                    eval(caraquelinhos)
                    stringFinal += caraquelinhos
                except NameError:
                    stringFinal = '1' + stringFinal[1:]
            stringFinal = '100' + stringFinal[3:]
            mensagemSTR.append(stringFinal)

        except SyntaxError:     #simbolos
            #print('SIMBOLO')
            #converte string em binario
            string = STRtoBIN(caracolis)
            #converte do jeito que eu preciso
            stringFinal = ''
            for caraquelinhos in string:
                try:
                    eval(caraquelinhos)
                    stringFinal += caraquelinhos
                except NameError:
                    stringFinal = 'a' + stringFinal[1:]
            stringFinal = '11' + stringFinal[2:]
            #stringFinal = stringFinal[:-1] + '1'
            while(len(stringFinal)>8):
                stringFinal = stringFinal[:-1] 
                #stringFinal = stringFinal[:-1] + '0'

            while(len(stringFinal)<8): 
                stringFinal = stringFinal + '1'

            mensagemSTR.append(stringFinal)

    print(mensagemSTR)
    #mensagem = "{0:08b}".format(mensagem)
    for i in range(len(decimais)):
        array_bytes.append("{0:08b}".format(decimais[i]))
        try:
            if(contadorMSG==8):
                contadorMSGpos += 1
                contadorMSG = 0
            array_bytes[i] = (array_bytes[i])[:-1] + (mensagemSTR[contadorMSGpos])[contadorMSG]
        except IndexError:
            array_bytes[i] = (array_bytes[i])[:-1] + '0'

        contadorMSG += 1
    print('mensagem:',mensagem)

def ler(array_bytes):
    print('recuperado: ', end='')
    oito = 0
    cod = ''
    for i in range(len(array_bytes)):
        if(oito==8):
            if(cod[:1] == '1'):
                print(letras[cod], end = '')
            else:
                print(int(cod, 2), end = '')
            cod = ''
            oito = 0
        cod += array_bytes[i][-1:]
        oito += 1

guardar(mensagem)
ler(array_bytes)
