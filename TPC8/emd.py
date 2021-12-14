
# BdEMD = [EMD]
# EMD = [id,dataEMD,pnome,unome,idade,género,morada,modalidade,clube,email,federado,resultado]
# Leitura/carregamento da informação do ficheiro

def getAtleta(linha):
    novaLinha=linha.strip("\n") # ou replace("\","") | aqui substituimos a aspa por uma string vazia
    emd=[] 
    campos=novaLinha.split(",") #Separar o texto 
    emd.append("emd"+str(int(campos[1])+1))
    for i in range(2,len(campos)):
        emd.append(campos[i])
    return emd

def lerDataset(fnome):
    # abrir o ficheiro apenas em leitura
    f = open(fnome, encoding="utf-8")
    bd = [] #criar uma lista vazia
    f.readline() #retirar o título
    #colocar o conteúdo do ficheiro e colocar dentro da Bd
    for linha in f: #correr as linhas do ficheiro
        emd=getEMD(linha)
        bd.append(emd)
    return bd 


def carregar():
    texto = open ("emd.csv")
    bd = []
    texto.readline()
    for linha in texto:
        bd.append(getAtleta(linha))
    return bd  

def contadorBD():
    contador = 0
    baseDados = []
    baseDados = carregar()
    for elemento in baseDados:
        contador += 1
    return contador

# Listagem da informação
# id | data| nome| apto

def chaveOrd(exame):
    return exame[1]

def listarDataset(bd):
    bd.sort(key=chaveOrd,reverse=True) #ORDENAR
    print ("{:<10} {:<15} {:<25} {:<8}".format('Id','Data','Nome','Apto'))
    for e in bd:
        print ("{:<10} {:<15} {:<25} {:<8}".format(e[0],e[1],e[2]+" "+e[3],e[11]))
    return 


#Lista de modalidades ordenada alfabeticamente e sem repetições.
def modalidades(bd):
    lista=[]
    for emd in bd:
        if emd[7] not in lista:
            lista.append(emd[7])
    lista.sort()
    return lista
 #os codigos das maiusculas tem valor maior que as minusculas daí BTT aparecer primeiro que badminton

#lista de pares indicando quantos EMD estÃ£o registados em cada modalidade.
def distribPorModalidade(bd):
    distribuicao={}
    for emd in bd:
        if emd[7] in distribuicao.keys():
            distribuicao[emd[7]]=distribuicao[emd[7]]+1
        else:
            distribuicao[emd[7]]=1
    return distribuicao


def distribPorClube(bd):
    distribuicao= {}
    for emd in bd:
        if emd[8] in distribuicao.keys():
            distribuicao[emd[8]]=distribuicao[emd[8]]+1
        else:
            distribuicao[emd[8]]=1
    return distribuicao


def ordAno (registo):
    return registo[1]

def distribPorAno(bd):
    # EMD = [id, dataEMD, Pnome, Unome, idade, género, morada, modalidade, clube, email, federado,resultado]
    # data : ano-mes-dia, e uma strig, o ano tem 4 numeros logo corresponde str[0:4] o quarto nao e incluido
    distribuicao = {}
    bd.sort(reverse = True, key = ordAno) #por do mais recente para o menos
    for registo in bd:
        if registo[1][0:4] in distribuicao.keys():
            distribuicao[registo[1][0:4]] = distribuicao[registo[1][0:4]]+1
        else:
            distribuicao[registo[1][0:4]] = 1
    return distribuicao #{ano : numero de emd}


def buscarCampo (campo):
    if campo == "Ano":
        return distrib(1,BD)
    elif campo == "Idade":
        return distrib(4,BD)
    elif campo == "Genero" :
        return distrib(5,BD)
    elif campo == "Morada":
        return distrib(6,BD)
    elif campo == "Modalidade":
        return distrib(7,BD)
    elif campo == "Clube" :
        return distrib(8,BD)
    elif campo == "Federado":
        return distrib(10,BD)
    elif campo == "Resultado" :
        return distrib(11,BD)

def distrib(n,bd):
    distribuicao = {}
    if n == 1 :
        return distribPorAno(bd)
    elif n == 7 :
        return distribPorModalidade(bd)
    elif n == 8 :
        return distribPorClube(bd)
    else:
        for registo in bd:
            if registo[n] in distribuicao.keys():
                distribuicao[registo[n]] = distribuicao[registo[n]]+1
            else:
                distribuicao[registo[n]] = 1
        return distribuicao #{campo : numero de emd}


import matplotlib.pyplot as plt

def plotDistribPorModalidade(bd):
    distribuicao = distribPorModalidade(bd)
    # heights of bars
    modalidade = distribuicao.values()
    height = []
    for m in modalidade :
        height.append(m)   
 
    # labels for bars
    numero_emd = distribuicao.keys() #retorna lista com as chaves, nomne dos cursos
    x = []
    i = 1
    tick_label = []
    for emd in numero_emd:
        tick_label.append(emd)
        x.append(i)
        i = i+1
 
    # plotting a bar chart
    plt.bar(x,height, tick_label = tick_label, width = 0.8)
    # naming the x-axis
    plt.xlabel('Modalidades')
    # naming the y-axis
    plt.ylabel('Número de atletas')
    # plot title
    plt.title('Distribuição por Modalidade')
    plt.show() 



def plotDistrib(campo):
    import matplotlib.pyplot as plt
    if campo == "Modalidade":
        plotDistribPorModalidade(BD)
    elif campo == "Clube":
        distribuicao = distribPorClube(BD)
        # heights of bars
        clube = distribuicao.values()
        height = []
        for c in clube :
            height.append(c)   
        # labels for bars
        numero_emd = distribuicao.keys() #retorna lista com as chaves, nomne dos cursos
        x = []
        i = 1
        tick_label = []
        for emd in numero_emd:
            tick_label.append(emd)
            x.append(i)
            i = i+1
        # plotting a bar chart
        plt.bar(x,height, tick_label = tick_label, width = 0.8)
        # naming the x-axis
        plt.xlabel('clubes')
        # naming the y-axis
        plt.ylabel('número atletas')
        # plot title
        plt.title('Distribuição por Clube')
        plt.show()
    elif campo=="Ano":
        distribuicao = distribPorAno(BD)
        # heights of bars
        ano = distribuicao.values()
        height = []
        for a in ano :
            height.append(a)   
        # labels for bars
        numero_emd = distribuicao.keys() #retorna lista com as chaves, nomne dos cursos
        x = []
        i = 1
        tick_label = []
        for emd in numero_emd:
            tick_label.append(emd)
            x.append(i)
            i = i+1
        # plotting a bar chart
        plt.bar(x,height, tick_label = tick_label, width = 0.8)
        # naming the x-axis
        plt.xlabel('ano')
        # naming the y-axis
        plt.ylabel('número atletas')
        # plot title
        plt.title('Distribuição por ano')
        plt.show()
    else:
        # heights of bars
        distribuicao = buscarCampo(campo)
        numero_emd = distribuicao.values()
        height = []
        for emd in numero_emd :
            height.append(emd)   
 
    # labels for bars
        campos = distribuicao.keys() 
        x = []
        i = 1
        tick_label = []
        for c in campos:
            tick_label.append(c)
            x.append(i)
            i = i+1
 
        # plotting a bar chart
        plt.bar(x,height, tick_label = tick_label, width = 0.8)
        # naming the x-axis
        plt.xlabel(campo)
        # naming the y-axis
        plt.ylabel('Numero emd')
        # plot title
        plt.title('Distribuição por ' + campo)
        plt.show()
    

