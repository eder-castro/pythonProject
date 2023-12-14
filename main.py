import Adivinhacao
import Forca
import msg_entrada


titulo = "*           Seleção de Jogos             *"
msg_entrada.mensagem_entrada(titulo)

print("1 - Forca")
print("2 - Adivinhacao","\n")


jogo = int(input("Escolha um jogo: "))

if (jogo == 1):
  Forca.jogar()

elif (jogo == 2):
  Adivinhacao.jogar()

else:
  print("Escolha inválida!")
