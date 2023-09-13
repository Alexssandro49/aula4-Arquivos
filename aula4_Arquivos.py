#encoding: latin-1
#Q1) criar arquivo txt com frase ola mundo
arquivo = open('texto.txt', 'w+')
arquivo.write('Olá, mundo!')
arquivo.close()

#Q2) abrir arquivo para leitura
arquivo = open('texto.txt', 'r')
for linha in arquivo.readlines():
    print(linha)
arquivo.close()

#Q3 número de linhas no arquivo
arquivo = open('texto.txt', 'r')
contador=arquivo.readlines()
contador=len(contador)
print(contador)

