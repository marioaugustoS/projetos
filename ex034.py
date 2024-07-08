salario = float(input("digite aqui o seu salario "))

if salario >1250.0:
    salarioAumentado = salario*1.1
    print(f"o salario com aumento é {salarioAumentado:.2f}")
if salario <= 1250.0:
    salarioAumentado = salario*1.15
    print(f"o salario com aumento é {salarioAumentado:.2f}")