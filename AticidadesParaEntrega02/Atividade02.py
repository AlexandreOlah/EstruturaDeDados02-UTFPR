import os
#==============================Estrutura=Professores=====================================
class Professores:
    def __init__(self):
        self.codigo = []
        self.nome = []
        self.sexo = []
        self.idade = []
        self.area = []
        self.telefone = []
        self.n = 0                                                                 #quantidade de registros

    def setProfessores(self, codigo, nome, sexo, idade, area, telefone):
        self.codigo.append(codigo)
        self.nome.append(nome)
        self.sexo.append(sexo)
        self.idade.append(idade)
        self.area.append(area)
        self.telefone.append(telefone)
        self.n = self.n + 1

    def AltProfessores(self, codigo, nome, sexo, idade, area, telefone, n):
        self.codigo[n] = codigo
        self.nome[n] = nome
        self.sexo[n] = sexo
        self.idade[n] = idade
        self.area[n] = area
        self.telefone[n] = telefone
        self.n = n

    def getProfessores(self, n):
        return (self.codigo[n]+'|'+self.nome[n]+'|'+self.sexo[n]+'|'+self.idade[n]+'|'+self.area[n]+'|'+self.telefone[n]) 

def Tabula(codigo, nome, sexo, idade, area, telefone):
    tamCodi = 3
    tamNome = 30
    tamSexo = 1
    tamIdad = 2
    tamArea = 30
    tamTele = 14


    for Tam in range(tamCodi - len(codigo)):
        codigo = codigo + '|'
    for Tam in range(tamNome - len(nome)):
        nome = nome + ' '
    for Tam in range(tamSexo - len(sexo)):
        sexo = sexo + ' '
    for Tam in range(tamIdad - len(idade)):
        idade = idade + ' '
    for Tam in range(tamArea - len(area)):
        area = area + ' '
    for Tam in range(tamTele - len(telefone)):
        telefone = telefone + ' '
    return(codigo+'|'+nome+'|'+sexo+'|'+idade+'|'+area+'|'+telefone)    

    
#===============================Tratammento-do-Input===============================
Entrada = open("input3.txt",'r')
Entrada.seek(0,0)                                                                  #Cursor no inicio do arquivo

LinhaArquivoEntrada = (Entrada.readline()).replace('\n', '')  
if (LinhaArquivoEntrada == ''):                                                    #Verifica se o arquivo esta vazio ou em branco
  print('ERRO: Arquivo De Entrada Vazio!')
  exit()

Cabecalho = LinhaArquivoEntrada.split()
VetCabecalho = []
#VetCabecalho [0] -> valor de 'SIZE'
#VetCabecalho [1] -> valor de 'TOP'
for x in Cabecalho:
    Valor = x.split('=')
    VetCabecalho.append(Valor[1])

texto = Entrada.readlines()
#===========================Contador-Linha-Sem-Cabecalho===========================
ContLinhasSemCabecalho = 0
for z in texto:
    ContLinhasSemCabecalho = ContLinhasSemCabecalho + 1
#===============================Reescrevendo-Arquivo===============================
Temporario = open("Temporario.txt",'w+')
Temporario.seek(0,0)  
# Entrada.seek(0,0)                                                                  #Cursor no inicio do arquivo
# LinhaArquivoEntrada = (Entrada.readline()).replace('\n', '')                       #Cabeçalho

# Temporario.write('size='+VetCabecalho[0]+' top='+VetCabecalho[1]+'\n')
# for Line in range(ContLinhasSemCabecalho):
#     LinhaArquivoTemporario = (Entrada.readline()).replace('\n', '')
#     Temporario.write(LinhaArquivoTemporario)
#     Temporario.write('\n')
# Temporario.close()    
#==============================Tratamento-de-Registros========================== ===
Temporario.seek(0,0)  
LinhaArquivoTemporario = (Temporario.readline()).replace('\n', '')
Temporario.seek(0,0)  
Temporario.write('size=84 top='+str(-1)+'\n')
Entrada.seek(0,0)                                                                  #Cursor no inicio do arquivo
LinhaArquivoEntrada = (Entrada.readline()).replace('\n', '')                       #Cabeçalho

Registro = Professores()
VetCod = []

for Line2 in range(ContLinhasSemCabecalho):
    LinhaArquivoEntrada = (Entrada.readline()).replace('\n', '') 
    if (LinhaArquivoEntrada == ''):                                                #Verifica se o arquivo esta vazio
        print('ERRO -> Não há registro no arquivo')
        exit() 
    LinhaArquivoEntrada = LinhaArquivoEntrada.split('|')
    Registro.setProfessores(codigo=LinhaArquivoEntrada[0], nome=LinhaArquivoEntrada[1], sexo=LinhaArquivoEntrada[2], 
                             idade=LinhaArquivoEntrada[3], area=LinhaArquivoEntrada[4], telefone=LinhaArquivoEntrada[5])
    VetCod.append(LinhaArquivoEntrada[0]) 
    LinhaArquivoTemporario = Registro.getProfessores(Line2)
    Temporario.write(LinhaArquivoTemporario+'\n')

Temporario.seek(0,0)  
TextoTempor = (Temporario.readlines())
#===============================Tratamento-Operations==============================
Operacao = open("operations3.txt",'r')
Operacao.seek(0,0)                                                                  #Cursor no inicio do arquivo
# Temporario = open("Temporario.txt",'')
# Temporario.seek(0,0)                                                                  #Cursor no inicio do arquivo

ContOperacao = 0 #======================================Contador-Linha-Sem-Cabecalho
texto = Operacao.readlines()
for z in texto:
    ContOperacao = ContOperacao + 1

Operacao.seek(0,0)                                                                  #Cursor no inicio do arquivo
LinhaArquivoOperacao = (Operacao.readline()).replace('\n', '')  
if (LinhaArquivoOperacao == ''):                                                    #Verifica se o arquivo esta vazio ou em branco
  print('ERRO: Arquivo De Entrada Vazio!')
  exit()
Operacao.seek(0,0)                                                                  #Cursor no inicio do arquivo

Topo = -1
Top : str
aux = 0

for x in range(ContOperacao):
    LinhaArquivoOperacao = (Operacao.readline()).replace('\n', '')
    if   (LinhaArquivoOperacao[0] == 'd'):
        LinhaArquivoOperacao = LinhaArquivoOperacao.split(' ')
        CodDeletaProf = LinhaArquivoOperacao[1]
        ContVetorPos = 0 

        for c in VetCod:
            if (CodDeletaProf == VetCod[ContVetorPos]):
                VetCod[ContVetorPos] = '*'+str(Topo)
                TextoTempor[ContVetorPos+1] =  TextoTempor[ContVetorPos+1].replace(str(CodDeletaProf),('*'+str(Topo)))
                # print(TextoTempor[ContVetorPos+1])
                Topo = ContVetorPos
            ContVetorPos = ContVetorPos + 1


    elif (LinhaArquivoOperacao[0] == 'i'):
        # print('Inserindo - ',VetCod)
        LinhaArquivoOperacao = LinhaArquivoOperacao.split(',')
        LinhaArquivoOperacao[0] = LinhaArquivoOperacao[0].replace('i ','')
        # print(Topo)
        if (Topo != -1):
            Top  =  VetCod[Topo] 
            VetCod[Topo] = LinhaArquivoOperacao[0]
            Top  = Top.replace('*','') 
            Registro.AltProfessores(codigo=LinhaArquivoOperacao[0], nome=LinhaArquivoOperacao[1], sexo=LinhaArquivoOperacao[2], 
                                    idade=LinhaArquivoOperacao[3], area=LinhaArquivoOperacao[4], telefone=LinhaArquivoOperacao[5], n = int(Topo))
            # print('REante -',TextoTempor[Topo+1])  
            TextoTempor[Topo+1] = Registro.getProfessores(Topo)+'\n'              
            # print('REGISTRO -',TextoTempor[Topo+1])  
            Topo = int(Top)
        else: 
            Registro.setProfessores(codigo=LinhaArquivoOperacao[0], nome=LinhaArquivoOperacao[1], sexo=LinhaArquivoOperacao[2], 
                                    idade=LinhaArquivoOperacao[3], area=LinhaArquivoOperacao[4], telefone=LinhaArquivoOperacao[5])
            VetCod.append(LinhaArquivoOperacao[0])  
            LinhaArquivoTemporario = Registro.getProfessores(len(VetCod)-1)
            TextoTempor.append(LinhaArquivoTemporario+'\n')             
        
    else:
        print('ERRO -> A Operação não é válida!')
        exit()    

    print(VetCod)
Temporario.seek(0,0)
for m in range(len(VetCod)+1):
    if m != 0:
        VetTextoTempor = str(TextoTempor[m])
        VetTextoTempor = VetTextoTempor.split('|')
        TextoTempor[m] = Tabula(VetTextoTempor[0],VetTextoTempor[1],VetTextoTempor[2],VetTextoTempor[3],VetTextoTempor[4],VetTextoTempor[5])
        print(VetTextoTempor[0])
    Temporario.write(str(TextoTempor[m]))
Temporario.seek(0,0)
if (Topo < 10 and Topo > -1):
    Temporario.write('size=86 top='+str(Topo)+' \n')
else:    
    Temporario.write('size=86 top='+str(Topo)+'\n')
# print(Topo)

Operacao.close()
Entrada.close()

#============================Preparando-Arquivo-de-Saida===========================
Saida = open("Saida.txt",'w')
Saida.seek(0,0)
Temporario.seek(0,0)

for Escr in Temporario:
    if Escr[0] == 's':                #size=84 top=-1
        Saida.write('size=84 top=-1\n')
    elif Escr[0] != '*':
        # print(Escr.replace('\n',''))
        Saida.write(Escr)

Temporario.close()
Saida.close()