l1 = []
l2 = []
print("Lista 1:\n")
for al1 in range(10):
    al1 = int(input())
    l1.append(al1)
print("Lista 2:\n")
for al2 in range(10):
    al2 = int(input())
    l2.append(al2)
l3soma = l1 + l2            #adiciona a segunda lista a primeira
print(f'Soma das duas listas anteriores = {l3soma}')