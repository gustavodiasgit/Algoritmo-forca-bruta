numeros = []
qtd = int(input("Quantos números você deseja inserir na sua lista? "))
for i in range(qtd):
    numero = int(input("Insira o número {}: ".format(i + 1)))
    numeros.append(numero)
alvo = int(input("Insira o número que você deseja encontrar: "))
encontrado = False

print("Comparando valores...")
for numero in numeros:
    print("Comparando {} com {}".format(numero, alvo))
    if numero == alvo:
        encontrado = True
        break

if encontrado:
    print("Número encontrado!")
else:
    print("Número não encontrado.")
print("Busca concluída.")
