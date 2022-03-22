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
print(lista_tokens)

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
        token.replace("*", "")
        count += afd[nterminais].count(token)
        token = "*" + token
    else:
        count = afd[nterminais].count(token)
    
    if count > max[1]:
        max = [token, count]

state_error = max[0]
for token in range(len(fita_saida)):
    if "*" not in fita_saida[token]:
        fita_saida[token] = state_error
fita_saida.append("$")
print(fita_saida)

for error in range(len(fita_saida)):
    if fita_saida[error] == state_error:
        print("Erro na cadeia", "\"" + lista_tokens[error].replace(" ", "") + "\"","(" + fita_saida[error] + ")", "na linha", linha_tokens[error],"do arquivo de entrada.")

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

# print(slr)
for token in range (len(lista_tokens)):
    lista_tokens[token] = lista_tokens[token].replace(' ', '')

arq = open("reducoes.csv", "r")
arq = arq.readlines()
print(arq)
reducoes = []
string = ""
for i in arq:
    string = []
    string = i.split(",")
    string[-1] = string[-1].replace("\n", '')
    reducoes.append(string)

print(reducoes)
for reduce in range(len(reducoes)):
    reducoes[reduce][1] = reducoes[reduce][1].split("->")
print(reducoes)
# print(lista_tokens)
pilha = ['0']
for token in lista_tokens:
    if token == "$":
        print("Arquivo de entrada aceito e interpretado!")
        break

    try:
        index = slr[0].index(token)
    except:
        print("\"" + token + "\"", "não é conhecido. Compilação terminou.")
        break
    transicao = slr[int(pilha[-1])+1][index]

    if transicao == '':
        continue

    if transicao[0] == "s":
        pilha.append(lista_tokens[0])
        lista_tokens.pop(1)
        pilha.append(transicao[1:-1] + transicao[-1])
    
    elif transicao[0] == "r":
        for reduce in reducoes:
            if reduce[0] == (transicao[1:-1] + transicao[-1]):
                pilha.pop(-1)
                pilha.pop(-1)
                pilha.append(reduce[1])
                _index = slr[0].index(pilha)
                _transicao = slr[int(pilha[-1])+1][_index]
                pilha.append(_transicao)
                print(pilha)
                break
    
    elif transicao[0] == "a":
        print("Linguagem reconhecida e aceita!")
        break
    print(pilha)
