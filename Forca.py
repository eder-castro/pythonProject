def jogar():
    print("*****************************************")
    print("*                                       *")
    print("*             Jogo da Forca             *")
    print("*                                       *")
    print("*****************************************","\n")

    palavra_secreta = "abacaxi"
    acertou = False
    enforcado = False
    letras_certas = ["_",'_',"_","_","_","_","_"]
    
    print(letras_certas)
  
    while (not acertou and not enforcado):
        chute = input("Qual a letra ? ")
        chute = chute.strip()
        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {}".format(chute, index))
                letras_certas[index] = letra
            index = index + 1

        print(letras_certas)

    print("Jogando Forca")
    print("Jogo finalizado")

if (__name__ == "__main__"):
    jogar()