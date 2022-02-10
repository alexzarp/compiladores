def generate_csv(afd):
    arq = open('saida.csv', 'w')

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
lista_tokens = []
position_tokens = []
for lines in arq:
    for char in range(len(lines)):
        print(lines[char])
        if lines[char] == " " or lines[char] == "\n" or lines[char] == "\t":
            palavra = ""
            print("entrou")
            
            for letra in position_tokens:
                palavra += lines[letra]
                print(palavra)

            if palavra == '':
                continue
            lista_tokens.append(palavra)
            position_tokens = []
            continue
        else:
            position_tokens.append(char)
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
        

print(fita_saida)