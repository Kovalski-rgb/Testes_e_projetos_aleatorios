# Importing Image from PIL package
from PIL import Image
from tkinter import Tk, filedialog

root = Tk() # pointing root to Tk() to use it as Tk() in program.   | IMAGINO que crie um objeto Tk com nome root
root.withdraw() # Hides small tkinter window.                       | Vou seguir com a linha do que ta escrito ali, não mostra a janelinha padrão
root.attributes('-topmost', True) #deixa a janela como importante (no topo), ela fica em cima das outras janelas (vou tirar isso depois se pa)
open_file = filedialog.askopenfilename(filetypes=(("PNG Files","*.png"),("JPG Files","*.jpg"),("All Files","*.*"))) #janela de pesquisa de arquivo + caminho

contador = 0
alocacao = []
array_bytes = []
mensagemSTR = []

# a mudaPixel só existe pra ficar mais facil mexer nas coisas, 
# ja que as dimensões da imagem podem ser diferentes
def mudaPixel(x, y):
    canais = 0
    tuplo = (image.getpixel( (x, y) ))
    # o tuplo acima tem ou RGB ou RGBA, RGB tem 3 canais e 
    # RGBA tem 4, isso tem que ser responsivo ou não funciona direito
    canais = len(tuplo)
    for i in range(canais):
        byte = "{0:08b}".format(tuplo[i])
        # basicamente ele converte o valor dentro do tuplo em binario
        # e salva na variavel byte, que depois vai ser inserida na lista alocacao

        #comentado por motivo de debug futuro

        '''
        print(tuplo[i], end = ' decimal | ')
        print('byte',byte,'| posicão na cor: ',i,'| cor:',tuplo)
        '''

        alocacao.append(byte)

    # ele retorna o numero de canais, que vai 
    # ser utilizado mais tarde em outra função
    return canais

def STRtoBIN(cont):
    string = ''
    byteSTR = bytearray(cont, "utf8")

    #converte em byte o valor acima
    for posicao in byteSTR:
        string = bin(posicao)
    return string

# a função guardar insere a mensagem dentro dos bytes disponiveis
# da imagem, é aqui que a magia acontece
def guardar(mensagem):   
    #contador de quantos bytes da mensagem ja foram alocados
    contadorMSG = 0
    #contador de qual posição a mensagem ta alocando
    contadorMSGpos = 0

    #se eu fosse usar o padrão i - j no for, dava ruim por que 
    #uma hora ou outra eles podem receber i ou j, e da conflito :/
    for letras in str(mensagem):
        try:
            # ele vai tentar rodar o codigo abaixo, se conseguir, o
            # caractere é um número, se não, pode dar 2 erros, 
            # NameError, que indica que é uma letra, e SyntaxError,
            # que indica que é um símbolo
            eval(letras)

            # mensagemSTR vai ser a mensagem inteira convertida em bytes
            mensagemSTR.append("{0:08b}".format(int(letras)))

        # caso letras(a variavel) seja uma letra
        # NameError indica que é letra, erro vindo do eval
        # ValueError passa as vezes pelo eval, mas é letra
        except (NameError, ValueError):

            #converte a "string" (caractere) em binario
            stringBIN = STRtoBIN(letras)
    
            # converte do jeito que eu preciso, esse é tipo um
            # formato que, creio eu, só funciona nesse programa
            stringFinal = ''

            for posicao in stringBIN:
                try:
                    # quando uma string é convertida em binario, em alguma
                    # parte dela aparede um 0b, geralmente nos 2 primeiros
                    # caracteres, quando aparecer, o try vai identificar. em
                    # quanto não aparece, os bytes do caractere vão sendo salvos
                    eval(posicao)
                    stringFinal += posicao

                except NameError:
                    # esse except infelizmente praticamente não faz nada, a
                    # intenção dele é colocar 1 em vez do b que aparece no
                    # inicio, mas a linha de baixo passa por cima dessa
                    stringFinal = '1' + stringFinal[1:]

            # um byte possui 8 bits, como o alfabeto inteiro vai até o 26, e
            # o máximo de bits que são necessarios pra representar 26 são 5
            # bits, os ultimos 3 são utilizados pra identificar se isso é uma
            # letra (101 maiuscula ou 100 minuscula), um número ou um caractece na hora da leitura
            if(stringFinal[2] == '0'):
                stringFinal = '101' + stringFinal[3:]
            else:
                stringFinal = '100' + stringFinal[3:]

            # mensagemSTR vai ser a mensagem inteira convertida em bytes
            mensagemSTR.append(stringFinal)

        # caso letras(a variavel) seja um símbolo
        except SyntaxError:
            stringBIN = STRtoBIN(letras)
            stringFinal = ''
            for posicao in stringBIN:
                try:
                    # até aqui a lógica é exatamente a mesma da de converter
                    # letras em binário, a grande diferença fica na sinalização
                    # dos simbolos
                    eval(posicao)
                    stringFinal += posicao

                except NameError:
                    # agora sim, essa linha literalmente não agrega em nada no
                    # resultado final, mas eu preciso dela pro programa não
                    # crashar
                    stringFinal = 'a' + stringFinal[1:]
            
            # 11 na frente do byte é utilizado para indicar que isso
            # deve ser lido como um simbolo na hora da leitura
            stringFinal = '11' + stringFinal[2:]

            # alguns simbolos tem resultado maior que 8 bits, esses precisam ser
            # padronizados, removendo o ultimo bit
            while(len(stringFinal)>8):
                stringFinal = stringFinal[:-1] 

            # ja outros (infelizmente a maioria) são menores que 8 bits, esses 
            # precisam receber 1 bit no final para ficarem padronizados
            while(len(stringFinal)<8): 
                stringFinal = stringFinal + '1'

            # mensagemSTR vai ser a mensagem inteira convertida em bytes
            mensagemSTR.append(stringFinal)

    # isso coloca 0 nos valores fora da mensagem, e coloca a mensagem no ultimo bit
    # dentro da lista de bytes recebida da imagem
    # comentando isso eu notei que alocacao não é alterado até o final do programa,
    # mas mesmo assim ele funciona, não sei por que :/
    for i in range(len(alocacao)):
        array_bytes = alocacao
        try:
            if(contadorMSG==8):
                contadorMSGpos += 1
                contadorMSG = 0

            # se ta dentro da mensagem ele coloca no ultimo bit o bit correspondende na mensagem
            array_bytes[i] = (array_bytes[i])[:-1] + (mensagemSTR[contadorMSGpos])[contadorMSG]

        except IndexError:
            # se tiver fora do index da mensagem, o padrão é inserir um 0
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
    # não acho que outros formatos tenham mais ou menos canais de cor (R,G,B,A,X....)
    # mas sei que existe RGBA e RGB, por isso só tem 2 opções aqui
    if(n_cores == 4):
        image.putpixel((x, y),(int(alocacao[c-3], 2), int(alocacao[c-2], 2), int(alocacao[c-1], 2), int(alocacao[c], 2)))
        #print('coords:',x, y,' cor:',int(alocacao[c-3], 2), int(alocacao[c-2], 2), int(alocacao[c-1], 2), int(alocacao[c], 2),'c=',c)
    else:
        image.putpixel((x, y),(int(alocacao[c-2], 2), int(alocacao[c-1], 2), int(alocacao[c], 2)))
        #print('coords:',x, y,' cor:',int(alocacao[c-2], 2), int(alocacao[c-1], 2), int(alocacao[c], 2),'c=',c)

#isso cria um objeto de imagem | open_file é o caminho da imagem selecionada la em cima
image = Image.open(open_file) 
width, height = image.size

#se a dimensão da imagem não for na ordem certa, o programa crasha, por isso esse if existe
if(width>height): 
    for x in range(height):
        for y in range(width):
            n_cores = mudaPixel(y, x)
# a funcao mudaPixel na verdade pega o valor RGB / RGBA dos pixels
else:
    for x in range(width):
        for y in range(height):
            n_cores = mudaPixel(x, y)

print('bytes(caracteres) disponiveis para mensagem:',(len(alocacao)/8))
print("a mensagem final aceita os seguintes simbolos: ")
print("' ' ''' '(' ')' ',' '.' '\\' '/' '?' ':' ';' '-' '+'")
print("'=' '*' '!' '@' '#' '$' '%' '&' '|' '^' '~' '´' '`'")
# coloquei um caractere especial (alt + 255) p representar o final da mensagem
mensagem = input('Mensagem: ') + ' '

# não funciona direito salvar em JPG, vou deixar aqui como um lembrete
# talvez num futuro próximo eu tente ver o que ta dando errado com o formato em jpg
# formato = int(input('Qual o formato de saida desejado? \n 1 - png \n 2 - jpg \nDigite a opção desejada: '))
formato = 1

guardar(mensagem)
injecao()
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
