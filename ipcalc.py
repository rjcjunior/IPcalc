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

def validarmascara(mascara):
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
    if sub[3]<'255':
        sub[3] = str(int(sub[3])+1)  
    else:
        sub[3] = str(0)
        sub[2] = str(int(sub[2])+1)
    aux = ''
    for i in sub:
        if aux != '':
            aux += '.'
        aux += i
    return aux

    
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
        if(escolhaMenu == 2):
            tamprefixo = input("Insira um novo tamanho de prefixo, ou uma mascara de subrede: ")
            prefixo2 = False
            mascara2 = False
            if ('.' in tamprefixo):
                if not (verificarIPV4orMascara(tamprefixo)):
                    print ("Esse formato não é permitido, vou cancelar isso")  
                    os._exit(1) #Sair do programa
                tamprefixo = mascaraToPrefixo(dectobinEnd(tamprefixo)) #Vamos trabalhar com Prefixo para ficar mais facil, por isso vamos traduzir a mascara para prefixo
            else:
                if not(validarprefixo(tamprefixo)):
                    print ("Esse formato não é permitido, vou cancelar isso")  
                    os._exit(1) #Sair do programa
            if (int(tamprefixo) > int(subrede[1])):
                    print ("Prefixo maior do que o prefixo da subrede original")  
                    os._exit(1) #Sair do programa
        '''
        if(escolhaMenu == 3):
            FAZER VERIFICAÇÃO DA TERCEIRA ESCOLHA.
        '''
        #------ Fim das validações ------
        #Como a escolha 1 tem de aparecer em todas as outras, não faz sentido fazer um if para ela. Chamando ela de forma direta
        #O endereço de sub-rede (em notação decimal e em binário).
        print('')        
        print('  O Endereço da sub-rede em decimal é: ' + endprincipal(subrede[0],bintodecEnd(prefixoToMascara(subrede[1]))))
        print('  O Endereço da sub-rede em binario é: ' + dectobinEnd(endprincipal(subrede[0],bintodecEnd(prefixoToMascara(subrede[1])))))
        #O endereço de broadcast (em notação decimal e em binário).
        print('')
        #A máscara de sub-rede (em notação decimal e em binário).
        print('')
        print('  A Mascara da sub-rede em decimal é: ' + str(bintodecEnd(prefixoToMascara(subrede[1]))))
        print('  A Mascara da sub-rede em binario é: ' + str(prefixoToMascara(subrede[1])))
        #O tamanho do prefixo da sub-rede.
        print('')
        print('  O Tamanho do prefixo da sub-rede é: ' + str(subrede[1]))
        #O primeiro (i.e., menor) endereço atribuível a uma interface (em notação decimal e em binário).
        print('')
        print('  O primeiro endereço atribuivel é: ' + str(primeiroEnd(endprincipal(subrede[0],bintodecEnd(prefixoToMascara(subrede[1]))))))
        #O último (i.e., maior) endereço atribuível a uma interface (em notação decimal e em binário).
        print('')
        #O número total de endereços atribuíveis a interfaces naquela sub-rede.          
        print('')
