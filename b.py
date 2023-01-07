#Programa que calcula o IMC
nome = input("Digite o seu nome para avaliarmos o seu IMC: ")
h = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso: "))
imc = peso/(h * h)
print(nome,"o seu IMC é",round(imc,2),"\n""Você está classificado como:")
if imc < 18.5:
    print("obesidade nivel I, ou seja magreza")
if imc >= 18.5 or imc < 25:
    print("obesidade nivel II, ou seja seu peso está normal")
elif imc >= 25 or imc < 30:
    print("obesidade nivel III, ou seja você está com sobrepeso!")
elif imc >= 30 or imc <= 39.9:
    print("obesidade nível IV, ou seja obesidade")
elif imc >= 40:
    print("obesidade nível V, ou seja obesidade grave")