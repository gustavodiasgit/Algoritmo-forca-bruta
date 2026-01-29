numeros = []
qtd = int(input("Quantos valores você deseja inserir na sua lista? "))
for i in range(qtd):
    numero = input("Insira o valor {}: ".format(i + 1))
    numeros.append(numero)
alvo = input("Insira o valor que você deseja encontrar: ")
encontrado = False

print("Comparando valores...")
for numero in numeros:
    print("Comparando {} com {}".format(numero, alvo))
    if numero == alvo:
        encontrado = True
        break

if encontrado:
    print("Valor encontrado!")
else:
    print("Valor não encontrado.")
print("Busca concluída.")
