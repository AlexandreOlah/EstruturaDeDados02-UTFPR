#==============================Estrutura=Musica=====================================
class Musica:
    def __init__(self):
        self.ano = []
        self.duracao = []
        self.titulo = []
        self.artista = []
        self.genero = []
        self.idioma = []
        self.n = 0                                                                 #quantidade de registros

    def setMusica(self, ano, duracao, titulo, artista, genero, idioma):
        self.ano.append(ano)
        self.duracao.append(duracao)
        self.titulo.append(titulo)
        self.artista.append(artista)
        self.genero.append(genero)
        self.idioma.append(idioma)
        self.n = self.n + 1

    def getMusica(self, n):
        return (self.ano[n]+'|'+self.duracao[n]+'|'+self.titulo[n]+'|'+self.artista[n]+'|'+self.genero[n]+'|'+self.idioma[n])
#==============================Tratammento-do-Arquivo==============================
Musicas = open("musics.txt",'r')
Musicas.seek(0,0)                                                                  #Cursor no inicio do arquivo

LinhaArquivoMusicas = (Musicas.readline()).replace('\n', '')  
if (LinhaArquivoMusicas == ''):                                                           #Verifica se o arquivo esta vazio ou em branco
  print('ERRO: Arquivo "musics.txt" Vazio!')
  exit()
#==============================Tratammento-do-Arquivo==============================
Entrada = open("entrada06.txt",'r')
Entrada.seek(0,0)                                                                  #Cursor no inicio do arquivo

LinhaArquivo = (Entrada.readline()).replace('\n', '')  
if (LinhaArquivo == '' or LinhaArquivo == ' '):                                    #Verifica se o arquivo esta vazio ou em branco
  print('ERRO: Arquivo Vazio!')
  exit()
Categoria     = LinhaArquivo    
print("Categoria = ", Categoria)
LinhaArquivo = (Entrada.readline()).replace('\n', '')  
if (LinhaArquivo == '' or LinhaArquivo == ' '):                                    #Verifica se o arquivo esta vazio ou em branco
  print('ERRO: Falta de parâmetros no arquivo!')
  exit()
DescCategoria = LinhaArquivo.upper()
print("DescCategoria = ", DescCategoria)
#==============================Tratammento-do-Cabecalho============================
Cabecalho = LinhaArquivoMusicas.split()
VetCabecalho = []
#VetCabecalho [0] -> valor de 'SIZE'
#VetCabecalho [1] -> valor de 'TOP'
#VetCabecalho [2] -> valor de 'QTDE'
#VetCabecalho [3] -> valor de 'SORT'
#VetCabecalho [4] -> valor de 'ORDER'
for x in Cabecalho:
    Valor = x.split('=')
    VetCabecalho.append(Valor[1])
#==============================Tratammento-de-Registros============================
Registro = Musica()
for y in range(int(VetCabecalho[2])):
    LinhaArquivoMusicas = (Musicas.readline()).replace('\n', '') 
    if (LinhaArquivoMusicas == ''):                                                           #Verifica se o arquivo esta vazio
        print('ERRO -> Não há registro no arquivo')
        exit() 
    LinhaArquivoMusicas = LinhaArquivoMusicas.split('|')

    Registro.setMusica(ano=LinhaArquivoMusicas[0], duracao=LinhaArquivoMusicas[1], titulo=LinhaArquivoMusicas[2], 
        artista=LinhaArquivoMusicas[3], genero=LinhaArquivoMusicas[4], idioma=LinhaArquivoMusicas[5])                 
#===========================Tratamento-Condições-de-Busca==========================
Saida = open("Saida.txt",'w')
Saida.seek(0,0)                                                                    #Cursor no inicio do arquivo
DescRegistro = ''
cont = 0
if   Categoria.upper() == "ANO":
    for i in range(int(VetCabecalho[2])):
        if Registro.ano[i] == DescCategoria:
            RegistroBusca = Registro.getMusica(i)
            print(RegistroBusca)
            Saida.write(RegistroBusca+'\n')
            cont = cont + 1
elif Categoria.upper() == "DURACAO": 
    for i in range(int(VetCabecalho[2])):
        if Registro.duracao[i] == DescCategoria:
            RegistroBusca = Registro.getMusica(i)
            print(RegistroBusca)
            Saida.write(RegistroBusca+'\n')  
            cont = cont + 1    
elif Categoria.upper() == "TITULO":   
    for i in range(int(VetCabecalho[2])):
        DescRegistro = Registro.titulo[i]
        if DescRegistro.upper() == DescCategoria:
            RegistroBusca = Registro.getMusica(i)
            print(RegistroBusca)
            Saida.write(RegistroBusca+'\n') 
            cont = cont + 1   
elif Categoria.upper() == "ARTISTA":   
    for i in range(int(VetCabecalho[2])):
        DescRegistro = Registro.artista[i]
        if DescRegistro.upper() == DescCategoria:
            RegistroBusca = Registro.getMusica(i)
            print(RegistroBusca)
            Saida.write(RegistroBusca+'\n') 
            cont = cont + 1   
elif Categoria.upper() == "GENERO":   
    for i in range(int(VetCabecalho[2])):
        # print("Registro",Registro.genero[i])
        # print("DescRegistro",DescRegistro.upper())
        DescRegistro = Registro.genero[i]
        if DescRegistro.upper() == DescCategoria:
            RegistroBusca = Registro.getMusica(i)
            print(RegistroBusca)
            Saida.write(RegistroBusca+'\n')
            cont = cont + 1    
elif Categoria.upper() == "IDIOMA": 
    for i in range(int(VetCabecalho[2])):
        DescRegistro = Registro.idioma[i]
        if DescRegistro.upper() == DescCategoria:
            RegistroBusca = Registro.getMusica(i)
            print(RegistroBusca)
            Saida.write(RegistroBusca+'\n')  
            cont = cont + 1  
else:
    print("ERRO -> Parâmetro NÃO existe") 

if cont == 0:
    print("Nenhum registro foi encontrado!\n")
    Saida.write("Nenhum registro foi encontrado!\n")        

Musicas.close()
Entrada.close()
Saida.close()    
