def mostrar_adiv(chute, numero_secreto, pontos, rodada, chances):
  if (chute == numero_secreto):
    print("PARABÉNS! Você acertou o número secreto!")
    print("Você fez {} pontos!".format(pontos))
    trofeu()
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


def mostrar_forca(chances, letras_certas, palavra_secreta, enforcado, acertou):
  if enforcado:
    print("A palavra era {}".format(palavra_secreta))
    print("""          
                      @@@@@@@@@@@@@@@@@@@@@@@                       
                   @@@@                     @@@@              
                 @@@                           @@@            
                @@@                              @@@           
              @@ @@                              @@ @@          
              @@ @@                              @@ @@          
              @@  @@                            @@  @@          
              @@  @@                            @@  @@          
               @@ @@   @@@@@@@@     @@@@@@@@    @@ @@           
                @@@@ @@@@@@@@@@     @@@@@@@@@@ @@@@@           
                 @@@ @@@@@@@@@@     @@@@@@@@@@ @@@                  VOCÊ FOI ENFORCADO!!!
        @@@       @@  @@@@@@@@       @@@@@@@@@  @@      @@@@        
       @@@@@     @@   @@@@@@@   @@@   @@@@@@@   @@     @@@@@@  
      @@   @@    @@     @@@    @@@@@    @@@     @@    @@   @@  
     @@@    @@@@  @@          @@@@@@@          @@  @@@@    @@@ 
    @@         @@@@@@@@       @@@@@@@       @@@@@@@@@        @@
    @@@@@@@@@     @@@@@@@@    @@@@@@@    @@@@@@@@      @@@@@@@@
              @@@@@@  @@@  @@           @@  @@@  @@@@@@        
                  @@@@@@ @@ @@@@@@@@@@@ @@ @@@@@@              
                      @@ @@ @ @ @ @ @ @ @ @ @@                 
                    @@@@  @ @ @ @ @ @ @ @   @@@@@              
                @@@@@ @@   @@@@@@@@@@@@@   @@ @@@@@            
        @@@@@@@@@@     @@                 @@      @@@@@@@@@    
       @@           @@@@@@@             @@@@@@@@          @@   
        @@@     @@@@@     @@@@@@@@@@@@@@@     @@@@@     @@@    
          @@   @@@           @@@@@@@@@           @@@   @@      
          @@  @@                                   @@  @@      
           @@@@                                     @@@@""")
  elif acertou:
    trofeu()


def trofeu():
  print("""
         PARABÉNS!!! VOCÊ GANHOU!
          
        ##########################          
   #####################################    
 #########################################  
####      ######################       #### 
###     ##########################      ### 
###    ############################    #### 
 ###   ### #################### ###    ###  
 ####   ### ################## ####  ####   
   ####  ######################### #####    
    ######## ################ #########     
      ######  ##############   ######       
               ############                 
                 ########                   
                   ####                     
                   ####                     
                   ####                     
               ############                 
            ##################              
            ###            ###              
            ###            ###              
            ##################              
          ######################            """)
