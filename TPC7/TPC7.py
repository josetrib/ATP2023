import matplotlib as plt

listaPol = []
def criaPolIn():
    resPol = []
    grau = int(input("Insira o grau do polinómio:"))
    k = 0
    while k <= grau:
        coeficiente = float(input("Insira o valor do coeficiente para o monómio de grau %d:"%(grau-k,))) 
        if coeficiente != 0:
            expoente = grau-k
            resPol.append((coeficiente,expoente))
        k = k + 1
    listaPol.append(tuple(listaPol))
    return listaPol

def recuperarPolinomios():
    fnome = input("Insira o nome do ficheiro a carregar: ")
    fpol = open(fnome)
    listaPol = []
    for linha in fpol:
        pol = []
        termos = linha.split("|")
        termos.remove("\n")
        for x in termos:
            coef, exp = x.split(",")
            pol.append((float(coef),int(exp)))
        listaPol.append(pol)
    
    fpol.close()    
    return listaPol
def listarPolinomios():
    print("Número de ordem\tpolinómio")
    for ordem, polinomio in listaPol:
        print(f"{ordem}\t{polinomio}")


def grauPolinomio(p):
    grau = -999999999999999999999999999999999999
    for monomio in p:
        if monomio[1] > grau:
            grau = monomio[1]
    return grau
def calculoPolinomio():
    ordem = int(input("Digite o número de ordem do polinómio a ser calculado: "))
    x = float(input("Digite o valor de x: "))
    ordem, coeficientes = listaPol[ordem - 1]
    resultado = sum(c * (x ** i) for i, c in enumerate(coeficientes))
    print(f"Resultado: {resultado}")

def grauPolinomios(listap):
    maior = -9999999999999
    for p in listap:
        if grauPolinomio(p) > maior:
            maior = grauPolinomio(p)
    return maior

def guardarPolinomios(listap):
    fnome = input("Insira o nome do ficheiro a criar: ")
    fpol = open(fnome, "w")

    for pol in listap:
        for monomio in pol:
            coef, exp = monomio

            fpol.write(str(coef) + "," + str(exp) + "|")
        fpol.write("\n")
    
    fpol.close()
    return

def mostrarPolinomiosEGrau():
    print("Número de ordem\tpolinómio\tGrau")
    for ordem, coeficientes in listaPol:
        grau = len(coeficientes) - 1
        print(f"{ordem}\t{coeficientes}\t{grau}")

def somarPol():
    ordem1 = int(input("Digite o número de ordem do primeiro polinómio: "))
    ordem2 = int(input("Digite o número de ordem do segundo polinómio: "))
    _, coeficientes1 = listaPol[ordem1 - 1]
    _, coeficientes2 = listaPol[ordem2 - 1]
    coeficientes_soma = [c1 + c2 for c1, c2 in zip(coeficientes1, coeficientes2)]
    listaPol.append((ordem, coeficientes_soma))
    ordem += 1
    print(f"Resultado da soma (Número de Ordem {ordem}): {coeficientes_soma}")

def derivarPolinomio():
    polinomioDerivado = []
    polinomioIndex = int(input("Digite o número de ordem do polinómio: ")) - 1
    polinomio = listaPol[polinomioIndex]
    for monomio in polinomio:
        coeficiente, expoente = monomio
        novoCoeficiente = coeficiente * expoente
        novoExpoente = expoente - 1
        if novoExpoente >= 0:
            polinomioDerivado.append((novoCoeficiente, novoExpoente))
    return polinomioDerivado

def gerar_grafico():
    num_ordem = int(input("Digite o número de ordem do polinómio para gerar o gráfico: "))
    if 1 <= num_ordem <= len(listaPol):
        _, coeficientes = listaPol[num_ordem - 1]
        x = [i for i in range(-10, 11)]
        y = [sum(c * (xi ** i) for i, c in enumerate(coeficientes)) for xi in x]
        plt.plot(x, y)
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title(f"Gráfico do polinómio (Número de Ordem {num_ordem})")
        plt.grid()
        plt.show()
    else:
        print("Número de ordem inválido.")

def main():

    print("talcoiso e cenas")
    print("\nEscolha uma opção:")
    print("1) Criar polinómio")
    print("2) Ler polinómios de um arquivo")
    print("3) Mostrar polinómios em memória")
    print("4) Calcular valor de um polinómio")
    print("5) Mostrar polinomios com grau")
    print("6) Mostrar polinómio de maior grau")
    print("7) Mostrar polinómio de maior grau")
    print("8) Somar dois polinómios")
    print("9) Gerar gráfico de um polinómio")
    print("A) Gravar polinómios em um arquivo")
    print("0) Sair")

    escolhaMain = input("Opção: ")

    if escolhaMain == '1':
        criaPolIn()
        input("\n\nPrima Enter para Voltar")
        main()
    elif escolhaMain == '2':
        recuperarPolinomios()
        input("\n\nPrima Enter para Voltar")
        main()
    elif escolhaMain == '3':
        listarPolinomios()
        input("\n\nPrima Enter para Voltar")
        main()
    elif escolhaMain == '4':
        calculoPolinomio()
        input("\n\nPrima Enter para Voltar")
        main()
    elif escolhaMain == '5':
        mostrarPolinomiosEGrau()
        input("\n\nPrima Enter para Voltar")
        main()
    elif escolhaMain == '6':
        grauPolinomios()
        input("\n\nPrima Enter para Voltar")
        main()
    elif escolhaMain == '7':
        derivarPolinomio()
        input("\n\nPrima Enter para Voltar")
        main()
    elif escolhaMain == '8':
        somarPol()
        input("\n\nPrima Enter para Voltar")
        main()
    elif escolhaMain == '9':
        gerar_grafico()
        input("\n\nPrima Enter para Voltar")
        main()
    elif escolhaMain == 'A':
        guardarPolinomios()
        input("\n\nPrima Enter para Voltar")
        main()
    elif escolhaMain == '0':
        exit()
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
        input("\n\nPrima Enter para Voltar")
        main()

main()
