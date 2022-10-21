import random

def atualiza_vizinhanca(campo, l, c, dim):
    if c + 1 < dim and campo[l][c + 1] != 9:
        campo[l][c+1] = campo[l][c+1] + 1

    if c + 1 < dim and l + 1 < dim and campo[l+1][c+1] != 9:
        campo[l+1][c+1] = campo[l+1][c+1] + 1

    if l + 1 < dim and campo[l+1][c] != 9:
        campo[l+1][c] = campo[l+1][c] + 1

    if c - 1 >= 0 and l + 1 < dim and campo[l+1][c-1] != 9:
        campo[l+1][c-1] = campo[l+1][c-1] + 1

    if c - 1 >= 0 and campo[l][c-1] != 9:
        campo[l][c-1] = campo[l][c-1] + 1

    if c - 1 >= 0 and l - 1 >= 0 and campo[l-1][c-1] != 9:
        campo[l-1][c-1] = campo[l-1][c-1] + 1

    if l - 1 >= 0 and campo[l-1][c] != 9:
        campo[l-1][c] = campo[l-1][c] + 1

    if c + 1 < dim and l - 1 >= 0 and campo[l-1][c+1] != 9:
        campo[l-1][c+1] = campo[l-1][c+1] + 1


campo = []
dim = 10
BOMBA = 9

for i in range(dim):
    campo.append([0] * dim)

contador = 0    
while contador < dim:
    i = random.randint(0, dim - 1)
    j = random.randint(0, dim - 1)

    if i != 0 and j != 0 and campo[i][j] == 0:
        campo[i][j] = 9
        contador = contador + 1


for i in range(dim):
    for j in range(dim):
        if campo[i][j] == BOMBA:
            atualiza_vizinhanca(campo, i, j, dim)


for lin in campo:
    print(lin)