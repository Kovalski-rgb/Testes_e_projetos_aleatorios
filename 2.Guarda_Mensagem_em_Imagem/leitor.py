from PIL import Image
from tkinter import Tk, filedialog

root = Tk() # pointing root to Tk() to use it as Tk() in program. ?????????????????????????????????????????
root.withdraw() # Hides small tkinter window. também não sei
root.attributes('-topmost', True) #deixa a janela como importante, só pode mexer na janela (vou tirar isso depois se pa)
open_file = filedialog.askopenfilename(filetypes=(("PNG Files","*.png"),("JPG Files","*.jpg"),("All files","*.*"))) #janela de pesquisa de arquivo + caminho

contador = 0
n_cores = 0

letras = { #o 1° byte indica se é número ou letra, o segundo indica se é simbolo ou não
    "10000001": "a", "10000010": "b","10000011": "c","10000100": "d","10000101": "e","10000110": "f","10000111": "g","10001000": "h","10001001": "i",
    "10001010": "j", "10001011": "k","10001100": "l","10001101": "m","10001110": "n","10001111": "o","10010000": "p","10010001": "q","10010010": "r",
    "10010011": "s", "10010100": "t","10010101": "u","10010110": "v","10010111": "w","10011000": "x","10011001": "y","10011010": "z",

    "11000001": " ", "11001111": "'", "11010001": "(", "11011101": ".", "11010011": ")", "11011001": ",", "11011100": "\"", "11011111": "/", "11111111": "?",
    "11110101": ":", "11110111": ";", "11011011": "-", "11010111": "+", "11111011": "=", "11010101": "*", "11000011": "!",  "11000000": "@", "11000111": "#",
    "11001001": "$", "11001011": "%", "11001101": "&", "11111100": "|", "11011110": "^", "11111110": "~", "11011010": "´",  "11100000": "`" 
}   #dicionario pra todos os bytes/numeros/letras (talvez eu tenha feito isso de uma forma ESTUPIDAMENTE burra vendo agora)

alocacao = []
array_bytes = []
mensagemSTR = [] #STRING DE CADA NUMERO DA MENSAGEM

#função pra deixar tudo padrão, da pra editar tudo aqui
def mudaPixel(x, y):
    tuplo = (image.getpixel( (x, y) ))
    n_cores = len(tuplo)
    for i in range(n_cores):
        byte = "{0:08b}".format(tuplo[i])
        '''print(tuplo[i], end = ' decimal | ')
        print('byte',byte,'| posicão na cor: ',i,'| cor:',tuplo) #'''
        alocacao.append(byte)

def ler(array_bytes):
    print('Mensagem: ', end='') 
    oito = 0
    stringmensageira = ''
    cod = ''
    for i in range(len(array_bytes)):
        if(oito==8):
            #print('codigo',cod)
            if(cod[:1] == '1'):
                try:
                    stringmensageira += (str(letras[cod]))
                    print(letras[cod], end = '')
                except KeyError:
                    stringmensageira += '>'
                    print('?', end = '')
            else:
                if(cod == '11111111'):
                    print('')
                else:
                    stringmensageira += (str(int(cod, 2)))
                    print(int(cod, 2), end = '')
            cod = ''
            oito = 0
        cod += array_bytes[i][-1:]
        oito += 1
    return stringmensageira

image = Image.open(open_file) 
width, height = image.size


if(width>height):
    for x in range(height): #*da dimensão
        for y in range(width):
            mudaPixel(y, x)
else:
    for x in range(width):
        for y in range(height):
            mudaPixel(x, y)

msg = ler(alocacao)
print()
output = int(input('Deseja salvar a mensagem em um documento de texto? \n 1 - sim \n 2 - não \nDigite sua escolha: '))

if(output != 2):
    try: #testa a linha de baixo
        mensagem = open('mensagem.txt', 'w') #no caso essa linha tenta abrir o arquivo mensagem.txt
        mensagem.write(msg)
    except FileNotFoundError: #ele roda isso se der esse erro especifico
        open('mensagem.txt','x') #o modo x dentro do open cria um arquivo
        mensagem = open('mensagem.txt', 'w')
        mensagem.write(msg)

input('pressione enter para fechar o programa')
exit()
