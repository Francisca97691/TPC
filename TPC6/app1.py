import pubATP as pub

myBD = pub.criarBD()

a1 = pub.criarAutor("jcr", "José Carlos Ramalho")
a2 = pub.criarAutor("prh", "Pedro Rangel Henriques")
a3 = pub.criarAutor("mf", "Miguel Ferreira")
a4 = pub.criarAutor("jj", "José João Almeida")

la1 = [a1, a2, a4]
la2 = [a1,a3]

reg1 = pub.criarRegisto("RHA2008", "Álgebra Documental", la1, 2008, "Twente - Holanda")
reg2 = pub.criarRegisto("RHA1998", "Utilização do email pedagogicamente", la1, 1999, "Universidade do Minho")
reg3 = pub.criarRegisto("FR04","Aquisição e Armazenamento de Metainformação no Contexto de um Arquivo", la2, 2004, "Faculdade de Engenharia da Universidade do Porto")
reg4 = pub.criarRegisto("FR04b", "DigitArq: Creating a Historical Digital Archive", la2, 2004, "Instituto Superior Técnico, Lisboa")

artigos = pub.criarBD()
artigos = pub.inserirReg(artigos, reg1)
artigos = pub.inserirReg(artigos, reg2)
artigos = pub.inserirReg(artigos, reg3)
artigos = pub.inserirReg(artigos, reg4)

print(artigos)