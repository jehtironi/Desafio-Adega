from re import T
import os

os.system('cls')
    
escolha = 'N'
quantidadeT = 0
quantidade = 0
contT = 0 #Contador para vinho tinto
contB = 0 #Contador para vinho branco
contR = 0 #Contador para vinho Rose

while(escolha !=  'F'):
    #Solicita o tipo de vinho ao usuario
    vinho = input("Qual o tipo de vinho que você deseja adicionar? (T = tinto, B = Branco, R = Rose)  = ")
    vinho = vinho.upper() #Deixa a opção sempre em letra maiuscula
    
    #Verifica se é uma opção valida
    while(vinho != 'T' and vinho != 'B' and vinho != 'R'):
        vinho = input("Opção invalida, digite outra (T = tinto, B = Branco, R = Rose)  = ")
        vinho = vinho.upper() #Deixa a opção sempre em letra maiuscula
    
    #Solicita a quantidade de vinhos
    quantidade = int(input("Digite a quantidade de vinhos: "))
    
    #Incrementa a quantidade de vinhos digitados pelo usuario levando em consideração o tipo de vinho
    if(vinho == 'T'):
        contT = contT + quantidade
    elif(vinho == 'B'):
        contB = contB + quantidade
    else:
        contR = contR + quantidade
    
    #Verifica a quantidade de vinho no estoque
    quantidadeT = contT + contB + contR

    #Calcula a porcentagem total de vinhos    
    porcentagemT = (contT/quantidadeT)*100
    porcentagemB = (contB/quantidadeT)*100
    porcentagemR = (contR/quantidadeT)*100
    
    print("-------------------------------------------------------\n")
    
    #Retorna as informações ao usuario  
    print("\n\nQuantidade de vinhos no estoque")
    print("Existem ", contT, " vinhos tintos em estoque, correspondendo assim a ", round(porcentagemT, 2), "%"," do estoque total")
    print("Existem ", contB, " vinhos brancos em estoque, correspondendo assim a ",  round(porcentagemB, 2), "%"," do estoque total")
    print("Existem ", contR, " vinhos tintos em estoque, correspondendo assim a ",  round(porcentagemR, 2), "%"," do estoque total")

    #Solicita ao usuario se ele deseja continuar adicionando vinhos    
    escolha = input("Deseja finalizar a operação?: (F = Sim N = Não): ")
    escolha = escolha.upper() #Deixa a opção sempre em letra maiuscula
    print("-------------------------------------------------------\n")
    
    #Verifica se é uma opção valida
    while(escolha != 'F' and escolha != 'N'):
        escolha = input("Opção invalida, digite outra (F = Sim N = Não) = ")
        escolha = escolha.upper() #Deixa a opção sempre em letra maiuscula
        
    os.system('cls')


 
#Retorna as informações ao usuario  
print("Quantidade de vinhos no estoque")
print("Existem ", contT, " vinhos tintos em estoque, correspondendo assim a ", round(porcentagemT, 2), "%"," do estoque total")
print("Existem ", contB, " vinhos brancos em estoque, correspondendo assim a ",  round(porcentagemB, 2), "%"," do estoque total")
print("Existem ", contR, " vinhos tintos em estoque, correspondendo assim a ",  round(porcentagemR, 2), "%"," do estoque total")
    
    