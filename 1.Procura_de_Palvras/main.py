try:
    arquivo = open('text.txt', 'r')
except FileNotFoundError:
    open('text.txt','x')
    print("Arquivo 'text.txt' criado com sucesso!")
    input("Pressione enter...")
    exit()

string = []
palavra = ""
print("Este programa atualmente é Case Sensitive, ou seja, letras maíusculas e minúsculas são diferentes!")
strProcurada = input("Digite uma palavra ou frase: ")
stringProcurada = []
hit = 0
hits = 0

for l in strProcurada:
    stringProcurada.append(l)

for l in arquivo.read():
    if(l == stringProcurada[hit]):
        hit += 1
        if(hit == len(stringProcurada)):
            print("Frase ou palavra idêntica encontrada na linha:",len(string)+1)
            hits += 1
            hit = 0
    else:
        hit = 0
    if(l == "\n"):
        string.append(palavra)
        palavra = ""
    else:
        palavra += l

if( hits==0 ):
    print("Nenhuma frase ou palavra semelhante foi encontrada...")
else:
    print("Foram encontrados um total de",hits,"palavra(s) semelhante(s)!")
input("Pressione enter...")
exit()
