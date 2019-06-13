opcao = 0
vetor = []
nome = []

while(opcao != 4):
    print('=' * 30)
    opcao = int(input('DIGITE A OPÇÃO DESEJADA:\n1 - ADICIONAR LIVROS\n2 - REMOVER LIVROS\n3 - EXIBIR ITEM\n4 - SAIR\n'))
    if opcao == 1 :
        codigo = int(input('ADICIONAR UM LIVRO-\nADICIONAR CODIGO DO LIVRO: '))
        vetor.append(codigo)
        titulo = str(input('ADICIONAR NOME DO LIVRO: '))
        nome.append(titulo)
    elif opcao == 2:
        print('LIVROS A DISPOSIÇÃO')
        tam = len(vetor)
        for i in range(tam):
            print(vetor[i],'-',nome[i])
        j = -1
        valor = int(input("DIGITE O LIVRO QUE SERA RETIRADO: "))
        for i in range(tam):
            if vetor[i]==valor:
                j=i
        if j!=-1:
            del(vetor[j])
            del(nome[j])
        else:
            print('CODIGO INEXISTENTE')
    elif opcao == 3:
        print(f"QUANTIDADE DE LIVROS EM ESTOQUE: {len(vetor)}")
        for i in range(len(vetor)):
            print('='*30)
            print(vetor[i],'-',nome[i])
            print('=' * 30)
    elif opcao == 4:
        print('SAIR\nOBRIGADO POR TUDO')

    #elif opcao == 5:
        #print('LIVROS A DISPOSIÇÃO')
        #tam = len(vetor)
        #for i in range(tam):
            #print(vetor[i],'-',nome[i])
        #j = -1
        #valor = int(input("DIGITE O LIVRO QUE SERA TROCADO: "))
        #novo = int(input('NOVO CODIGO: '))
        #name = str(input('NOVO LIVRO: '))
        #for i in range(tam):
            #if vetor[i]==valor:
                #vetor[i] = novo
                #nome[i] = name
        #else:
            #print('CODIGO INEXISTENTE')