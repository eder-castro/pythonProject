import random

print("***********************")
print("*                     *")
print("* Jogo de adivinhação *")
print("*                     *")
print("***********************")

numero_secreto = 25
chances = 3
rodada = 1
while (rodada <= chances):
    chutxt = input("Digite seu palpite (entre 1 e 30): ")
    if (chutxt == ""):
        print("ATENÇÃO!!! Voce deve digitar um.palpite!")
        chutxt = input("Digite seu palpite (entre 1 e 30): ")
    else:
        chute = int(chutxt)
    if (chute > 30 or chute < 1):
        print("ATENÇÃO!!! Seu palpite deve estar entre 1 e 30")
    else:
        print("Rodada {} de {}".format(rodada, chances))
        if (chute == numero_secreto):
            print("Acertou, Mizeravi!")
            exit()
        else:
            if (chute > numero_secreto):
                print("Seu chute foi maior!")
            elif (chute < numero_secreto):
                print("Seu chute foi menor!")
        rodada = rodada + 1

print("Voce errou as 3 tentativas")
print("Jogo finalizado")
