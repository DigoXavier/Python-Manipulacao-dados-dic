from Dicionarios.Funcoes import perguntar, inserir

usuarios = {}
opcao = perguntar
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        inserir(usuarios)
    opcao=perguntar