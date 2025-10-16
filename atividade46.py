# Sistema de Avaliação Contínua
# Permita que o usuário digite notas enquanto desejar (perguntando se quer continuar).
# Ao final, exiba a média geral e quantas notas foram informadas.

soma = 0
quantidade = 0

while True:
    nota = float(input("Nota: "))
    soma += nota
    quantidade += 1
    if input("Continuar? (s/n) ") != "s":
        break

print("Média:", soma / quantidade)
print("Total de notas:", quantidade)
