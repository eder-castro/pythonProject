import random

import msg_entrada
import resultado


def jogar():
  titulo = "*          Jogo de adivinhação          *"
  msg_entrada.mensagem_entrada(titulo)

  print("1 - FÁCIL - 10 chances")
  print("2 - MÉDIO - 06 chances")
  print("3 - DIFÍCIL - 03 chances", "\n")

  nivel = input("Escolha um nível para jogar: ")
  level = int(nivel)
  rodada = 1
  numero_secreto = round(random.randrange(1, 31))
  pontos = 100

  if (level == 1):
    chances = 10
  elif (level == 2):
    chances = 6
  else:
    chances = 3

  while (rodada <= chances):
    print("Rodada {} de {}".format(rodada, chances))
    chutxt = input("Digite seu palpite (entre 1 e 30): ")
    if (chutxt == ""):
      print("ATENÇÃO!!! Você deve digitar um palpite!")
      continue
    else:
      chute = int(chutxt)
    if (chute > 30 or chute < 1):
      print("ATENÇÃO!!! Seu palpite deve estar entre 1 e 30")
    else:
      resultado.mostrar_adiv(chute, numero_secreto, pontos, rodada, chances)
      rodada = rodada + 1
      pontos = pontos - abs(numero_secreto - chute)


if (__name__ == "__main__"):
  jogar()
