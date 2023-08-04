T = int(input())
for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    arr = list(map(int, input().split()))

max_val = 0
min_val = 1000000

for i in range(N - M + 1):
    sol_sum = 0
    for j in range(M):
        sol_sum += arr[i + j]

    if max_val < sol_sum:
        max_val = sol_sum
    if min_val > sol_sum:
        min_val = sol_sum

print(f'#{tc} {max_val - min_val}')