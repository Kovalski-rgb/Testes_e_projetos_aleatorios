# Importing Image from PIL package
from PIL import Image
from tkinter import Tk, filedialog

root = Tk() # pointing root to Tk() to use it as Tk() in program. ?????????????????????????????????????????
root.withdraw() # Hides small tkinter window. também não sei
root.attributes('-topmost', True) #deixa a janela como importante, só pode mexer na janela (vou tirar isso depois se pa)
open_file = filedialog.askopenfilename(filetypes=(("PNG Files","*.png"),("JPG Files","*.jpg"),("All Files","*.*"))) #janela de pesquisa de arquivo + caminho

contador = 0

#601870.5 bytes(caracteres) para o pato 
#49056.0  bytes(caracteres) para o lino
alocacao = []
array_bytes = []
mensagemSTR = [] #STRING DE CADA NUMERO DA MENSAGEM


#função pra deixar tudo padrão, da pra editar tudo aqui
def mudaPixel(x, y):
    canais = 0
    #if(x > 0):#width-1):
    tuplo = (image.getpixel( (x, y) ))
    canais = len(tuplo)
    #print(n_cores)
    #print(tuplo)
    for i in range(canais):
        byte = "{0:08b}".format(tuplo[i])
        '''print(tuplo[i], end = ' decimal | ')
        print('byte',byte,'| posicão na cor: ',i,'| cor:',tuplo) #'''
        alocacao.append(byte)
    return canais

# creating a image object
image = Image.open(open_file) 
width, height = image.size

if(width>height): #se a dimensão da imagem não for na ordem certa, o programa da ruim
    for x in range(height):
        for y in range(width):
            n_cores = mudaPixel(y, x)
else:
    for x in range(width):
        for y in range(height):
            n_cores = mudaPixel(x, y)

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

    #se eu fosse usar o padrão i - j no for, dava ruim por que uma hora ou outra eles podem receber i ou j
    for caracolis in str(mensagem):
        try:
            eval(caracolis)             #numero
            mensagemSTR.append("{0:08b}".format(int(caracolis)))

        except NameError:       #letras - caracteres
            #converte string em binario
            string = STRtoBIN(caracolis)
    
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
            while(len(stringFinal)>8):
                stringFinal = stringFinal[:-1] 

            while(len(stringFinal)<8): 
                stringFinal = stringFinal + '1'

            mensagemSTR.append(stringFinal)

    for i in range(len(alocacao)):
        array_bytes = alocacao
        try:
            if(contadorMSG==8):
                contadorMSGpos += 1
                contadorMSG = 0
            array_bytes[i] = (array_bytes[i])[:-1] + (mensagemSTR[contadorMSGpos])[contadorMSG]
        except IndexError:
            array_bytes[i] = (array_bytes[i])[:-1] + '0'

        contadorMSG += 1

def injecao():
    contador = n_cores - 1
    if(width>height):
        for x in range(height):
            for y in range(width):
                injecaoEfetiva(y, x, contador)
                contador += n_cores
    else:
        for x in range(width):
            for y in range(height):
                injecaoEfetiva(x, y, contador)
                contador += n_cores
    

def injecaoEfetiva(x, y, c):
    if(n_cores == 4):
        image.putpixel((x, y),(int(alocacao[c-3], 2), int(alocacao[c-2], 2), int(alocacao[c-1], 2), int(alocacao[c], 2)))
        #print('coords:',x, y,' cor:',int(alocacao[c-3], 2), int(alocacao[c-2], 2), int(alocacao[c-1], 2), int(alocacao[c], 2),'c=',c)
    else:
        image.putpixel((x, y),(int(alocacao[c-2], 2), int(alocacao[c-1], 2), int(alocacao[c], 2)))
        #print('coords:',x, y,' cor:',int(alocacao[c-2], 2), int(alocacao[c-1], 2), int(alocacao[c], 2),'c=',c)

print('bytes(caracteres) disponiveis para mensagem:',(len(alocacao)/8))
print("a mensagem final aceita os seguintes simbolos: ")
print("' ' ''' '(' ')' ',' '.' '\\' '/' '?' ':' ';' '-' '+'")
print("'=' '*' '!' '@' '#' '$' '%' '&' '|' '^' '~' '´' '`'")
mensagem = input('Mensagem: ') + ' '
formato = int(input('Qual o formato de saida desejado? \n 1 - png \n 2 - jpg \nDigite a opção desejada: '))

guardar(mensagem)
injecao() #alocacao
print('mensagem implantada com sucesso')

if(formato == 1):
    image.save('output.png')
elif(formato == 2):
    try:
        image.save('output.jpg')
    except OSError:
        print('Erro ao salvar a imagem em JPG, salvando em PNG...')
        image.save('output.png')
else:
    image.save('output.png')


input('pressione enter para fechar o programa')
exit()
