import sorting
#==============================Estrutura=Heroi=====================================
class Heroi:
    def __init__(self):
        self.id = []
        self.nome = []
        self.sobrenome = []
        self.apelido = []
        self.poder = []
        self.vulneravel = []
        self.origem = []
        self.profissao = []
        self.n = 0                                                                 #quantidade de registros

    def setHeroi(self, id, nome, sobrenome, apelido, poder, vulneravel, origem, profissao):
        self.id.append(id)
        self.nome.append(nome)
        self.sobrenome.append(sobrenome)
        self.apelido.append(apelido)
        self.poder.append(poder)
        self.vulneravel.append(vulneravel)
        self.origem.append(origem)
        self.profissao.append(profissao)
        self.n = self.n + 1

    def buscalinear(self,chave):
        for i in range(0,self.n,1):
            if self.id[i] == chave:
                return i 
        return -1 

    def getNome(self, n):
        return (self.nome[n])

    def getHeroi(self, n):
        return (self.id[n]+'|'+self.nome[n]+'|'+self.sobrenome[n]+'|'+self.apelido[n]+'|'+self.poder[n]+'|'+self.vulneravel[n]+'|'+self.origem[n]+'|'+self.profissao[n])
#==============================Tratammento-do-Arquivo==============================
Entrada = open("intput7.txt",'r')
Entrada.seek(0,0)                                                                  #Cursor no inicio do arquivo

LinhaArquivo = (Entrada.readline()).replace('\n', '')  
if (LinhaArquivo == '' or LinhaArquivo == ' '):                                    #Verifica se o arquivo esta vazio ou em branco
  print('ERRO: Arquivo Vazio!')
  exit()
#==============================Tratammento-do-Cabecalho============================
CabecalhoArqSaida = LinhaArquivo
Cabecalho = LinhaArquivo.split()
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
Registro = Heroi()
VetorElementos = []     
for y in range(int(VetCabecalho[2])):
    LinhaArquivo = (Entrada.readline()).replace('\n', '') 
    if (LinhaArquivo == ''):                                                           #Verifica se o arquivo esta vazio
        print('ERRO -> Não há registro no arquivo')
        exit() 
    LinhaArquivo = LinhaArquivo.split('|')
    VetorElementos.append(LinhaArquivo[0])
    #São 8 campos no registro
    Registro.setHeroi(id=LinhaArquivo[0], nome=LinhaArquivo[1], sobrenome=LinhaArquivo[2], 
                      apelido=LinhaArquivo[3], poder=LinhaArquivo[4], vulneravel=LinhaArquivo[5],
                      origem=LinhaArquivo[6],profissao=LinhaArquivo[7])
#==============================Ordenando-Vetor=====================================
#Quick Sort
if (VetCabecalho[3] == 'Q'):
    VetOrdenado = sorting.quick(VetorElementos)
#Heap Sort
elif (VetCabecalho[3] == 'H'):
    VetOrdenado = sorting.minheap(VetorElementos)
#Merge Sort
elif (VetCabecalho[3] == 'M'):
    VetOrdenado = sorting.merge(VetorElementos)
#Insertion Sort - Não tem insertion sort em "sorting", substitui pelo bubble que aprendemos em aula, claro desempenho diferentes
elif (VetCabecalho[3] == 'I'):
    VetOrdenado = sorting.bubble(VetorElementos)
#ERRO    
else:
    print('ERRO -> Não existe este sort')
    exit()
#==============================Vetor-Crescente-ou-Decrescente======================
if (VetCabecalho[4] == 'D'):
    VetOrdenado.reverse()
elif (VetCabecalho[4] != 'C'):
    print('ERRO -> Não existe esta ordenação')
    exit()    
#==============================Escrita-Ordenada-Saida==============================
Saida = open("Saida.txt",'w')
Saida.seek(0,0)                                                                    #Cursor no inicio do arquivo
Saida.write(CabecalhoArqSaida)
for l in VetOrdenado:
    for i in range(int(VetCabecalho[2])):
        if Registro.id[i] == str(l):
            RegistroBusca = Registro.getHeroi(i)
            Saida.write('\n'+RegistroBusca)

Entrada.close()
Saida.close()    