# se algum dos modulos necessarios para o funcionamento do programa não esta instalado,
# um aviso será dado retornado no terminal, e o programa fechará
exit = False
try:
    from PIL import Image
except ModuleNotFoundError:
    print('PIL não esta instalado no sistema')
    print('abra o CMD e digite: pip install pillow')
    exit = True
try:
    from tkinter import Tk, filedialog
except ModuleNotFoundError:
    print('tkinter não esta instalado no sistema')
    exit = True

if(exit):
    print('Instale os modulos acima executando os comandos e tente novamente')
    input('pressione enter para encerrar o programa ')
    exit()

root = Tk() # pointing root to Tk() to use it as Tk() in program.   | IMAGINO que crie um objeto Tk com nome root
root.withdraw() # Hides small tkinter window.                       | Vou seguir com a linha do que ta escrito ali, não mostra a janelinha padrão
root.attributes('-topmost', True) #deixa a janela como importante (no topo), ela fica em cima das outras janelas (vou tirar isso depois se pa)
open_file = filedialog.askopenfilename(filetypes=(("PNG Files","*.png"),("JPG Files","*.jpg"),("All Files","*.*"))) #janela de pesquisa de arquivo + caminho

contador = 0
n_cores = 0

# o 1° byte indica se é número ou letra, o segundo indica se é simbolo ou não, e o 
# 3° juntamente com o 1° indica se é maiuscula ou não

# dicionario pra todos os bytes/numeros/letras (imagino que tenham formas melhores de fazer)
# a identificação das letras e dos caracteres, mas ficou assim por agora
letras = {
    "10000001":"a", "10000010":"b", "10000011":"c", "10000100":"d", "10000101":"e", "10000110":"f", "10000111":"g", "10001000":"h", "10001001":"i",
    "10001010":"j", "10001011":"k", "10001100":"l", "10001101":"m", "10001110":"n", "10001111":"o", "10010000":"p", "10010001":"q", "10010010":"r",
    "10010011":"s", "10010100":"t", "10010101":"u", "10010110":"v", "10010111":"w", "10011000":"x", "10011001":"y", "10011010":"z",

    "10100001":"A", "10100010":"B", "10100011":"C", "10100100":"D", "10100101":"E", "10100110":"F", "10100111":"G", "10101000":"H", "10101001":"I",
    "10101010":"J", "10101011":"K", "10101100":"L", "10101101":"M", "10101110":"N", "10101111":"O", "10110000":"P", "10110001":"Q", "10110010":"R",
    "10110011":"S", "10110100":"T", "10110101":"U", "10110110":"V", "10110111":"W", "10111000":"X", "10111001":"Y", "10111010":"Z",

    "11000001":" ", "11001111":"'", "11010001":"(", "11011101":".", "11010011":")", "11011001":",", "11011100":"\\", "11011111":"/", "11111111":"?",
    "11110101":":", "11110111":";", "11011011":"-", "11010111":"+", "11111011":"=", "11010101":"*", "11000011":"!",  "11000000":"@", "11000111":"#",
    "11001001":"$", "11001011":"%", "11001101":"&", "11111100":"|", "11011110":"^", "11111110":"~", "11011010":"´",  "11100000":"`" 
}

alocacao = []
array_bytes = []
mensagemSTR = [] #STRING DE CADA NUMERO DA MENSAGEM

# função mudaPixel, exatamente igual a do mensageiro.py
def mudaPixel(x, y):
    tuplo = (image.getpixel( (x, y) ))
    n_cores = len(tuplo)
    for i in range(n_cores):
        byte = "{0:08b}".format(tuplo[i])
        alocacao.append(byte)

def ler(array_bytes):
    print('Mensagem: ', end='') 
    oito = 0
    stringmensageira = ''
    cod = ''

    # array_bytes são os bytes das cores da imagem
    for i in range(len(array_bytes)):

        # se ele conseguir fechar um byte, ele procede no if
        if(oito==8):
            # quando cod virar um byte (oito == 8)
            # ele verifica se o 1° bit é um 1 (representando
            # uma letra)
            if(cod[:1] == '1'):
                try:
                    # ele vai tentar achar o byte dentro do dicionario,
                    # se não achar, um caractere invalido foi digitado,
                    # e vai descer pro KeyError 
                    stringmensageira += (str(letras[cod]))
                    print(letras[cod], end = '')
                except KeyError:
                    # o codigo 11010000 é um byte do caractere
                    # alt + 255, ele ta sendo usado pro final da mensagem
                    # e pra não continuar printando valores fora da mensagem
                    if(cod == '11010000'):
                        return stringmensageira
                    else:
                        # se não é um valor valido, nem um byte "especial"
                        # o caractere '>' é inserido, representando um
                        # valor invalido
                        stringmensageira += '>'
                        print('>', end = '')
            else:
                # se o inicio do byte não tem 1, quer dizer que é um
                # número entre 0 e 9
                stringmensageira += (str(int(cod, 2)))
                print(int(cod, 2), end = '')
            cod = ''
            oito = 0
        
        # se não conseguiu, ele pega o ultimo bit da posição
        # do array_bytes, e concatena na variavel cod
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

# até a chamada da função 'ler()', o programa principal é igual ao
# programa do mensageiro.py
msg = ler(alocacao)
print()
try:
    output = int(input('Deseja salvar a mensagem em um documento de texto? \n 1 - sim \n 2 - não \nDigite sua escolha: '))
except ValueError:
    # se o enter foi apertado, intencionalmente a opção 2 sera selecionada
    output = 2
    
if(output != 2):
    try: 
        # ele tenta abrir um arquivo de testo para escrita
        mensagem = open('mensagem.txt', 'w')
        mensagem.write(msg)
    
    # se o arquivo não existe, ele procede com esse erro
    except FileNotFoundError:
        # ele cria um arquivo de texto e escreve a mensagem nele
        open('mensagem.txt','x')
        mensagem = open('mensagem.txt', 'w')
        mensagem.write(msg)

    # fecha o arquivo de texto
    mensagem.close()

    input('pressione enter para fechar o programa')
exit()
