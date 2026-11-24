#import 

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

print(f"\nNome:", {nome}, "\nIdade:", {idade}, "\nCurso:", {curso}, "\nCidade", {cidade}, "\n")
#.commit()