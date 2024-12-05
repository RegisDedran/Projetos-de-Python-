# Entrada
peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em metros): "))
idade = int(input("Digite sua idade: "))
genero = input("Digite seu gênero (masculino/feminino): ").strip().lower()
# Processamento
imc = peso / (altura ** 2)

# Seleção de perfil
print('Selecione o perfil de atividade física:')
print("1. Sedentário")
print("2. Ativo")
print("3. Moderadamente ativo")
print("4. Muito ativo")

# Correção aqui: usar um único '=' para atribuição
perfil_opcao = int(input('Digite o número do perfil: '))

# Estimativa de massa muscular com base na seleção de perfil
if perfil_opcao == 1:
    perfil = "Sedentário"
    fator_atividade = 1.2
    massa_muscular = 32
elif perfil_opcao == 2:
    perfil = "Ativo"
    fator_atividade = 1.375
    massa_muscular = 38
elif perfil_opcao == 3:
    perfil = "Moderadamente ativo"
    fator_atividade = 1.55
    massa_muscular = 42
elif perfil_opcao == 4:
    perfil = "Muito ativo"
    fator_atividade = 1.725
    massa_muscular = 48
else:
    perfil = "Desconhecido"
    massa_muscular = 0  # Para o caso de uma opção inválida

if genero == "masculino":
    tmb = 88.362 + (13.397 * peso) + (4.799 * (altura * 100)) - (5.677 * idade)
else:
    tmb = 447.593 + (9.247 * peso) + (3.098 * (altura * 100)) - (4.330 * idade)


ingestao_calorica = tmb * fator_atividade

# Cálculo do peso da massa muscular
peso_massa_muscular = (massa_muscular / 100) * peso

# Exibe resultado do IMC e estimativa de massa muscular
print(f"\nSeu IMC é: {imc:.2f}")
print(f"Perfil: {perfil}")
print(f"Percentual estimado de massa muscular: {massa_muscular}%")
print(f"Peso da massa muscular: {peso_massa_muscular:.2f} kg")
print(f"Ingestão calórica recomendada: {ingestao_calorica:.2f} calorias por dia")