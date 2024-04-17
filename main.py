import Adivinhacao
import Forca
import msg_entrada
import Futebol

titulo = "*           Seleção de Jogos            *"
msg_entrada.mensagem_entrada(titulo)

print("1 - Forca")
print("2 - Adivinhacao")
print("3 - Futebol", "\n")

jogo = int(input("Escolha um jogo: "))

if (jogo == 1):
  Forca.jogar()

elif (jogo == 2):
  Adivinhacao.jogar()

elif (jogo == 3):
  Futebol.jogar()

else:
  print("Escolha inválida!")
