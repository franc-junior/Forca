def imprimeLista(r):                    # Imprime a lista com as letras declaradas
    for i in r:
        print("{}".format(i), end= "") 

while True:
    tipo = int(input("\n|1-Individual | 2-Duo|\n|R: "))

    if tipo == 2:
        dica = "\nLIVRE"
        passe = str(input("\n|Digite a palavra para ser adivinhada|\n|R: "))

    elif tipo == 1:
        tipo2 = int(input("\n|      1-Animais | 2-Paises | 3-Frutas      |\n|(qualquer outro número volta para o começo)|\n|R: "))
        if tipo2 == 1: 
            dica = "\nANIMAIS"  
            listaA = ["cachorro", "cobra", "gato", "tartaruga", "macaco", "elefante", "arara", "vaca", "ovelha", "coruja"] 
        elif tipo2 == 2:
            dica = "\nPAISES"
            listaA = ["portugal", "espanha", "peru", "uruguai", "nigeria", "turquia", "alemanha", "estados unidos", "brasil", "mexico"]
        elif tipo2 == 3:
            dica = "\nFRUTAS"
            listaA = ["abacate", "abacaxi", "jabuticaba", "manga", "melancia", "pera", "pitanga", "goiaba", "coco", "carambola"]
        else:
            continue
    
    else:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n!!APENAS 1(UM) OU 2(DOIS) CARA!!\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")   
        continue

    while tipo == 1:
        tipo3 = int(input("\n|Escolha um numero entre 1 e 10|\n|R: "))

        if tipo3 >= 1 and tipo3 <= 10:  
            passe = listaA[tipo3-1]
            break
        
        else:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n!!APENAS DE 1(UM) A 10()DEZ!!\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
            continue 
        
    lista = list(passe.upper())         # Converte a palavra recebida para uma lista
    boneco = "\n!~~¬\n|  O\n| /|\ \n| / \ \n!===== " # Desenho inicial do boneco
    contErro = 0                        # contador de erros inicial
    contAcer = len(lista)               # contador de acertos inicial
    resposta = []                       # lista 2 onde será implementada as letras presentes da lista 1 (lista)
    
    for e in range(len(lista)):         # implementa caracteres(significado de vazio) de acordo com o tamanho da lista 1(lista)
        resposta.append("-")
        
    print("\n",dica,boneco)
    imprimeLista(resposta)
    
    while True:
        letras = str(input("\n|Digite uma letra|\n|R: "))
        letra = letras.upper()
        ocorrencia = passe.upper().count(letra) # mostra a quantidade de caracteres definida pela variavel 'letra' na lista 1(lista)

        if ocorrencia > 0:

            if resposta.count(letra) > 0:
                print("\n",dica,boneco)
                imprimeLista(resposta)
                print("\n\n!!VOCÊ JÁ DIGITOU ESSA LETRA MEU CHAPA!!")
                
            else: 
                while ocorrencia > 0:
                    resultado = lista.index(letra) # mostra a posição do caractere na lista 1 (lista)
                    resposta[resultado] = letra # substitui ' - ' por 'letra' na lista 2 (resposta)
                    lista[resultado] = 0 # substitui a letra que estava presente, por 0, na lista 1(lista)
                    ocorrencia -= 1
                    contAcer -= 1
            
                print("\n",dica,boneco)
                imprimeLista(resposta)

            if contAcer == 0:
                print("\n|!!!!!PARABÉNS!!!!!|\n|!!VOCÊ CONSEGUIU!!|\n        ||       ")
                reinicio = int(input("|Você deseja jogar novamente? (1-sim | 2-não)|\n|R: "))

                if reinicio == 1:
                    break

                elif reinicio == 2:
                    quit("\n|ATÉ A PROXIMA CAMPEÃO|\n")

        else:
            contErro += 1

            if contErro == 1:
                boneco = "\n!~~¬\n|  O\n| /|\ \n| /   \n!===== "
            elif contErro == 2:
                boneco = "\n!~~¬\n|  O\n| /|\ \n|     \n!===== "
            elif contErro == 3:
                boneco = "\n!~~¬\n|  O\n| / \ \n|     \n!===== " 
            elif contErro == 4:
                boneco = "\n!~~¬\n|  O\n| /   \n|     \n!===== " 
            elif contErro == 5:
                boneco = "\n!~~¬\n|  O\n|     \n|     \n!===== "
            elif contErro == 6:
                bonecofim = "!~~¬\n|   \n|     \n|     \n!=====\n\n|FIM DE JOGO!!|\n|!!VOCÊ PERDEU|\n       |       \n"
                print("{}|A PALAVRA ERA|\n|-{}-".format(bonecofim, passe.upper()))
                reinicio = int(input("\n|Você deseja jogar novamente? (1-sim | 2-não)|\n|R: "))

                if reinicio == 1:
                    break
                elif reinicio == 2:
                    quit("\n|JÁ VAI TARDE|\n")

            print("\n",dica,boneco)
            imprimeLista(resposta)
