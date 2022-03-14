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

lista_tokens_SLR = []
position_tokens = []
for char in arq[0]:
    if char == "$":
        break
    if char == ",":
        palavra = ""
        for letra in position_tokens:
            palavra += letra
        position_tokens = []
        lista_tokens_SLR.append(palavra)
    else:
        position_tokens.append(char)

for token in range(len(lista_tokens)):
    lista_tokens[token] = lista_tokens[token].replace(" ", "")
position_tokens = []
for token in lista_tokens_SLR:
    if token in lista_tokens:
        index = lista_tokens.index(token)
        position_tokens.append(index)
if lista_tokens_SLR[0] == "index":
    lista_tokens_SLR.pop(0)
for index in position_tokens:
    lista_tokens_SLR[index] = fita_saida[index]

print(fita_saida)
print(lista_tokens)
print(lista_tokens_SLR)