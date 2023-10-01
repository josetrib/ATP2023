import time,sys,random
#version 1.0.5

#Typewriter
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.0069)
#intro Computador adivinha
def introComputadorAdivinha():
    print_slow("\nVamos a isso!")
    print_slow("\nPensa num número entre 1 a 100.")
    print_slow("\nVou tentar adivinhar o teu número!")
    print_slow("\nDeseja-me sorte!\n\n")
    time.sleep(0.5)
#intro Computador adivinha 1-1000
def introComputadorAdivinhaMil():
    print_slow("\nVamos a isso!")
    print_slow("\nPensa num número entre 1 a 1000.")
    print_slow("\nVou tentar adivinhar o teu número!")
    print_slow("\nDeseja-me muita sorte!\n\n")
    time.sleep(0.5)
#intro Eu adivinho
def introJogadorAdivinha():
    print_slow("\nVamos a isso!")
    print_slow("\nTenta adivinhar o meu número entre 1 e 100")
    print_slow("\nBoa sorte!")
    time.sleep(0.5)

#intro Eu adivinho hardmode
def introJogadorAdivinhaHard():
    print_slow("\nVamos a isso!")
    print_slow("\nTenta adivinhar o meu número entre 1 e 100")
    print_slow("\nSó tens 3 vidas")
    print_slow("\nBoa sorte! Vais precisar ;)")
    time.sleep(0.5)

#Title screen
def titleScreen():
    print(" █████  ██████  ██ ██    ██ ██ ███    ██ ██   ██  █████       ██████      ███    ██ ██    ██ ███    ███ ███████ ██████   ██████  ")
    time.sleep(0.2)
    print("██   ██ ██   ██ ██ ██    ██ ██ ████   ██ ██   ██ ██   ██     ██    ██     ████   ██ ██    ██ ████  ████ ██      ██   ██ ██    ██ ")
    time.sleep(0.2)
    print("███████ ██   ██ ██ ██    ██ ██ ██ ██  ██ ███████ ███████     ██    ██     ██ ██  ██ ██    ██ ██ ████ ██ █████   ██████  ██    ██ ")
    time.sleep(0.2)
    print("██   ██ ██   ██ ██  ██  ██  ██ ██  ██ ██ ██   ██ ██   ██     ██    ██     ██  ██ ██ ██    ██ ██  ██  ██ ██      ██   ██ ██    ██ ")
    time.sleep(0.2)
    print("██   ██ ██████  ██   ████   ██ ██   ████ ██   ██ ██   ██      ██████      ██   ████  ██████  ██      ██ ███████ ██   ██  ██████ ")

    time.sleep(0.5)
titleScreen()


def main():
    menorMedia = 1
    maiorMedia = 100
    menorMediaMil = 1
    maiorMediaMil = 1000
    tentativasComputador = 1

    numeroComputador = random.randint(1,100)
    tentativas = int(0)
    vidas = int(3)
    escolhaMain = str(input("\nEscolha um dos modos de jogo \n 1) Computador adivinha \n 2) Computador adivinha 1-1000 \n 3) Eu adivinho \n 4) Eu adivinho (Difícil)\n 8) Conclusões \n 9) Como jogar\n 0) Créditos\n"))
    #Computador adivinha
    if escolhaMain == str(1):
        introComputadorAdivinha()
        time.sleep(0.5)
        def computadorAdivinha(menorMedia, maiorMedia, tentativasComputador):

            print("\nO teu número é", int((maiorMedia+menorMedia)/2),"?\n")
            maiorMenor = input("maior/menor/certo\n")

            if maiorMenor == "certo":
                print(" ██████   ██████   ██████  ██████       ██████   █████  ███    ███ ███████ ")
                time.sleep(0.2)
                print("██       ██    ██ ██    ██ ██   ██     ██       ██   ██ ████  ████ ██      ")
                time.sleep(0.2)
                print("██   ███ ██    ██ ██    ██ ██   ██     ██   ███ ███████ ██ ████ ██ █████   ")
                time.sleep(0.2)
                print("██    ██ ██    ██ ██    ██ ██   ██     ██    ██ ██   ██ ██  ██  ██ ██      ")
                time.sleep(0.2)
                print(" ██████   ██████   ██████  ██████       ██████  ██   ██ ██      ██ ███████ ")
                time.sleep(0.2)
                print("\n\nConsegui adivinhar o teu número em", tentativasComputador,"tentativas!\n\n")
                input("Prima Enter para voltar")
                main()
            elif int((maiorMedia+menorMedia)/2) == int(99):
            
                menorMedia = 100
                maiorMedia = 100
                tentativasComputador = tentativasComputador + 1
                computadorAdivinha(menorMedia, maiorMedia, tentativasComputador)

            elif maiorMenor == "maior":
            
                menorMedia = int((maiorMedia+menorMedia)/2)
                tentativasComputador = tentativasComputador + 1
                computadorAdivinha(menorMedia, maiorMedia, tentativasComputador)
            elif maiorMenor == "menor":

                maiorMedia = int((maiorMedia+menorMedia)/2)
                tentativasComputador = tentativasComputador + 1
                computadorAdivinha(menorMedia, maiorMedia, tentativasComputador)
            else:
                print("\nPor favor escolha uma das opções: maior/menor/certo")
                computadorAdivinha(menorMedia, maiorMedia, tentativasComputador)
        computadorAdivinha(menorMedia,maiorMedia, tentativasComputador)
    #Computador adivinha 1-1000
    if escolhaMain == str(2):
        introComputadorAdivinhaMil()
        def computadorAdivinhaMil(menorMediaMil, maiorMediaMil, tentativasComputador):
            print("O teu número é", int((maiorMediaMil+menorMediaMil)/2),"?")
            maiorMenorMil = input("maior/menor/certo\n")
            if maiorMenorMil == "certo":
                print(" ██████   ██████   ██████  ██████       ██████   █████  ███    ███ ███████ ")
                time.sleep(0.2)
                print("██       ██    ██ ██    ██ ██   ██     ██       ██   ██ ████  ████ ██      ")
                time.sleep(0.2)
                print("██   ███ ██    ██ ██    ██ ██   ██     ██   ███ ███████ ██ ████ ██ █████   ")
                time.sleep(0.2)
                print("██    ██ ██    ██ ██    ██ ██   ██     ██    ██ ██   ██ ██  ██  ██ ██      ")
                time.sleep(0.2)
                print(" ██████   ██████   ██████  ██████       ██████  ██   ██ ██      ██ ███████ ")
                time.sleep(0.2)
                print("\n\nConsegui adivinhar o teu número em", tentativasComputador,"tentativas!\n\n")
                input("Prima Enter para voltar")
                main()
            elif int((maiorMediaMil+menorMediaMil)/2) == int(999):
            
                menorMediaMil = 1000
                maiorMediaMil = 1000
                tentativasComputador = tentativasComputador + 1
                computadorAdivinhaMil(menorMediaMil, maiorMediaMil, tentativasComputador)
            elif maiorMenorMil == "maior":
            
                menorMediaMil = int((maiorMediaMil+menorMediaMil)/2)
                tentativasComputador = tentativasComputador + 1
                computadorAdivinhaMil(menorMediaMil, maiorMediaMil, tentativasComputador)
            elif maiorMenorMil == "menor":
                maiorMediaMil = int((maiorMediaMil+menorMediaMil)/2)
                tentativasComputador = tentativasComputador + 1
                computadorAdivinhaMil(menorMediaMil, maiorMediaMil, tentativasComputador)
            else:
                print("\nPor favor escolha uma das opções: maior/menor/certo")
                computadorAdivinhaMil(menorMediaMil, maiorMediaMil, tentativasComputador)
        computadorAdivinhaMil(menorMediaMil,maiorMediaMil, tentativasComputador)
    #Jogador adivinha
    if escolhaMain == str(3):
        introJogadorAdivinha()
        time.sleep(0.5)
        def jogadorAdivinha(tentativas):
            #print(numeroComputador)
            palpiteString = str(input("\nQual é o teu palpite? \n"))

            if palpiteString.isnumeric() == False:
                print("\nPor favor introduza um número inteiro de 1 a 100")
                jogadorAdivinha(tentativas)

            elif palpiteString.isnumeric() == True:
                palpite = int(palpiteString)
                if palpite > 100 or palpite < 1 :
                    print("\nPor favor introduza um número inteiro de 1 a 100")
                    jogadorAdivinha(tentativas)
                elif palpite == numeroComputador:
                    tentativas += 1
                        
                    print("██    ██  ██████  ██    ██     ██     ██ ██ ███    ██ ██ ")
                    time.sleep(0.2)
                    print(" ██  ██  ██    ██ ██    ██     ██     ██ ██ ████   ██ ██ ")
                    time.sleep(0.2)
                    print("  ████   ██    ██ ██    ██     ██  █  ██ ██ ██ ██  ██ ██ ")
                    time.sleep(0.2)
                    print("   ██    ██    ██ ██    ██     ██ ███ ██ ██ ██  ██ ██    ")
                    time.sleep(0.2)
                    print("   ██     ██████   ██████       ███ ███  ██ ██   ████ ██ \n\n")
                    print("Parabéns! Conseguiste adivinhar o meu número em", tentativas, "tentativa(s)")
                    time.sleep(1)
                    input("\n\nPrima Enter para Voltar")
                    main()
                    return tentativas
                elif palpite < numeroComputador:
                    tentativas += 1
                    print("\nMaior")
                    jogadorAdivinha(tentativas)
                    return tentativas
                elif palpite > numeroComputador:
                    tentativas += 1
                    print("\nMenor")
                    jogadorAdivinha(tentativas)
                    return tentativas
        jogadorAdivinha(tentativas)
    #Jogador adivinha com Três vidas
    if escolhaMain == str(4):
        #print(numeroComputador)
        introJogadorAdivinhaHard()
        time.sleep(0.5)
        def jogadorAdivinhaHardmode(vidas,numeroComputador):

            palpiteStringHard = str(input("\nQual é o teu palpite? \n"))
            if vidas > 0:
                if palpiteStringHard.isnumeric() == False:
                    print("\nPor favor introduza um número inteiro de 1 a 100")
                    jogadorAdivinhaHardmode(vidas,numeroComputador)

                if palpiteStringHard.isnumeric() == True:
                    palpite = int(palpiteStringHard)
                    if palpite > 100 or palpite < 1 :
                        print("\nPor favor introduza um número inteiro de 1 a 100")
                        jogadorAdivinhaHardmode(vidas,numeroComputador)
                    elif palpite == numeroComputador:
                        
                        print("██    ██  ██████  ██    ██     ██     ██ ██ ███    ██ ██ ")
                        time.sleep(0.2)
                        print(" ██  ██  ██    ██ ██    ██     ██     ██ ██ ████   ██ ██ ")
                        time.sleep(0.2)
                        print("  ████   ██    ██ ██    ██     ██  █  ██ ██ ██ ██  ██ ██ ")
                        time.sleep(0.2)
                        print("   ██    ██    ██ ██    ██     ██ ███ ██ ██ ██  ██ ██    ")
                        time.sleep(0.2)
                        print("   ██     ██████   ██████       ███ ███  ██ ██   ████ ██ \n\n")
                        
                        print("Muitos parabéns! Derrotaste o Modo Difícil com", vidas, "vida(s) restantes!")

                        hardChoices = input("\n\nJogar novamente? (Y/N)\n")
                        if hardChoices == "Y" or hardChoices == "y":
                            
                            numeroComputador = random.randint(1,100)
                            vidas = 3
                            introJogadorAdivinhaHard()
                            jogadorAdivinhaHardmode(vidas,numeroComputador)
                            return vidas
                        else:
                            vidas = 3
                            main()
                            
                    elif palpite < numeroComputador:
                        vidas -= 1
                        print("\nMaior")
                        jogadorAdivinhaHardmode(vidas,numeroComputador)
                        return vidas
                    elif palpite > numeroComputador:
                        vidas -= 1
                        print("\nMenor")
                        jogadorAdivinhaHardmode(vidas,numeroComputador)
                        return vidas
            #Lose condition
            if vidas == 0:
                print("\n\n██    ██  ██████  ██    ██     ██       ██████  ███████ ███████ ")
                time.sleep(0.2)
                print(" ██  ██  ██    ██ ██    ██     ██      ██    ██ ██      ██      ")
                time.sleep(0.2)
                print("  ████   ██    ██ ██    ██     ██      ██    ██ ███████ █████   ")
                time.sleep(0.2)
                print("   ██    ██    ██ ██    ██     ██      ██    ██      ██ ██      ")
                time.sleep(0.2)
                print("   ██     ██████   ██████      ███████  ██████  ███████ ███████ ")

                time.sleep(2)
                
                hardEscolha = str(input("\n\nTentar novamente? (Y/N)\n"))
                if hardEscolha == "Y" or hardEscolha =="y":
                    vidas = int(3)
                    numeroComputador = random.randint(1,100)
                    introJogadorAdivinhaHard()
                    jogadorAdivinhaHardmode(vidas,numeroComputador)
                else:
                    main()

        jogadorAdivinhaHardmode(vidas,numeroComputador)
    #Trollings
    if escolhaMain == str(5):
        def modoTroll():
            respostasRandom = ["Deixa-me cá ver...","...","Analisando a localização...","Carregando módulos de lógica...","Limpando o código de esparguete...","Analisando a temperatura...","Processando informação...","Calculando estimativas...","Buscando metadados...","Verificando ficheiros...","Fazendo café para os servidores...","Descobrindo o significado do número 42...","Trocando o valor de bits...","Refletindo profundamente...","Removendo bugs...","Ensinando morcegos a programar em Python...","Procurando erros no easter egg...","Localizando o servidor mais próximo...","Procurando mais easter eggs..."]
            numeroTroll = str(input("Introduza um número:"))
            contador = 0
            while contador < 20:
                print("\n")
                print_slow(random.choice(respostasRandom))
                contador = contador + 1
                time.sleep(0.69)
            else:
                #botar aqui o vegeta e o I win
                print("\n\nO número em que estás a pensar é", numeroTroll)
                time.sleep(3)
                print("\n\n██     ██     ██ ██ ███    ██ ")
                time.sleep(0.2)
                print("██     ██     ██ ██ ████   ██ ")
                time.sleep(0.2)
                print("██     ██  █  ██ ██ ██ ██  ██ ")
                time.sleep(0.2)
                print("██     ██ ███ ██ ██ ██  ██ ██ ")
                time.sleep(0.2)
                print("██      ███ ███  ██ ██   ████ ")
                time.sleep(1)
                input("Prima Enter para voltar")
                main()
        modoTroll()
    if escolhaMain == str(8):
        def conclusao():
            print_slow("\n\nConclusões:")
            print_slow("\nPara um número entre 1 e 100 o computador precisa, normalmente, no máximo, de 7 tentativas para descobrir o número que o jogador pensou.")
            print_slow("\n(Por vezes o computador precisa de 8 tentativas devido aos arredondamentos)")
            print_slow("\nPara um número entre 1 e 1000 o computador precisa, normalmente, no máximo, de 10 tentativas para descobrir o número que o jogador pensou.")
            print_slow("\n(Por vezes o computador precisa de 11 tentativas devido aos arredondamentos)")
            print_slow("\nEstes valores não aparecem por acaso. Isto é, 2^7=128 e 2^6=64, 2^6 < 100 < 2^7 o que significa que para um intervalo de 100 números inteiros serão necessários 7 ciclos para chegar aos números \"mais específicos\"")
            print_slow("\nTal também acontece com 2^10=1024, 2^9 < 1000 < 2^10 , são necessários 10 ciclos para chegar aos números \"mais específicos\"")
            print_slow("\nO algoritmo utilizado assemelha-se ao algoritmo Quicksort")

            input("\n\nPrima Enter para voltar")
            main()
        conclusao()
    #Tutorial
    if escolhaMain == str(9):
        def tutorial():
            print_slow("\nBem-vindo(a) ao Adivinha O Número!")
            print_slow("\n->No modo de jogo \"Computador adivinha\", o jogador pensa num número de 1 a 100 e o computador vai tentar adivinhá-lo")
            print_slow("\n  O computador diz um número e o jogador responde com:")
            print_slow("\n  -\"maior\" se o seu número for maior do que o do computador")
            print_slow("\n  -\"menor\" se o seu número for menor do que o do computador")
            print_slow("\n  -\"certo\" se o computador adivinhar o seu número")
            print_slow("\n->No modo de jogo \"Computador adivinha 1-1000\", o jogador pensa num número de 1 a 1000")

            print_slow("\n->No modo de jogo \"Eu adivinho\", o computador pensa num número e o jogador tenta adivinhá-lo")
            print_slow("\n  O jogador lança um número e o computador responde:")
            print_slow("\n  -\"maior\" se o seu número do computador for maior do que o palpite")
            print_slow("\n  -\"menor\" se o seu número do computador for menor do que o palpite")
            print_slow("\n  O jogo termina quando o jogador adivinha o número do computador!")
            
            
            print_slow("\n->No modo de jogo \"Eu adivinho (Difícil)\", o jogador tem apenas 3 vidas! Boa sorte!")

            input("\n\nPrima Enter para voltar")
            main()
        tutorial()
    #Créditos    
    if escolhaMain == str(0):
        def creditos():
            print("\n\n █████╗ ████████╗██████╗     ██████╗  ██████╗ ██████╗ ██████╗  ")
            time.sleep(0.2)
            print("██╔══██╗╚══██╔══╝██╔══██╗    ╚════██╗██╔═████╗╚════██╗╚════██╗ ")
            time.sleep(0.2)
            print("███████║   ██║   ██████╔╝     █████╔╝██║██╔██║ █████╔╝ █████╔╝ ")
            time.sleep(0.2)
            print("██╔══██║   ██║   ██╔═══╝     ██╔═══╝ ████╔╝██║██╔═══╝  ╚═══██╗ ") 
            time.sleep(0.2)
            print("██║  ██║   ██║   ██║         ███████╗╚██████╔╝███████╗██████╔╝ ") 
            time.sleep(0.2)
            print("╚═╝  ╚═╝   ╚═╝   ╚═╝         ╚══════╝ ╚═════╝ ╚══════╝╚═════╝  ")

            time.sleep(0.5)
            print_slow("\nDesenvolvido por: José Ribeiro A103741")
            print_slow("\nEditor de código: Microsoft Visual Studio Code")
            print_slow("\nDesenvolvido em Python 3.11.5")
            print_slow("\nArte desenvolvida utilizando https://patorjk.com/software/taag/")
            print_slow("\n\nAgradecimento especial a todos os playtesters! <3")
            print_slow("\nOs verdadeiros algoritmos foram os amigos que fizemos ao longo do caminho!")
            input("\n\nPrima Enter para voltar")
            print_slow("5")
            main()
        creditos()
main()
