def generate_csv(afd):
    arq = open('output.csv', 'w')

    for i in range(len(afd)):
        for j in range(len(afd[i])):
            arq.write(afd[i][j])
            arq.write(';')
        arq.write('\n')
    
    arq.close()

arq = open("output.csv", "r")
arq = arq.readlines()

afd = []
string = ""
for i in arq:
    string = []
    string = i.split(",")
    string[-1] = string[-1].replace("\n", '')
    afd.append(string)

fita_saida = []
arq = open("entrada_linguagem.txt", "r")
arq = arq.readlines()
if arq[-1][-1] != "\n":
    arq[-1] += "\n"
lista_tokens = []
linha_tokens = []
linha = 0
position_tokens = []
for lines in arq:
    for char in range(len(lines)):
        if lines[char] == " " or lines[char] == "\n" or lines[char] == "\t":
            palavra = ""
            for letra in position_tokens:
                palavra += lines[letra]

            if palavra == '':
                continue
            lista_tokens.append(palavra)
            linha_tokens.append(linha)
            position_tokens = []
            continue
        else:
            position_tokens.append(char)
    linha += 1
for tokens in range(len(lista_tokens)):
    lista_tokens[tokens] += " "

def encontraColuna(afd, terminal):
    return afd[0].index(terminal)

def encontraLinha(afd, linha, naoTerminal):
    temp = ""
    naoTerminal = afd[linha][naoTerminal]
    for linhaa in range(len(afd)):
        temp = afd[linhaa][0]
        if "*" in temp:
            temp = temp.replace('*', '')
        if temp == naoTerminal:
            return linhaa

# loop sob o arquivo do programador
coluna = 0
linha = 1
for token in lista_tokens:
    for caracter in token:
        if caracter == " ":
            fita_saida.append(afd[linha][0])
            linha = 1
            continue
        coluna = encontraColuna(afd, caracter)
        linha = encontraLinha(afd, linha, coluna)

lista_tokens.append('$')
token = ""
count = 0
max = ["", 0]
for nterminais in range(len(afd)):
    token = afd[nterminais][0]
    if "*" in token:
        count = afd[nterminais].count(token)
        token = token.replace("*", "")
        count += afd[nterminais].count(token)
        token = "*" + token
    else:
        count = afd[nterminais].count(token)
    
    if count > max[1]:
        max = [token, count]

state_error = max[0]
for token in range(len(fita_saida)):
    # if "*" not in fita_saida[token]:
    if state_error == fita_saida[token]:
        fita_saida[token] = state_error
fita_saida.append("$")

flag = False
for error in range(len(fita_saida)):
    if fita_saida[error] == state_error:
        print("Erro na cadeia", "\"" + lista_tokens[error].replace(" ", "") + "\"","(" + fita_saida[error] + ")", "na linha", linha_tokens[error],"do arquivo de entrada.")
        flag = True
if flag:
    exit()

arq = open("tableSLR.csv", "r")
arq = arq.readlines()

slr = []
string = ""
for i in arq:
    string = []
    string = i.split(",")
    string[-1] = string[-1].replace("\n", '')
    slr.append(string)
# :D

for token in range (len(lista_tokens)):
    lista_tokens[token] = lista_tokens[token].replace(' ', '')

arq = open("reducoes.csv", "r")
arq = arq.readlines()
reducoes = []
string = ""
for i in arq:
    string = []
    string = i.split(",")
    string[-1] = string[-1].replace("\n", '')
    reducoes.append(string)

for reduce in range(len(reducoes)):
    reducoes[reduce][1] = reducoes[reduce][1].split("->")
for reduce in range(len(reducoes)):
    reducoes[reduce].append(reducoes[reduce][1][0])
    reducoes[reduce].append(reducoes[reduce][1][1])
    reducoes[reduce].pop(-3)

pilha = ['0']
while (True):
    # print(pilha)
    token = lista_tokens[0]
    try:
        index = slr[0].index(token)
    except:
        print("\"" + token + "\"", "não é conhecido. Compilação terminou.")
        break
    try:
        transicao = slr[int(pilha[-1])+1][index]
    except:
        print("\"" + pilha[-2] + "\"", "não contém um estado para transicionar. Transição caiu em local vazio da SLR.")
        break

    if transicao == '':
        print("\"" + token + "\"", "caiu em local vazio da SLR, compilação terminada!")
        break

    if transicao[0] == "s":
        pilha.append(lista_tokens[0])
        lista_tokens.pop(0)
        pilha.append(transicao[1:-1] + transicao[-1])
    
    elif transicao[0] == "r":
        for reduce in reducoes:
            if reduce[0] == (transicao[1:-1] + transicao[-1]):
                count = len(reduce[2].split(" ")) *2
                for i in range(count):
                    pilha.pop(-1)
                pilha.append(reduce[1])
                index = slr[0].index(pilha[-1])
                try:
                    empilhado = slr[int(pilha[-2])+1][index]
                except:
                    print("\"" + pilha[-2] + "\"", "não é uma transição válida!")
                    exit()
                pilha.append(empilhado)
                break

    elif transicao[0] == "a":
        print("Linguagem reconhecida e aceita!")
        break