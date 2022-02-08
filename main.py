import csv

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

arq = open("entrada.csv", "r")
arq = arq.readlines()
estados = []

