todos = [[], []]
for c in range(0, 7):
    n = int(input('digite um numero'))
    if n % 2 == 0:
        todos[1].append(n)
    else:
        todos[0].append(n)
print(f'os numeros impares são : {todos[0]}')
print(f'os numerospares são : {todos[1]}')
