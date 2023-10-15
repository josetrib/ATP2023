# Features adicionais: Eliminar Salas; Remover Lugares de uma Sala; Importar a partir de .csv; Exportar para .csv

import os
salasCinema = []

def limparConsola():
    os.system('cls')

# Inserir uma sala
def inserirSala():
    nome = input("Insira o nome do filme:\n")
    cond = False
    for sala in salasCinema:
        if sala[2] == nome:
            cond = True
    if cond == True:
        print("Já existe uma sala a exibir esse filme.")
        escolha = input("Inserir outra sala? (Y/N)\n")
        if escolha == "Y" or escolha == "y":
            inserirSala()
        else: main()
    else:
        salaInserida = []
        vendidos = []
        nlugares = int(input("\nInsira o número de lugares da sala:"))
        salaInserida.append(nlugares)
        salaInserida.append(vendidos)
        salaInserida.append(nome)
        print("Adicionar", salaInserida, "ao cinema?(Y/N)\n")
        confirmar = input()
        if confirmar == "Y" or confirmar == "y":
            salasCinema.append(salaInserida)
        sair = input("Adicionar outra sala? (Y/N)\n")
        if sair == "Y" or sair == "y":
            inserirSala()
        else:
            main()
    return salasCinema

# Listar os filmes 
def listarFilmes():
    print("Filmes em exibição:")
    for sala in salasCinema:
        print(sala[2])
    input("\n\nPrima Enter para voltar")
    main()

# Listar os filmes em exibição c/ número de lugares no total e lugares ocupados
def listarDisponivel():
    print("Filmes em exibição:")
    for sala in salasCinema:
        print(sala[2], "- total de", sala[0],"lugares | lugares", sala[0]-len(sala[1]),"disponíveis")
    input("\n\nPrima Enter para voltar")
    main()

# Vender bilhetes
def venderBilhete():
    nome = input("Insira o nome do filme:\n")
    controlo = False
    for sala in salasCinema:
        if sala[2] == nome:
            print("Lugares ocupados:", sala[1])
            controlo = True
            k = 1
            nvendas = int(input("Número de lugares a vender:"))
            while k <= nvendas:
                lugar = int(input("Lugar vendido:"))
                if  lugar > 0 and lugar <= sala[0]:
                    if lugar not in sala[1]:
                        sala[1].append(lugar)
                        k = k + 1
                    else:
                        print("Esse lugar já se encontra vendido.")
                else:
                    print("Lugar fora de alcance. Por favor introduza um valor entre 1 e", sala[0])
            voltar = input("Vender mais bilhetes? (Y/N)")
            if voltar == "Y" or voltar == "y":
                venderBilhete()
            else: main()
    if controlo == False:
        print("Não foi encontrada nenhuma sala com esse filme em exibição.")
        voltar = input("\nVerificar outra sala? (Y/N)")
        if voltar == "Y" or voltar == "y":
            venderBilhete()
        else: main()
    return salasCinema

# Limpar lugares - útil para várias exibições de um dado filme na mesma sala ou para reembolsos
def limparLugares():
    nome = input("Insira o nome do filme:\n")
    print("1) Eliminar todos os lugares")
    print("2) Eliminar lugares individuais")
    print("0) Cancelar\n")
    escolha = input()
    controlo = False
    for sala in salasCinema:
        if sala[2] == nome:
            controlo = True
            if escolha == "1":
                sala[1] = []
                print("Lugares eliminados com sucesso")
                input("\nPrima Enter para voltar")
                main()      
            if escolha == "2":
                print("Lugares ocupados:", sala[1])
                nEliminar = int(input("Número de lugares a eliminar:"))
                k = 1
                if nEliminar > len(sala[1]):
                    print("Número de lugares a eliminar excede o número de lugares ocupados.")
                    input("\nPrima Enter para voltar")
                    main()
                while k <= nEliminar:
                    lugar = int(input("Lugar a remover:"))
                    if  lugar > 0 and lugar <= sala[0]:
                        if lugar in sala[1]:
                            sala[1].remove(lugar)
                            k = k + 1
                        else:
                            print("Lugar não encontrado.")
                input("\nPrima Enter para voltar")
                main()       
            else:
                print("Operação cancelada")
                input("\nPrima Enter para voltar")
                main()       
    if controlo == False:
        print("Não foi encontrada nenhuma sala com esse filme em exibição.")
        voltar = input("\nVerificar outra sala? (Y/N)")
        if voltar == "Y" or voltar == "y":
            limparLugares()
        else: main()
    return salasCinema

# Eliminar sala
def eliminarSala():
    nome = input("Insira o nome do filme a remover:\n")
    for sala in salasCinema:
        if sala[2] == nome:
            print("Eliminar", sala, "? (Y/N)")
            escolha = input()
            if escolha == "Y" or escolha == "y":
                print(sala," foi removido.")
                salasCinema.remove(sala)
                input("\nPrima Enter para voltar")
                main()
            else:
                print("Operação cancelada")
                input("\nPrima Enter para voltar")
                main()
    return salasCinema

# Verificar se lugar disponivel
def disponivel(): 
    nome = input("Insira o nome do filme:\n")
    lugar = int(input("\nInsira o lugar a verificar:"))
    cond = True
    controlo = False
    for sala in salasCinema:
        if sala[2] == nome:
            controlo = True
            if lugar in sala[1]:
                cond = False   
    if controlo == False:
        print("Não foi encontrada nenhuma sala com esse filme em exibição.")
        voltar = input("\nTentar novamente? (Y/N)")
        if voltar == "Y" or voltar == "y":
            disponivel()
        else: main()
    return cond
    
# Terminar aplicação
def sair():
    print("Cinema final:", salasCinema)
    #fazer funcao para guardar cinema num ficheiro?
    exit()

# Exporta a lista salasCinema para um ficheiro .csv
def exportar():
    confirm = input("Exportar o cinema atual para cinemaOut.csv? \nEsta ação eliminará os conteúdos preexistentes de cinemaOut.csv, caso este exista. \n(Y/N)\n")
    if confirm == "Y" or confirm == "y":
        f = open("cinemaOut.csv", "w")
        f.write("lugaresTotal;lugaresVendidos;filme\n")
        for sala in salasCinema:
            for campo in sala:
                f.write(str(campo))
                f.write(";")
            f.write("\n")
        print("Exportação concluída com sucesso para cinemaOut.csv.")
        input("\nPrima Enter para voltar")
        main()
        f.close()
    else:
        print("Operação cancelada")
        input("\nPrima Enter para voltar")
        main()

#importar a partir de ficheiro csv
def importar():
    global salasCinema
    nome = input("Introduza o nome do ficheiro a importar:\n")
    print("Importar", nome, "para o cinema atual? (Y/N)\n")
    confirm = input()
    if confirm == "Y" or confirm == "y":
        f = open(nome,"r")
        f.readline()
        salasCinema = []
        for linha in f:
            campos = linha.split(";")
            salasCinema.append((int(campos[0]), campos[1], str(campos[2])))
        print(nome,"foi importado com sucesso.")
        f.close()
    else:
        print("Operação cancelada")
    return salasCinema


def main():
    limparConsola()
    print("1) Listar filmes em exibição")
    print("2) Listar número de lugares disponíveis")
    print("3) Verificar disponibilidade de lugares")
    print("4) Vender bilhetes")
    print("5) Inserir sala de cinema")
    print("6) Eliminar sala de cinema")
    print("7) Eliminar lugares de uma sala")
    print("8) Importar cinema a partir de ficheiro .csv")
    print("9) Exportar cinema para um ficheiro .csv")
    print("0) Sair")
    escolhaMain = input()
    if escolhaMain == "1":
        limparConsola()
        listarFilmes()
    if escolhaMain == "2":
        limparConsola()
        listarDisponivel()
    if escolhaMain == "3":
        limparConsola()
        print(disponivel())
        input("\nPrima Enter para voltar")
        main()
    if escolhaMain == "4":
        limparConsola()
        venderBilhete()
    if escolhaMain == "5":
        limparConsola()
        inserirSala()
    if escolhaMain == "6":
        limparConsola()
        eliminarSala()    
    if escolhaMain == "7":
        limparConsola()
        limparLugares()    
    if escolhaMain == "8":
        limparConsola()
        importar()
        input("\nPrima Enter para voltar")
        main()
    if escolhaMain == "9":
        limparConsola()
        exportar() 
    if escolhaMain == "0":
        limparConsola()
        sair()
main()