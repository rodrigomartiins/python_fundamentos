notas = []

quantidade = int(input('Quantas notas você quer inserir? '))

for i in range(quantidade):
    nota = float(input(f'Digite a nota {i + 1}: '))
    notas.append(nota)
    
soma = sum(notas)
media = soma / len(notas)

print(f'Notas digitadas: {notas}')
print(f'Média final: {media:.2f}')
