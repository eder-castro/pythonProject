def mostrar(chute, numero_secreto, pontos, rodada, chances):
  if (chute == numero_secreto):
    print("Você acertou e fez {} pontos!".format(pontos))
    exit()
  else:
    if (chute > numero_secreto):
      print("Seu chute foi maior!")
      if (rodada == chances):
        print(
                "O número secreto era {}. Você faria {} pontos se tivesse acertado"
                .format(numero_secreto, pontos))
    elif (chute < numero_secreto):
      print("Seu chute foi menor!")
      if (rodada == chances):
        print(
                "O número secreto era {}. Você faria {} pontos se tivesse acertado"
                .format(numero_secreto, pontos))
#***************
if (chances == 0 and "_" in letras_certas):
  print("Voce perdeu :(")
  print("A palavra era {}".format(palavra_secreta))
else:
  print("Parabens, voce ganhou :)")
