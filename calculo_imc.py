def calcular_imc(peso, altura):
    # Cálculo do IMC
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    # Classificação do IMC
    if imc < 18.5:
        return "Abaixo do Peso"
    elif 18.5 <= imc < 24.9:
        return "Peso Normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

# Solicitando entrada do usuário
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Calculando o IMC
imc = calcular_imc(peso, altura)

# Classificando o IMC
categoria = classificar_imc(imc)

# Exibindo o resultado
print(f"Seu IMC é {imc:.2f}. Você está na categoria: {categoria}.")