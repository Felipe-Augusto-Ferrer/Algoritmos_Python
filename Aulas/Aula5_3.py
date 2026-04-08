numero = int(input("Valor entre 1 e 10: "))
while numero <= 0 or numero > 10:
    print("O valor deve estar entre 1 e 10")
    numero = int(input("Valor válido: "))

multiplicador=1
while multiplicador <= 10:
    print(f"{numero}x{multiplicador}={numero*multiplicador}")
    multiplicador += 1
