-- 27/11/2023
import random

print ("***********************")
print ("*                     *")
print ("* Jogo de adivinhação *")
print ("*                     *")
print ("***********************")

print("1 - FÁCIL - 10 chances")
print("2 - MÉDIO - 06 chances")
print("3 - DIFÍCIL - 03 chances")

nivel = input("Escolha um nivel para jogar:")
level = int (nivel)

numero_secreto = round(random.randrange(1, 31))

if (level == 1):
    chances = 10
elif (level == 2):
        chances = 6
else:
        chances = 3
        print (chances)

rodada = 1
while (rodada <= chances): 
    print ("Rodada {} de {}".format(rodada, chances))
    chutxt = input ("Digite seu palpite (entre 1 e 30): ")
    if (chutxt == ""):
        print ("ATENÇÃO!!! Voce deve digitar um.palpite!")
        continue
    else:
            chute = int(chutxt)
    if (chute > 30 or chute < 1):
        print ("ATENÇÃO!!! Seu palpite deve estar entre 1 e 30")
    else:
        if (chute == numero_secreto):
          print ("Acertou, Mizeravi!")
          break
        else:
            if (chute > numero_secreto):
              print ("Seu chute foi maior!")
            elif (chute < numero_secreto):
              print ("Seu chute foi menor!")
        rodada = rodada + 1  
      
print ("Jogo finalizado")
  