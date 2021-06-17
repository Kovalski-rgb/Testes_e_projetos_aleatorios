# Importing Image from PIL package
from PIL import Image
from tkinter import Tk, filedialog

root = Tk() # pointing root to Tk() to use it as Tk() in program. ?????????????????????????????????????????
root.withdraw() # Hides small tkinter window. também não sei
root.attributes('-topmost', True) #deixa a janela como importante, só pode mexer na janela (vou tirar isso depois se pa)
open_file = filedialog.askopenfilename(filetypes=(("PNG Files","*.png"),("JPG Files","*.jpg"),("All files","*.*"))) #janela de pesquisa de arquivo + caminho

contador = 0

#601870.5 bytes(caracteres) para o pato 
#49056.0  bytes(caracteres) para o lino
alocacao = []
array_bytes = []
mensagemSTR = [] #STRING DE CADA NUMERO DA MENSAGEM

#função pra deixar tudo padrão, da pra editar tudo aqui
def mudaPixel(x, y):
    #if(x > 0):#width-1):
    tuplo = (image.getpixel( (x, y) ))
    for i in range(4):
        byte = "{0:08b}".format(tuplo[i])
        '''print(tuplo[i], end = ' decimal | ')
        print('byte',byte,'| posicão na cor: ',i,'| cor:',tuplo) #'''
        alocacao.append(byte)

# creating a image object
image = Image.open(open_file) 
width, height = image.size

print('w:',width)
print('h:',height)

if(width>height):
    print('Height') #dependendo da imagem ela crasha o python :/
    for x in range(height): #*da dimensão
        for y in range(width):
            mudaPixel(y, x)
else:
    print('Width')
    for x in range(width):
        for y in range(height):
            mudaPixel(x, y)

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
            print(caracolis)
            eval(caracolis)             #numero
            mensagemSTR.append("{0:08b}".format(int(caracolis)))

        except NameError:       #letras - caracteres
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
    for i in range(len(alocacao)):
        array_bytes = alocacao#.append("{0:08b}".format(alocacao[i]))
        try:
            if(contadorMSG==8):
                contadorMSGpos += 1
                contadorMSG = 0
            array_bytes[i] = (array_bytes[i])[:-1] + (mensagemSTR[contadorMSGpos])[contadorMSG]
        except IndexError:
            array_bytes[i] = (array_bytes[i])[:-1] + '0'

        contadorMSG += 1
    print('mensagem:',mensagem)

def injecao():
    contador = 3
    if(width>height):
        print('Height')
        for x in range(height):
            for y in range(width):
                injecaoEfetiva(y, x, contador)
                contador += 4
    else:
        print('Width')
        for x in range(width):
            for y in range(height):
                injecaoEfetiva(x, y, contador)
                contador += 4

def injecaoEfetiva(x, y, c):
    image.putpixel((x, y),(int(alocacao[c-3], 2), int(alocacao[c-2], 2), int(alocacao[c-1], 2), int(alocacao[c], 2)))
    #print('coords:',x, y,' cor:',int(alocacao[c-3], 2), int(alocacao[c-2], 2), int(alocacao[c-1], 2), int(alocacao[c], 2),'c=',c)
    

#print alocacao
#for i in alocacao:
#    print(i)
print('bytes(caracteres) disponiveis para mensagem:',(len(alocacao)/8))
input('pressione enter: ') #" '(.),\/?:;-+ =*!@#$%&|^~´`"
print("a mensagem final aceita os seguintes simbolos: ")
print("' ' ''' '(' ')' ',' '.' '\\' '/' '?' ':' ';' '-' '+'")
print("'=' '*' '!' '@' '#' '$' '%' '&' '|' '^' '~' '´' '`'")
mensagem = input('Mensagem: ') + ' '

guardar(mensagem)
injecao() #alocacao

#print('ar',array_bytes)
#print('al',alocacao)

image.show()
image.save('lino.png')
