#* Desenvolve as seguintes funcionalidades que não foram trabalhadas na aula:
#    1. Define uma função que dado um polinómio calcula a sua derivada;
#    2. Define uma função que recebe dois polinómios `p1` e `p2` e calcula um novo polinómio correspondente à soma de `p1` e `p2`;
#    3. Define uma função que recebe um polinómio e o desenha num gráfico.
#
#* Num ficheiro Python, cria uma aplicação para manipular polinómios com as seguintes operações:
#done    1. Criar um polinómio interativamente;
#done    2. Ler uma lista de polinómios de um ficheiro;
#    3. Listar polinómios: mostra numa tabela os polinómios carregados em memória, adicionando um número de ordem a cada um;
#    4. Calcular o valor de um polinómio num ponto (usa o número de ordem para referenciar o polinómio);
#    5. Listar polinómios com grau: à listagem anterior, acrescenta mais uma coluna com o grau;
#done    6. Maior grau: mostra o polinómio de maior grau e indica o seu número de ordem;
#    7. Derivada: mostra uma tabela com os polinómios e as respetivas derivadas;
#    8. Somar dois polinómios: indicando os seus números de ordem;
#    9. Gerar um gráfico para o polinómio;
#done    10. Gravar num ficheiro os polinómios em memória;
#done    0. Sair da aplicação


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

def grauPolinomio(p):
    grau = -999999999999999999999999999999999999
    for monomio in p:
        if monomio[1] > grau:
            grau = monomio[1]
    return grau

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


def main():
    print("talcoiso e cenas")
    escolhaMain = int(input())

    if escolhaMain == 1:
        criaPolIn()

    if escolhaMain == 2:
        recuperarPolinomios()

    if escolhaMain == 10:
        guardarPolinomios(listaPol)

    if escolhaMain == 0:
        exit()

main()