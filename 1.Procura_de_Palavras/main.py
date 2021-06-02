try: #testa a linha de baixo
    arquivo = open('text.txt', 'r') #no caso essa linha tenta abrir o arquivo text.txt
except FileNotFoundError: #ele roda isso se der esse erro especifico
    open('text.txt','x') #o modo x dentro do open cria um arquivo
    print("Arquivo 'text.txt' criado com sucesso!") #o modo r dentro do open ali no try é pra ler o arquivo
    input("Pressione enter...")
    exit()

string = [] #lista string que recebe todas as palavras do arquivo
frase = "" #serve pra receber a frase antes de entrar dentro da lista uma linha em cima
print("Este programa atualmente é Case Sensitive, ou seja, letras maíusculas e minúsculas são diferentes!")
strProcurada = input("Digite uma palavra ou frase: ") 
stringProcurada = [] #string procurada
hit = 0 #serve pra marcar que a letra atual bateu com a letra digitada
hits = 0 #serve pra contar quantos "matches" foram achados

for l in strProcurada: #ele pega todos os caracteres dentro da variavel strProcurada, um por um
    stringProcurada.append(l) #e insere dentro da lista stringProcurada, na ultima posição

for l in arquivo.read(): #isso basicamente trata o arquivo inteiro como uma lista, sendo cada caractere (e break line) como um elemento
    if(l == stringProcurada[hit]): #se o caractere l é igual ao caractere dentro da lista
        hit += 1
        if(hit == len(stringProcurada)): #se o total de acertos seguidos equivale ao total de caracteres da frase digitada
            print("Frase ou palavra idêntica encontrada na linha:",len(string)+1) #ele printa qual linha ele ta agora (len(string))
            hits += 1
            hit = 0
    else: #se não bateu a letra atual com a digitada, o contador de letras iguais é reiniciado
        hit = 0
    if(l == "\n"): #agora se chegou no final da linha de uma frase
        string.append(frase) #toda a string que tava sendo concatenada ali em baixo é inserida nessa lista
        frase = "" #e a string é limpada também
    else:
        frase += l #agora se não chegou no final da linha o caractere atual é concatenado na string

if( hits==0 ):
    print("Nenhuma frase ou palavra semelhante foi encontrada...")
else:
    print("Foram encontrados um total de",hits,"palavra(s) semelhante(s)!")
input("Pressione enter...")
exit() #espero que esteja bem comentado, se tiver alguma duvida, abra um issue perguntando sobre, só lembre de colocar o link do programa, mais ou menos assim "tenho duvida (nesse)[url vem aqui] programa"
