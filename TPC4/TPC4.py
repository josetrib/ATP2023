import random

listaInterna = []
def main(listaInterna):


    
    escolhaMain = str(input("\n(1) Criar Lista \n(2) Ler Lista\n(3) Soma\n(4) Média\n(5) Maior\n(6) Menor\n(7) estaOrdenada por ordem crescente\n(8) estaOrdenada por ordem decrescente\n(9) Procura um elemento\n(0) Sair\n"))

    if escolhaMain == str(1):
        listaInterna=[]
        def criarLista():
            length = int(input("Introduza o tamanho da sua lista aleatória:\n"))
            k = 1
            while k <= length:
                listaInterna.append(random.randint(1,100))
                k = k + 1
            return listaInterna
        print("A sua lista foi guardada:",criarLista())
        input("\nPrima Enter para voltar.")
        main(listaInterna)

    if escolhaMain == str(2):
        listaInterna=[]
        def leLista():
            length=int(input("Introduza o tamanho da sua lista:"))
            k = 1
            while k <= length:
                
                elementoInput = int(input("Introduza um número inteiro:"))
                listaInterna.append(elementoInput)
                k=k+1
            return listaInterna
        print(leLista())
        input("\nPrima Enter para voltar.")
        main(listaInterna)

    if escolhaMain == str(3):
        def somaLista():
            soma = 0
            for k in listaInterna:
                soma = soma + k
            return soma
        print("A soma dos elementos da sua lista é:",somaLista())
        input("\nPrima Enter para voltar.")
        main(listaInterna)

    if escolhaMain == str(4):
        def mediaLista():
            somaMedia = 0
            for k in listaInterna:
                somaMedia = somaMedia + k
            return  somaMedia/len(listaInterna)
        print("A média dos elementos da sua lista é:",mediaLista())
        input("\nPrima Enter para voltar.")
        main(listaInterna)
        
    if escolhaMain == str(5):
        def maiorLista():
            maior = 0
            for i in listaInterna:
                if i > maior: maior = i
            return maior
        print("O maior elemento da sua lista é:",maiorLista())
        input("\nPrima Enter para voltar.")
        main(listaInterna)

    if escolhaMain == str(6):
        def menorLista():
            menor = 999999999999999999999999999999999
            for i in listaInterna:
                if i < menor: menor = i
            return menor
        print("O menor elemento da sua lista é:",menorLista())
        input("\nPrima Enter para voltar.")
        main(listaInterna)

    if escolhaMain == str(7):
        
        def estaOrdenadaC(listaInterna):
            listaTeste = []
            listaTeste = sorted(listaInterna)
            
            if listaTeste == listaInterna:
                print("Sim")
            else:
                print("Não")
                a = input("\nOrdenar lista por ordem crescente? (Y/N)\n")
                if a == "Y" or a == "y":
                    listaInterna = sorted(listaInterna)
                    print("Lista ordenada:", listaInterna)
                    input("\nPrima Enter para voltar.")
                    main(listaInterna)
                else:
                    input("\nPrima Enter para voltar.")
                    main(listaInterna)
        estaOrdenadaC(listaInterna)

    if escolhaMain == str(8):
        def estaOrdenadaD(listaInterna):
            listaTeste = []
            listaTeste = sorted(listaInterna, reverse=True)
            
            if listaTeste == listaInterna:
                print("Sim")
            else:
                print("Não")
                a = input("\nOrdenar lista por ordem decrescente? (Y/N)\n")
                if a == "Y" or a == "y":
                    listaInterna = sorted(listaInterna, reverse=True)
                    print("Lista ordenada:", listaInterna)
                    input("\nPrima Enter para voltar.")
                    main(listaInterna)
                else:
                    input("\nPrima Enter para voltar.")
                    main(listaInterna)
        estaOrdenadaD(listaInterna)
        
    if escolhaMain == str(9):
        def procurarElemento():
            wanted = int(input("\nIntroduza o elemento a procurar:"))
            
            
            if wanted in listaInterna:
                print("O elemento", wanted,"foi encontrado na posição", listaInterna.index(wanted))
            else: print(-1)
        procurarElemento()
        input("\nPrima Enter para voltar.")
        main(listaInterna)
    if escolhaMain == str(0):
        def sair():
            print("Lista final:", listaInterna)
            exit()
        sair()
main(listaInterna)