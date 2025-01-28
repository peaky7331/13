#22.	Формируется матрица F следующим образом: Скопировать в нее матрицу А и если сумма чисел, больших К в нечетных столбцах в области 3 больше, чем произведение чисел по периметру в области 2, 
#то поменять симметрично области 1 и 2 местами, иначе 3 и 4 поменять местами несимметрично. При этом матрица А не меняется. После чего вычисляется выражение: 
#((К*A)*F+ K* F T . Выводятся по мере формирования А, F и все матричные операции последовательно.

import random

K = int(input("Введите значение K: "))
N = int(input("Введите значение N: "))

print("Выберите способ заполнения матрицы:")
print("1. Случайные значения")
print("2. Заполнение из файла")
choice = int(input("Введите 1 или 2: "))

if choice == 2:
    with open("1.txt", 'r') as f:
        A = [list(map(int, line.split())) for line in f]
else:
    A = [[random.randint(-10, 10) for _ in range(N)] for _ in range(N)]

print("\nМатрица A:")
for row in A:
    print("\t".join(map(str, row)))
print()

# вычисление суммы чисел больших K в нечетных столбцах в области 3
s = 0
for i in range(N//2, N):
    for j in range(0, N//2, 2):  # нечетные столбцы
        if A[i][j] > K:
            s += A[i][j]

# вычисление произведения чисел по периметру в области 2
p = 1
for i in range(N//2):
    p *= A[i][N//2]
    p *= A[i][N-1]
for j in range(N//2, N):
    p *= A[0][j]
    p *= A[N//2-1][j]

F = [row[:] for row in A]

# проверка условий и обмен областей
if s > p:
    for i in range(N//2):
        for j in range(N//2):
            F[i][j], F[i][j+N//2] = F[i][j+N//2], F[i][j]
else:
    for i in range(N//2, N):
        for j in range(N//2):
            F[i][j], F[i][j+N//2] = F[i][j+N//2], F[i][j]

# вычисление выражения ((K * A) * F + K * F) * F^T
K_A = [[K * A[i][j] for j in range(N)] for i in range(N)]
K_F = [[K * F[i][j] for j in range(N)] for i in range(N)]
K_A_F = [[sum(K_A[i][k] * F[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
K_A_F_plus_K_F = [[K_A_F[i][j] + K_F[i][j] for j in range(N)] for i in range(N)]
F_T = [[F[j][i] for j in range(N)] for i in range(N)]
result = [[sum(K_A_F_plus_K_F[i][k] * F_T[k][j] for k in range(N)) for j in range(N)] for i in range(N)]


print("\nМатрица F:")
for row in F:
    print("\t".join(map(str, row)))
print()


print("\nРезультат ((K * A) * F + K * F) * F^T:")
for row in result:
    print("\t".join(map(str, row)))
print()
