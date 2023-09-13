#encoding: latin-1

#Todas as questões feitas estão neste arquivo

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
print('Foram encotradas '+str(contador)+' linhas')

#Q4 copiar um arquivo de texto.txt para copia.txt
arquivo = open('texto.txt', 'r')
copia = open('copia.txt','w+')
for linha in arquivo.readlines():
    copia.write(linha)
arquivo.close()
copia.close()

#Q5 copiar e combinar texto.txt e copia.txt para combinado.txt
arquivo = open('texto.txt', 'r')
copia = open('copia.txt','r')
combinado= open('combinado','w+')
for linha in arquivo.readlines():
    for linhaCopia in copia.readlines():   
        combinado.write(linha+linhaCopia)
arquivo.close()
copia.close()
combinado.close()

#Q6 contador de palavras em arquivo
arquivo = open('texto.txt', 'r')
texto= arquivo.read()
palavras =texto.split()
numPalavras= len(palavras)
print('Foram encontradas '+str(numPalavras)+' palavras!')
arquivo.close()


#Q7 modificar a palavra mundo do texto.txt e salvar modificado.txt
arquivo = open('texto.txt', 'r')
modificado = open('modificado.txt','w+')
texto = arquivo.read()
textoModificado = texto.replace('mundo', 'Python')
modificado.write(textoModificado)
arquivo.close()
modificado.close()

#Q8 adicione a frase "Isso é incrível!" ao final do arquivo texto.txt
arquivo = open('texto.txt', 'a')
arquivo.write('\nIsso é incrível!')
arquivo.close()

#Q9 contar letras do arquivo.txt
arquivo = open('texto.txt', 'r')
texto = arquivo.read()
texto = texto.replace(' ', '')
numLetras = sum(1 for char in texto if char.isalpha())
print('Foram encontradas '+str(numLetras)+' letras no arquivo')
arquivo.close()

#Q10 soma de números
arquivo = open('numeros.txt', 'r')
numeros = arquivo.read()
numStr = numeros.split(',')
total = sum(int(num) for num in numStr)
print(f"A soma dos números é {total}")
arquivo.close()

#Q11 relatório dos endereços IP válidos e inválidos.
arquivo = open('ips.txt', 'r')



