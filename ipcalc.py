import os #Importado para fechar o programa


def verificarIPV4orMascara(ip):#Função para verificar se o ip ou a mascara são validos
    if (not('.' in ip)):
        return False
    aux = ip.split('.') #Ele vai pegar a string e separar em 4 pedaços, usando o '.' como "flag"
    if len(aux) != 4:
        return False# Se o array não tiver tamanho == 4, ou seja se não tiver 4 blocos, é falso
    try: #Testar condições de entrada
        return all(0<=int(p)<256 for p in aux) #Ele vai pecorrer cada posição da string, verificando se o numero está entre 0 e 255
    except ValueError: #Se for passado um valor invalido, diferente de string, é falso
        return False

def dectobin(valor): #Função para retornar o valor em binario
    valor = int(valor) #Passa o valor para inteiro, caso não seja
    valor = bin(valor) #Converte para binario
    return (str(valor[2:])) #Retorna o valor em binario, retorna a partir da segunda posição pois quando o python converte ele bota um 0b na frente do valor convertido

def bintodecEnd(valor): #Função para traduzir o endereço binario para o endereço em decimal
    retorno = '' #Variavel de retorno
    valor = valor.split('.') #Separar a string de acordo com os '.'
    for i in valor: #Pecorrer as listas geradas
        aux = '' #Variavel para armazenar o valor do bloco
        for j in i: # Passar pelo bloco i
            aux += j #Agregar o valor de cada caracter do bloco a aux
        aux = int(aux, 2) #Traduzir o bloco i para inteiro
        if (retorno != ''): #Se ele não for o primeiro
            retorno += '.' + str(aux) #Adicionar o '.' mais o valor inteiro do bloco, se ele não for o primeiro
        else: #Se for o primeiro
            retorno += str(aux) # Adicionar somente o valor traduzido se for o primeiro
    return retorno

def dectobinEnd(valor): #Função para traduzir o endereço inteiro para o endereço em binario
    retorno = '' #Variavel de retorno
    valor = valor.split('.') #Separar a string de acordo com os '.'
    for i in valor: #Pecorrer as listas geradas
        aux = '' #Variavel para armazenar o valor do bloco
        for j in i: # Passar pelo bloco i
            aux += j #Agregar o valor de cada caracter do bloco a aux
        aux = dectobin(aux) #Traduzir o bloco i para binario
        if (len(aux)< 8): #Adicionar '0's até que o tamanho seja de 8 caracteres
            aux = ((8-len(aux))*'0') + aux
        if (retorno != ''): #Se ele não for o primeiro
            retorno += '.' + str(aux) #Adicionar o '.' mais o valor inteiro do bloco, se ele não for o primeiro
        else: #Se for o primeiro
            retorno += str(aux) # Adicionar somente o valor traduzido se for o primeiro
    return retorno


def prefixoToMascara(prefixo): #Função para traduzir o prefixo para mascara
    aux = ''    
    mascara = ''
    for i in range(1,33):
        if i<=int(prefixo): #Verificar se i é menor ou igual ao prefixo, sendo o prefixo a variavel controladora
            aux += '1' #Se for menor ou igual, adiciona o 1 pq ainda não chegou na contagem
        else:
            aux += '0' #Se for maior, adiciona o 0 pois já passou do tamanho do prefixo
        if (i%8==0) and (i!=32): #Adicionar um '.' a cada 8 caracteres
            aux+='.'    
    return aux

def mascaraToPrefixo(mascara): #Função para traduzir a mascara para o prefixo
    return mascara.count('1')

def endprincipal(sub, mascara): #Função para retornar o endereço da subrede
    aux = '' #Variavel para armazenar o valor do bloco
    sub = sub.split('.') #Separar o endereço em blocos, de acordo com o '.'
    mascara = mascara.split('.') #Separar o endereço em blocos, de acordo com o '.'
    for i in range(0,4): 
        if (aux!= ''): #Se ele não for o primeiro
            aux += '.' #Adicionar o '.' mais o valor  do bloco, se ele não for o primeiro
        aux += str(int(sub[i])&int(mascara[i])) #Fazer o AND BIT-A-BIT nos valores
    return aux        

def validarprefixo(prefixo): #Função para fazer a validação do prefixo
    try:
        if not (( 0 <= int(prefixo) <= 32 )): #VERIFICAR ESSE TAMANHO DE PREFIXO!!!
            print("prefixo ta zoado")
            os._exit(1) #Sair do programa
        else:
            return True
    except ValueError: #Se não for inteiro vai acontecer isso
        print ("Você não digitou um numero, vou cancelar isso")
        os._exit(1) #Sair do programa

def validarmascara(mascara): #Função para fazer a validação da mascara
    try:
        if( not verificarIPV4orMascara(subrede[1])): #Se não tiver no formato xxx.xxx.xxx.xxx e se os numeros estão abaixo de 0 ou acima de 255
            print("Essa mascara ta zoada")
            os._exit(1)
        else:
            return True
    except ValueError: #Se não for inteiro vai acontecer isso
        print ("Você digitou coisa errada, vou cancelar isso")
        os._exit(1) #Sair do programa

def primeiroEnd(sub): #Função para retornar o primeiro endereço atribuivel
    sub = sub.split('.') #Separar em blocos
    if sub[3]!='255': #Se o ultimo bloco for menor que 255( Flag maximo)
        sub[3] = str(int(sub[3])+1)  #Só somar mais um
    else: #Se for 255
        sub[3] = str(0) #O ultimo bloco vai ser 0 
        sub[2] = str(int(sub[2])+1) #O terceiro bloco vai ser ele + 1
    aux = '' #Auxiliar para o retorno
    for i in sub: #Pecorrer todo a nova subrede
        if aux != '': #Adicionar 1 '.' para cada novo bloco depois do primeiro
            aux += '.'
        aux += i #Agregar o bloco i a variavel de retorno
    return aux


def ultimoEnd(mascara): #Função para retornar o ultimo endereço atribuivel
    mascara = mascara.split('.') #Separar em blocos
    if mascara[3] == '0': #Se o ultimo bloco for 0 (Flag minimo)
        mascara[3] = str(255) #Colocar 255 no terceiro bloco
        mascara[2] = str(int(mascara[2])-1) #Diminuir o segundo bloco em 1
    else:#Se não for 0 
        mascara[3] = str(int(mascara[3])-1) #Só dimunir 1 valor
    aux = '' #Auxiliar para o retorno
    for i in mascara:  #Pecorrer todo a nova subrede
        if aux != '': #Adicionar 1 '.' para cada novo bloco depois do primeiro
            aux += '.'
        aux += i #Agregar o bloco i a variavel de retorno
    return aux

def broadcast(sub, mascara):
    aux = ''
    for i in mascara:
        if i == '0':
            aux += '1'
        elif i == '1':
            aux += '0'
        else:
            aux += '.'
    retorno = ''
    cont = 0
    for i in sub:
        if i == '1' or aux[cont] == '1':
            retorno += '1'
        elif i == '.':
            retorno += '.'
        else:
            retorno += '0'
        cont+= 1
    return retorno    

def maxend (mascara): #Retornar o numero maximo de endereços atribuives
    aux = mascara.count('0') #contar o numeros de 0 na mascara
    return (2**(int(aux))-2) #Usar e retornar função (2^n)-2 que é o numero de endereços maximos atribuives

def modoinfo(subrede, mascara): #Função para exibir o modo de informações
    #O endereço de sub-rede (em notação decimal e em binário).
    print('')        
    print('  O Endereço da sub-rede em decimal é: ' + endprincipal(subrede,bintodecEnd(prefixoToMascara(mascara))))
    print('  O Endereço da sub-rede em binario é: ' + dectobinEnd(endprincipal(subrede,bintodecEnd(prefixoToMascara(mascara)))))
    #O endereço de broadcast (em notação decimal e em binário).
    print('')
    print('  O Endereço broadcast em decimal é: ' + bintodecEnd(broadcast(dectobinEnd(subrede),prefixoToMascara(mascara))))
    print('  O Endereço broadcast em binario é: ' + broadcast(dectobinEnd(subrede),prefixoToMascara(mascara)))
    #A máscara de sub-rede (em notação decimal e em binário).
    print('')
    print('  A Mascara da sub-rede em decimal é: ' + str(bintodecEnd(prefixoToMascara(mascara))))
    print('  A Mascara da sub-rede em binario é: ' + str(prefixoToMascara(mascara)))
    #O tamanho do prefixo da sub-rede.
    print('')
    print('  O Tamanho do prefixo da sub-rede é: ' + str(mascara))
    #O primeiro (i.e., menor) endereço atribuível a uma interface (em notação decimal e em binário).
    print('')
    print('  O Primeiro endereço atribuivel é: ' + str(primeiroEnd(endprincipal(subrede,bintodecEnd(prefixoToMascara(mascara))))))
    #O último (i.e., maior) endereço atribuível a uma interface (em notação decimal e em binário).
    print('')
    print('  O Ultimo endereço atribuivel é: ' + str(ultimoEnd(bintodecEnd(broadcast(dectobinEnd(subrede),prefixoToMascara(mascara))))))
    #O número total de endereços atribuíveis a interfaces naquela sub-rede.          
    print('  O Numero maximo de endereços atribuíves é: ' + str(maxend(str(prefixoToMascara(mascara)))))
    print('  O Numero maximo de hosts é: ' + str(numhost(str(prefixoToMascara(mascara)))))
    
def tamfixo(subrede, mascara, prefixo):
    cont = 1
    newmaxend = maxend(prefixoToMascara(prefixo))
    first = endprincipal(subrede,bintodecEnd(prefixoToMascara(mascara)))
    while (cont <= numhost(str(prefixoToMascara(prefixo)))):
        print("\n Subrede " + str(cont) +':')
        print('  O Endereço da sub-rede em decimal é: ' + first)
        print('  O Endereço da sub-rede em binario é: ' + dectobinEnd(first))
        #O endereço de broadcast (em notação decimal e em binário).
        print('')
        print('  O Endereço broadcast em decimal é: ' + bintodecEnd(broadcast(dectobinEnd(first),prefixoToMascara(prefixo))))
        print('  O Endereço broadcast em binario é: ' + broadcast(dectobinEnd(first),prefixoToMascara(prefixo)))
        #A máscara de sub-rede (em notação decimal e em binário).
        print('')
        print('  A Mascara da sub-rede em decimal é: ' + str(bintodecEnd(prefixoToMascara(prefixo))))
        print('  A Mascara da sub-rede em binario é: ' + str(prefixoToMascara(prefixo)))
        #O tamanho do prefixo da sub-rede.
        print('')
        print('  O Tamanho do prefixo da sub-rede é: ' + str(prefixo))
        #O primeiro (i.e., menor) endereço atribuível a uma interface (em notação decimal e em binário).
        print('')
        print('  O Primeiro endereço atribuivel é: ' + str(primeiroEnd(first)))
        #O último (i.e., maior) endereço atribuível a uma interface (em notação decimal e em binário).
        print('')
        print('  O Ultimo endereço atribuivel é: ' + str(ultimoEnd(bintodecEnd(broadcast(dectobinEnd(first),prefixoToMascara(prefixo))))))
        #O número total de endereços atribuíveis a interfaces naquela sub-rede.          
        print('  O Numero maximo de endereços atribuíves é: ' + str(maxend(str(prefixoToMascara(prefixo)))))
        aux2 = ultimoEnd(bintodecEnd(broadcast(dectobinEnd(first),prefixoToMascara(prefixo)))).split('.')
        if aux2[3]!='255': #Se o ultimo bloco for menor que 255( Flag maximo)
            aux2[3] = str(int(aux2[3])+2)  #Só somar mais um
        else: #Se for 255
            aux2[3] = str(0) #O ultimo bloco vai ser 0 
            aux2[2] = str(int(aux2[2])+1) #O terceiro bloco vai ser ele + 1
        first = '' #Auxiliar para o retorno
        for i in aux2: #Pecorrer todo a nova subrede
            if first != '': #Adicionar 1 '.' para cada novo bloco depois do primeiro
                first += '.'
            first += i #Agregar o bloco i a variavel de retorno
        cont+=1

            
def numhost(mascara):
    mascara = mascara.split('.')
    if '1' in mascara[3]:
        aux = mascara[3].count('1') #contar o numeros de 0 na mascara
        return (2**(int(aux))) #Usar e retornar função (2^n)-2 que é o numero de endereços maximos atribuives    
    else:
        if '1' in mascara[2]:
            aux = mascara[2].count('1') #contar o numeros de 0 na mascara
            return (2**(int(aux))) #Usar e retornar função (2^n)-2 que é o numero de endereços maximos atribuives    
    return 2

print('-----------------Menu-----------------')
print('  1) Modo de Informações')
print('  2) Modo de Divisão em Sub-redes de Tamanho Fixo')
print('  3) Modo de Divisão em Sub-redes de Tamanho Variável')

try: #Try para tratar erro, vai tentar isso
    escolhaMenu = int(input("  Entre com a opção desejada: "))
except ValueError: #Se não for inteiro vai acontecer isso
      print ("Digitou uma opção invalida, vou cancelar isso")
      os._exit(1) #Sair do programa
finally: #Se for inteiro, vai vim p cá
    if (escolhaMenu > 3 or escolhaMenu < 1): #Se for um inteiro fora dos que foram passados, vai acontecer isso
      print ("Digitou uma opção invalida, vou cancelar isso")
      os._exit(1) #Sair do programa
    else:
        subrede = input("  Entre com a subrede( <Endereço>/<Tam. do Prefixo> ou <Endereço> <Máscara de Sub-rede>): ") #Pegar a entrada do usuario
        prefixo = False #Flag para saber se ele usou prefixo
        mascara = False #Flag para saber se ele usou mascara de subrede
        if ( '/' in subrede):   #Verificar se tem '/' na entrada do usuario( Formato 1)
            subrede = subrede.split('/') #Se tiver, ele vai separar o endereço do prefixo
            prefixo = True
        elif ( ' ' in subrede): #Verificar se tem ' ' na entrada do usuario( Formato 2)
            subrede = subrede.split(' ') #Se tiver, ele vai separar o endereço da mascara
            mascara = True
        else: #Se veio para cá, é porque ele tentou um formato que diferente do que eu falei, vou cancelar
          print ("Esse formato não é permitido, vou cancelar isso")  
          os._exit(1) #Sair do programa
        if( not verificarIPV4orMascara(subrede[0])): #Verificar se o endereço é um ip ipv4 valido
          print ("Isso não é um IPV4")
          os._exit(1) #Sair do programa
        if (prefixo):
            validarprefixo(subrede[1]) #Validar prefixo
        if(mascara): #Validar mascara
            validarmascara(subrede[1])
            subrede[1] = mascaraToPrefixo(dectobinEnd(subrede[1])) #Vamos trabalhar com Prefixo para ficar mais facil, por isso vamos traduzir a mascara para prefixo
            validarprefixo(subrede[1])
        if(escolhaMenu == 2):
            tamprefixo = input("Insira um novo tamanho de prefixo, ou uma mascara de subrede: ")
            if ('.' in tamprefixo):
                if not (verificarIPV4orMascara(tamprefixo)):
                    print ("Esse formato não é permitido, vou cancelar isso")  
                    os._exit(1) #Sair do programa
                tamprefixo = mascaraToPrefixo(dectobinEnd(tamprefixo)) #Vamos trabalhar com Prefixo para ficar mais facil, por isso vamos traduzir a mascara para prefixo
                validarprefixo(tamprefixo)
            else:
                if not(validarprefixo(tamprefixo)):
                    print ("Esse formato não é permitido, vou cancelar isso")  
                    os._exit(1) #Sair do programa
            if (int(tamprefixo) < int(subrede[1])):
                    print ("Prefixo maior do que o prefixo da subrede original")  
                    os._exit(1) #Sair do programa
        '''
        if(escolhaMenu == 3):
            FAZER VERIFICAÇÃO DA TERCEIRA ESCOLHA.
        '''
        #------ Fim das validações ------
        modoinfo(subrede[0],subrede[1]) #Chamar o modo de informações para qualquer opção, pois ele será mostrado em todas elas
        if (escolhaMenu == 1):
          print ("\n  Pronto, não tenho mais nada para mostrar, vou encerrar")
          os._exit(1) #Sair do programa
        elif (escolhaMenu == 2):
            tamfixo(subrede[0], subrede[1], tamprefixo)
        #else: Parte 3    
