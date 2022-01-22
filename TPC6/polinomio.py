# MÃ³dulo que implementa uma Ã¡lgebra sobre polinÃ³mios
# 2021-11-11
# by jcr
#
# polinomio = lista de tuplos -> tuplo = (coeficiente, expoente)
# Exemplos:
# p1 = x^2 + 2
# p2 = 7x^5 - 2x^2 - 21

p1 = [(1, 2), (2, 0)]
p2 = [(7, 5), (-2, 2), (-21, 0)]
p3 = [(1,5),(2,4),(3,3),(4,2),(5,1),(6,0)]

listaPol = [p1, p2, p3]

# criar um termo a partir de 2 inteiros
def criarTermo(coef, exp):
    return (coef, exp)

# criar um polinÃ³mio vazio
def criarPolinomio():
    return []

# inserir termo t no polinomio p
def inserirTermo(p, t): 
    return p.append(t)

# VisualizaÃ§Ã£o de um polinÃ³mio
def verTermo(t):
    c, e = t
    if e == 0 :
        return str(c)
    elif c == 1 :
        return "x^" + str(e)
    else :
        return str(c) + "x^" + str(e)
        
def verPolinomio(p):
    politexto = ""   # porque verTermo retorna em forma de str
    if len(p) != 0 : # caso p esteja vazio o resultado serÃ¡ a string vazia
        politexto = verTermo(p[0])
        for i in range(1, len(p)) :
            if p[i][0] >= 0 : # aceder ao coeficiente do termo i e ver se Ã© positivo
                politexto = politexto + " + " + verTermo(p[i])
            else : # termos de coeficiente negativo nÃ£o levam o "+"
                politexto = politexto + " " + verTermo(p[i])
    return politexto

# CÃ¡lculo do grau dum polinÃ³mio
def grauPolinomio(p):  # funÃ§Ã£o que encontra mÃ¡ximo de uma lista
    grau = p[0][1]
    for i in range(1, len(p)) :
        if p[i][1] > grau :
            grau = p[i][0]
    return grau

# CÃ¡lculo do valor dum polinÃ³mio num ponto x
def calcPolinomio(p, x):
    valor = 0
    for t in p :
        coef, exp = t
        valor = valor + (coef * (x ** exp))
    return valor

# Colocar na saÃ­da uma tabela com n linhas: x | p(x) 
def tabela(p, linhas):
    print ("x | " + str(verPolinomio(p)))
    print ("______")
    for i in range(0, linhas):
        print (str(i) + " | " + str(calcPolinomio(p, i)))

# Calcular a derivada dum polinÃ³mio: retorna um novo polinÃ³mio
def derivarPolinomio(p): 
    derivada = []
    for t in p :
        coef, exp = t
        if exp != 0 :  # quando usar condiÃ§Ã£o if exp == 0 retorna erro
            derivada.append((coef*exp, exp-1))
    return derivada

# Guardar a lista de polinÃ³mios criados
import json

def guardarBD(bd, fnome):
    with open(fnome, 'w', encoding='utf-8') as f:
        json.dump(bd, f, ensure_ascii=False, indent=4)

# Recuperar a lista de polinÃ³mios guardados
def carregarBD(fnome):
    f = open(fnome)
    bd = json.load(f)
    lista = []
    for p in bd:
        novoPol = []
        for t in p:
            novoPol.append((t[0],t[1]))
        lista.append(novoPol)
    return lista

# Criar uma vista para um BD de polinÃ³mios
def criarVista(polList):
    viewListPol = []
    cont = 1
    for p in polList:
        viewListPol.append("p" + str(cont) + ": " + verPolinomio(p))
        cont = cont +1
    return viewListPol