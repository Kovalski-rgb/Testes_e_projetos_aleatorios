# tenta abrir os arquivos especificados aqui em baixo, se der erro, ele cria um de texto p output (o outro deve ser criado pelo usuario)
try:
    opcao = input("Nome do arquivo: \n1-CrudView.html\n2-CrudController.js\n3-SpecialCrudView.html\nNome: ")
    opcao = int(opcao)
    if(opcao == 1):
        path = "CrudView.html"
    elif(opcao == 2):
        path = "CrudController.js"
    else:
        path = "SpecialCrudView.html"
except ValueError:
    path = opcao

arquivo = open(path, 'r', encoding='utf-8') 
try:
    out = open('out.txt', 'w', encoding='utf-8')
except FileNotFoundError: 
    open('out.txt','x') 
    input("Pressione enter...")
    exit()

string = [] 
frase = "" 
print("Este programa atualmente é Case Sensitive, ou seja, letras maíusculas e minúsculas são diferentes!")

try:
    padrao = input('Padrao 1 - >< \nPadrao 2 - ""\nPadrao 3 - ' +"''"+ '\nQualquer coisa menos int pra filtro customizavel: ')
    padrao = int(padrao)

    if(padrao == 1):
        print("PADRAO 1")
        strProcurada1 = '>'
        strProcurada2 = '<'
    elif(padrao == 2):
        print("PADRAO 2")
        strProcurada1 = '"'
        strProcurada2 = '"'
    else:
        print("PADRAO 3")
        strProcurada1 = "'"
        strProcurada2 = "'"

except ValueError:
    strProcurada1 = input("Inicio: ")
    strProcurada2 = input("Fim: ") 

stringProcurada1 = []
hit1 = 0  
firstHit = False

stringProcurada2 = []
hit2 = 0
secondHit = False

isThisTheFirstWord = False
linhaAtual = 1  
hits = 0 

out.write("Arquivo: "+path+"\n")
out.write("Filtros: '"+strProcurada1+"' e '"+strProcurada2+"'\n\n")

# separa os caracteres das 2 "strings" em um vetor 
for l in strProcurada1: 
    stringProcurada1.append(l) 
for l in strProcurada2:
    stringProcurada2.append(l)

'''
O bagulho que isso faz é: se o caractere bateu com a posição do caractere procurado, o contador de hits (acertos)
é incrementado, quando o total de incrementos for o tamanho da string original, a palavra foi encontrada!

Pra segunda string é a mesma coisa, mas se as 2 palavras forem as mesmas (procurar texto entre "" ou entre divs)
tem um boolean pra identificar se ela é a primeira palavra encontrada
'''
try:
    for l in arquivo.read():
        if(l == stringProcurada1[hit1]): 
            hit1 += 1
            if(hit1 == len(stringProcurada1)): 
                hits += 1
                if(not firstHit):
                    isThisTheFirstWord = True
                firstHit = True
                hit1 = 0
        else: 
            hit1 = 0

        if(l == stringProcurada2[hit2] and firstHit and not isThisTheFirstWord): 
            hit2 += 1
            if(hit2 == len(stringProcurada2)): 
                hits += 1
                secondHit = True
                hit2 = 0
        else: 
            hit2 = 0

        # quando a 2° palavra for encontrada, toda a frase que foi salva vai ser ecrita no out.txt, e td é resetado
        if(secondHit):
            frase += l
            string.append(frase)
            out.write(str(linhaAtual) + " | " + frase + " \n")
            firstHit = False
            secondHit = False
            frase = "" 
        else:
            #eu só quero que as frases sejam registradas quando a primeira palavra for encontrada, e também não quero \n no arquivo
            if(firstHit and l!="\n"):
                frase += l 
        if(l == "\n"):
            # quando for uma linha nova, incrementa 1 no contador de linhas p manter controle certinho de tudo
            linhaAtual += 1
        #vai settar o identificador da 1° palavra como falso depois de cara caractere (p nn dar erro com coisa tipo "")
        isThisTheFirstWord = False
except UnicodeDecodeError:
    out.write("\nArquivo selecionado está formatado em um formato não permitido, formate-o em UTF-8 para corrigir esse erro...\n")
    out.write(UnicodeDecodeError)
    out.close()
    input("UnicodeDecodeError")
    exit()

if( hits==0 ):
    print("Nenhuma frase ou palavra semelhante foi encontrada...")
else:
    print("Foram encontrados um total de",hits,"palavra(s) semelhante(s)!")
input("Pressione enter...")
arquivo.close()
out.close()
exit()