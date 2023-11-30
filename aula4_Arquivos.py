#encoding: latin-1

#Todas as quest�es feitas est�o neste arquivo

#Q1) criar arquivo txt com frase ola mundo
arquivo = open('texto.txt', 'w+')
arquivo.write('Ol�, mundo!')
arquivo.close()

#Q2) abrir arquivo para leitura
arquivo = open('texto.txt', 'r')
for linha in arquivo.readlines():
    print(linha)
arquivo.close()

#Q3 n�mero de linhas no arquivo
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

#Q8 adicione a frase "Isso � incr�vel!" ao final do arquivo texto.txt
arquivo = open('texto.txt', 'a')
arquivo.write('\nIsso � incr�vel!')
arquivo.close()

#Q9 contar letras do arquivo.txt
arquivo = open('texto.txt', 'r')
texto = arquivo.read()
texto = texto.replace(' ', '')
numLetras = sum(1 for char in texto if char.isalpha())
print('Foram encontradas '+str(numLetras)+' letras no arquivo')
arquivo.close()

#Q10 soma de n�meros
arquivo = open('numeros.txt', 'r')
numeros = arquivo.read()
numStr = numeros.split(',')
total = sum(int(num) for num in numStr)
print(f"A soma dos n�meros � {total}")
arquivo.close()

#Q11 relat�rio dos endere�os IP v�lidos e inv�lidos.
def verificarIp(ip):
    partes = ip.split('.')
    
    for parte in partes:
        try:
            valor = int(parte)
            if not (0 <= valor <= 255):
                return False
        except ValueError:
            return False
    
    return True

def processarEnderecos(arquivo_entrada, arquivo_saida):
    enderecosValidos = []
    enderecosInvalidos = []

    with open(arquivo_entrada, 'r') as entrada:
        for linha in entrada:
            ip = linha.strip()
            if verificarIp(ip):
                enderecosValidos.append(ip)
            else:
                enderecosInvalidos.append(ip)

    with open(arquivoSaida, 'w') as saida:
        saida.write("[Endere�os v�lidos:]\n")
        for endereco in enderecosValidos:
            saida.write(f"{endereco}\n")

        saida.write("\n[Endere�os inv�lidos:]\n")
        for endereco in enderecosInvalidos:
            saida.write(f"{endereco}\n")

arquivoEntrada = 'ips.txt'
arquivoSaida = 'relatorioIps.txt'
processarEnderecos(arquivoEntrada, arquivoSaida)

print("Relat�rio de ips gerado com sucesso.")

#Q12 No arquivo acima, o nome do usu�rio possui 15 caracteres. A partir dele, voc� devecriar um programa que gere um relat�rio, chamado "relat�rio.txt",

def bytes_megabytes(bytes):
    return bytes / (1024 ** 2)

def calcularP(espaco, espaco_total):
    return (espaco / espaco_total) * 100

def gerarRelatorio(usuarios):
    with open('relatorio.txt', 'w') as relatorio:
        relatorio.write("ACME Inc. Uso do espa�o em disco pelos usu�rios\n")
        relatorio.write("------------------------------------------------------------------------\n")
        relatorio.write("Nr. Usu�rio Espa�o utilizado % do uso\n")

        total_espaco = sum(usuarios.values())
        nr_usuario = 1

        for usuario, espaco in sorted(usuarios.items(), key=lambda x: x[1], reverse=True):
            percentual_uso = calcularP(espaco, total_espaco)
            relatorio.write(f"{nr_usuario} {usuario} {bytes_megabytes(espaco):.2f} MB {percentual_uso:.2f}%\n")
            nr_usuario += 1

        relatorio.write(f"\nEspa�o total ocupado: {bytes_megabytes(total_espaco):.2f} MB\n")
        relatorio.write(f"Espa�o m�dio ocupado: {bytes_megabytes(total_espaco / len(usuarios)):.2f} MB\n")

def lerUsuarios():
    usuarios = {}
    with open('usuarios.txt', 'r') as arquivo:
        for linha in arquivo:
            partes = linha.split()
            usuario = partes[0]
            espaco = int(partes[1])
            usuarios[usuario] = espaco
    return usuarios

usuarios = lerUsuarios()
gerarRelatorio(usuarios)
print("Relat�rio de Usu�rios gerado com sucesso.")

#Q13 Crie um programa que leia um arquivo-texto e gere um arquivo de sa�da paginado.
def paginarArquivo(entrada, saida):
    with open(entrada, 'r') as arquivo_entrada, open(saida, 'w') as arquivo_saida:
        numero_linhas_por_pagina = 60
        largura_linha = 76
        numero_pagina = 1

        for linha in arquivo_entrada:
            linha = linha.rstrip('\n')

            while len(linha) > largura_linha:
                segmento = linha[:largura_linha]
                linha = linha[largura_linha:]
                arquivo_saida.write(f"{segmento}  P�gina: {numero_pagina}, Arquivo: {entrada}\n")
                numero_pagina += 1

            arquivo_saida.write(f"{linha}  P�gina: {numero_pagina}, Arquivo: {entrada}\n")

            if numero_pagina % numero_linhas_por_pagina == 0:
                arquivo_saida.write('\f')

        print(f"Arquivo paginado gerado com sucesso: {saida}")

arquivoEntrada = 'exemplo.txt'
arquivoSaida = 'saidaPaginada.txt'

paginarArquivo(arquivoEntrada, arquivoSaida)
print("Arquivo paginado gerado com sucesso.")

#Q13 Crie um programa que leia um arquivo-texto e elimine os espa�os repetidos entre as palavras e o fim das linhas.

def arquivo(entrada, saida):
    with open(entrada, 'r') as arquivo_entrada, open(saida, 'w') as arquivo_saida:
        linhas = arquivo_entrada.readlines()

        for i, linha in enumerate(linhas):
            linha = ' '.join(linha.split())  # Eliminar espa�os repetidos
            linha = linha.rstrip()  # Eliminar espa�os no final da linha

            if i == 0 or (i > 0 and linhas[i] != linhas[i - 1]):
                arquivo_saida.write(linha + '\n')

        print(f"Arquivo processado com sucesso: {saida}")
        
arquivoEntrada = 'exemplo2.txt'
arquivoSaida = 'arquivoProcessado.txt'

arquivo(arquivoEntrada, arquivoSaida)
print("Arquivo processado sucesso.")