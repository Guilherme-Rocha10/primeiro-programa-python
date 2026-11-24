# Simbulos matematicos de python
print("\nDigite os valores")
a = float(input("- "))
b = float(input("- "))

soma = a + b        
subtracao = a - b   
produto = a * b    
divisao = a / b     
inteiro = a // b    
resto = a % b        
potencia = a ** b 

print("\nSoma:", soma)
print("subtração:", subtracao)
print("produto:", produto)
print("divisão:", divisao)
print("inteiro:", inteiro)
print("resto:", resto)
print("potencia:", potencia, "\n")


# idade curso e cidade
print("-------------------------")
nome = input("\nDigite seu nome: ")
idade = float(input("Digite sua idade: "))
curso = input("Digite o nome do seu curso: ")
cidade = input("Digite o nome da sua cidade: ")

print(f"\nNome:", nome, "\nIdade:", idade, "\nCurso:", curso, "\nCidade", cidade, "\n")
print("-------------------------\n")


# Menu interativo
cont = ""
num1 = float(input("Digite o novo primeiro valor: "))
num2 = float(input("Digite o novo segundo valor: "))
X = num1 + num2

while cont != "sair":
    print("\n[0] Digitar os números de interesse")
    print("[1] Mostrar a soma dos 2 números digitados")
    print("[2] Mostrar se a soma dos 2 números é par ou impar")
    print("[3] Sair")
    cont = input("Digite sua opção: ")

    if cont == "0":
        num1 = float(input("Digite o novo primeiro valor: "))
        num2 = float(input("Digite o novo segundo valor: "))
        X = num1 + num2
    elif cont == "1":
        print(f"\n {X}")
        print("--------------\n")
    elif cont == "2":
        if X % 2 == 0:
            print("\nA soma dos números é par")
            print("--------------\n")
        else:
            print("\nA soma dos números é impar")
            print("--------------\n")
    elif cont == "3":
        cont = "sair"
        print("\nPrograma finalizado")
    else:
        print("\nOpção invalida!\n")
        