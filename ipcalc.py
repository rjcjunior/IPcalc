import math 

def verificarIPV4(ip):#Função para verificar se o ip é valido
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

            
print('-----------------Menu-----------------')
print('  1) Modo de Informações')
print('  2) Modo de Divisão em Sub-redes de Tamanho Fixo')
print('  3) Modo de Divisão em Sub-redes de Tamanho Variável')

try: #Try para tratar erro, vai tentar isso
    escolhaMenu = int(input("Entre com a opção desejada: "))
except ValueError: #Se não for inteiro vai acontecer isso
      print ("Digitou uma opção invalida, vou cancelar isso")
      quit() #Sair do programa
finally: #Se for inteiro, vai vim p cá
    if (escolhaMenu > 3 or escolhaMenu < 1): #Se for um inteiro fora dos que foram passados, vai acontecer isso
      print ("Digitou uma opção invalida, vou cancelar isso")
      quit() #Sair do programa
    else:
        subrede = input("Entre com a subrede( <Endereço>/<Tam. do Prefixo> ou <Endereço> <Máscara de Sub-rede>): ") #Pegar a entrada do usuario
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
          quit() #Sair do programa
        if( not verificarIPV4(subrede[0])): #Verificar se o endereço é um ip ipv4 valido
          print ("Isso não é um IPV4")
          quit() #Sair do programa
        if (prefixo): #Validar prefixo
            try:
                if not (( 0 <= int(subrede[1]) <31 )): #VERIFICAR ESSE TAMANHO DE PREFIXO, QUAL É O MAXIMO E O MINIMO!!!!!!!
                    print("prefixo ta zoado")
                    quit() #Sair do programa
            except ValueError: #Se não for inteiro vai acontecer isso
                print ("Você não digitou um numero, vou cancelar isso")
                quit() #Sair do programa
        if(mascara): #Validar mascara
            try:
                if not(math.log(int(subrede[1]),2).is_integer()) or ( int(subrede[1])< 2): 
                    print("Essa mascara ta zoada")
                    quit()
            except ValueError: #Se não for inteiro vai acontecer isso
                print ("Você não digitou um numero, vou cancelar isso")
                quit() #Sair do programa

        
