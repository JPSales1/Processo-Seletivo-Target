n = int(input("Digite um número inteiro: "))

a = 0
b = 1

while a < n:
    print(a, end=' ')
    a, b = b, a + b
    if a == n:
        print(a)

if a != n:
    print(f'\nO número {n} não pertence à sequencia')
else:
    print(f'\nO número {n} pertence à sequencia')

