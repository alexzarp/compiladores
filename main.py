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

def encontraColuna(afd, terminal):
    return afd[0].index(terminal)

def encontraLinha(afd, naoTerminal):
    naoTerminal = afd[1][naoTerminal]
    #print(naoTerminal)
    for linha in range(len(afd)):
        if afd[linha][0] == naoTerminal:
            return linha

# loop sob o arquivo do programador
index = 0
coluna = 0
linha = 0
for i in arq:
    for j in i:
        if j == " " or j == "\n":
            fita_saida.append(afd[linha][0])
            continue
        coluna = encontraColuna(afd, j)
        linha = encontraLinha(afd, coluna)
        
    

print(fita_saida)