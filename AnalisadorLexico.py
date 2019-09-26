from beautifultable import BeautifulTable

plv_reservadas = ['auto','main','break','case','char','const','continue','default','do','double','else','enum','extern','float','for','goto','if','int','long','register','return','short','signed','sizeof','static','struct','switch','typedef','union','unsigned','void','volatile','while','print','printf']
simbolos_especiais = ['.',';',',','(',')',':','+','<','>','-','*','%','=','"','{','}','[',']']

table = BeautifulTable()
table.column_headers = ["LINHA", "TOKEN", "SÍMBOLO"]

linha = 0

#ler arquivo TXT
with open("teste.txt") as file:
    var = file.readlines()
    for line in var:
        line = line.replace("\t","")
        line = line.replace("\n","")
        if (len(line) > 0):
            linha += 1

            palavras = line.split()

            if(line[0] == "#"):
                simb = "Biblioteca"
                table.append_row([linha,line,simb])

            cont = 0
            for plv in palavras:
                if(plv in plv_reservadas):
                    simb = "Palavra Reservada"
                    table.append_row([linha,plv,simb])
                    if(palavras[cont+2] == "="):
                        simb = "Variável"
                        table.append_row([linha,palavras[cont+1],simb])

                if(plv in simbolos_especiais):
                    simb = "Símbolos Especiais"
                    table.append_row([linha,plv,simb])
        
print (table)
