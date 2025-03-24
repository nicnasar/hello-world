val_dia = 114.90
km_rodado = 0.1

km = float(input("Você percorreu quantos kilômetros?"))

dias = int(input("Foram quantos dias alugados?"))

valor = val_dia * dias + km_rodado * km

print(f"O preço a ser pago será R${valor:.2f}.")