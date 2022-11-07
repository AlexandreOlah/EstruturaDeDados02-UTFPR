def Grep(Arquivo, Palavra):
    Contador = 0
    Final = 0
    Matriz = []
    Pos = 0

    Entrada = open(Arquivo,"r")
    Entrada.seek(0,0)                                             #Cursor no inicio do arquivo
    while Final == 0:
        Linha1 = (Entrada.readline()).replace('\n', '')  
        if Linha1 != '':            
            LinhaSlipt = Linha1.split()
            Pos = Pos + 1    
            for Pal in LinhaSlipt:
                if(Pal == Palavra):
                    Contador = Contador + 1
                    Matriz.append('Linha: '+str(Pos)+' - '+Linha1)
        else:
            Final = 1 
            return Contador, Matriz

    Entrada.close()   

Arquivo = "bloco.txt"
Palavra = "brownie"

ContPalavra, LinhasPalavra = Grep(Arquivo,Palavra) 

print('======================================================')
print('A palavra',Palavra,'foi encontrada',ContPalavra,'veze(s) a palavra foi encontrada')
print('Palavra encontrada em:')
for x in LinhasPalavra:
    print(x)
print('======================================================')