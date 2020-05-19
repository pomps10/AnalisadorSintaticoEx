def checktabelaDeSimbolos(token, index):
    global tokenGlobal
    condicao = True
    while(condicao):
        index += 1
        if listaFinal[index] == "=":
            index += 1
            if listaFinal[index] in tabelaDeSimbolos or listaFinal[index] in numeros:
                index += 1
                if listaFinal[index] in palavrasDeOperacoes:
                    index += 1
                    if listaFinal[index] in tabelaDeSimbolos or listaFinal[index] in numeros:
                        index += 1
                        if listaFinal[index] == ";":
                            tokenGlobal = index
                            return True
        else:
            tokenGlobal = index
            return False
        


def checkIPalavrasReservadas(token, index):
    global tokenGlobal
    condicao = True
    while(condicao):
        index += 1
        if listaFinal[index-1] == "if":
            # Se for if ele vai tratar de uma maneira diferente do else
            if listaFinal[index] == '(':
                index += 1
                if listaFinal[index] in tabelaDeSimbolos or listaFinal[index] in numeros:
                    index += 1
                    if listaFinal[index] in operadoresRelacionais:
                        index += 1
                        if listaFinal[index] in tabelaDeSimbolos or listaFinal[index] in numeros:
                            index += 1
                            if listaFinal[index] == ')':
                                index += 1
                                if listaFinal[index] == '{':
                                    tokenGlobal = index
                                    index += 1
                                    for x in listaFinal:
                                        index += 1
                                        if listaFinal[index] == "}":
                                            listaFinal.remove("}")
                                            return True
            tokenGlobal = index
            return False
        elif listaFinal[index] in tabelaDeSimbolos:
            # ele encontrou a variavel na tabela de simbolos
            index += 1
            if listaFinal[index] == ';':
                tokenGlobal = index
                return True
            elif listaFinal[index] == ',':
                index = index
            else:
                tokenGlobal = index
                return False
        else:
            tokenGlobal = index
            return False


def validadorSintaticoFuncao(validadorSintatico, token):
    if validadorSintatico == True:
        print('O ' + token + ' foi declarado de maneira CORRETA!')
    else:
        print('O ' + token + ' foi declarado de maneira ######## INCORRETA ########!')


# Identificadores

# - Não começam com números
# - Não pode ter caractere especial
# - Não pode ter espaço entre as letras
palavrasDeOperacoes = ['+','-','/','*']
palavrasReservadas = ['int', 'float', 'char', 'if', 'else']
operadoresRelacionais = ['>', '<', '>=', '<=', '!=', '==']
simbolosTerminais = ['=', ',', ';', '(', ')', '{', '}']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
tabelaDeSimbolos = []
arquivo = open('prof.txt', 'r')
lista = arquivo.readlines()  # readlinesssssss
arquivo.close()

print(lista)
for index, val in enumerate(lista):
    lista[index] = val.replace('\n', '')

print(lista)

for terminal in simbolosTerminais:
    for index, val in enumerate(lista):
        lista[index] = val.replace(terminal, ' ' + terminal + ' ')

print(lista)
for operador in operadoresRelacionais:
    for index, val in enumerate(lista):
        lista[index] = val.replace(operador, ' ' + operador + ' ')

print(lista)

for index, val in enumerate(lista):
    lista[index] = val.replace('  ', ' ')

print(lista)
for index, val in enumerate(lista):
    lista[index] = val.strip()

print(lista)
for index, val in enumerate(lista):
    lista[index] = val.split(' ')

print(lista)


listaFinal = []
for i in lista:
    listaFinal.extend(i)

print(listaFinal)

for index, token in enumerate(listaFinal):
    if token in palavrasReservadas:
        print(token + ' - Palavra Reservada')
    elif token in operadoresRelacionais:
        print(token + ' - Operador Relacional')
    elif token in simbolosTerminais:
        print(token + ' - Simbolo Terminal')
    elif token in numeros:
        print(token + ' - Numero')
    else:
        if listaFinal[index-1] in palavrasReservadas:
            print(token + ' - Identificador')
            tabelaDeSimbolos.append(token)

tokenGlobal = 0

# for index, token in enumerate(listaFinal):
for token in listaFinal:
    # Vai chamar a função respectiva ao o que ele é
    if tokenGlobal < len(listaFinal):
        realToken = listaFinal[tokenGlobal]
        if realToken in palavrasReservadas:
            validadorSintatico = checkIPalavrasReservadas(realToken, tokenGlobal)
        elif realToken in tabelaDeSimbolos:
            validadorSintatico = checktabelaDeSimbolos(realToken, tokenGlobal)
        validadorSintaticoFuncao(validadorSintatico, realToken)
        tokenGlobal += 1
