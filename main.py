import Adivinhacao
import Forca

print("*****************************************")
print("*                                       *")
print("*           Escolha um jogo             *")
print("*                                       *")
print("*****************************************", "\n")

print("1 - Forca")
print("2 - Adivinhacao")

jogo = int(input("Escolha um jogo: "))

if (jogo == 1):
  Forca.jogar()

elif (jogo == 2):
  Adivinhacao.jogar()

else:
  print("Escolha inválida!")
