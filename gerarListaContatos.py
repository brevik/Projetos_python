
#PROGRAMA PARA GERAR LISTA DE CONTATOS PARA ENVIO DE MENSAGENS AUTOMATICA

arquivo = open("contatos.txt", "r")
qntLinhas = arquivo.readlines()
n = len(qntLinhas)

arq = open("1.txt","w")
q = 0
cont = 1
for z in qntLinhas:
	if q % 200 == 0:
		arq.close()
		arq = open(str(cont) + ".txt", "w")
		cont = cont + 1
	
	arq.write(z)
	q = q + 1

print(q)