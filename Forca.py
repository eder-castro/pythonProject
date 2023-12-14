import random
import msg_entrada
import resultado

def jogar():
  titulo = "*             Jogo da Forca             *"
  msg_entrada.mensagem_entrada(titulo)

  arquivo = open("frutas.txt", "r")
  lista_de_palavras = []

  for linha in arquivo:
    linha = linha.strip()
    lista_de_palavras.append(linha)
  arquivo.close()

  posicao_aleatoria = random.randrange(0, len(lista_de_palavras))

  palavra_secreta = lista_de_palavras[posicao_aleatoria].upper()

  acertou = False
  enforcado = False

  letras_certas = ["_" for letra in palavra_secreta]

  chances = len(palavra_secreta)

  print(letras_certas)
  print("Voce tem {} chances".format(chances))

  while (not acertou and not enforcado):
    chute = input("Qual a letra ? ")
    chute = chute.strip().upper()

    if (chute in palavra_secreta):
      index = 0
      for letra in palavra_secreta:
        if (chute == letra):
          letras_certas[index] = letra
          print("Encontrei a letra {} na posição {}".format(chute, index))
        index += 1
      print(letras_certas)
      chances -= 1
      if chances != 0:
        print("Voce tem {} chances".format(chances))
    else:
      chances -= 1
      print("Nao encontrei a letra {} na palavra secreta".format(chute))
      print(letras_certas)
      if chances != 0:
        print("Voce tem {} chances".format(chances))

    enforcado = chances == 0
    acertou = "_" not in letras_certas
    resultado.mostrar()
  print("Jogo finalizado")


if (__name__ == "__main__"):
  jogar()
