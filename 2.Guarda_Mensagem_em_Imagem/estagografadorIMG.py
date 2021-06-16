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

#função pra deixar tudo padrão, da pra editar tudo aqui
def mudaPixel(x, y):
    contador = 0
    if(x > 0):#width-1):
        tuplo = (image.getpixel( (x, y) ))
        for i in range(3):
            print(tuplo[i], end = ' decimal | ')
            byte = "{0:08b}".format(tuplo[i])
            print('byte',byte,'| posicão na cor: ',i,'| cor:',tuplo)
            contador += 1
    return contador

# creating a image object
image = Image.open(open_file) 
width, height = image.size

print('w:',width)
print('h:',height)

if(width>height):
    print('Height') #dependendo da imagem ela crasha o python :/
    for x in range(height):
        for y in range(width):
            contador += mudaPixel(y, x)
else:
    print('Width')
    for x in range(width):
        for y in range(height):
            contador += mudaPixel(x, y)

#image.save('MODIFICADO.png')
print('bytes(caracteres) disponiveis para mensagem:',((contador)/16))
input('pressione enter: ')
image.show()