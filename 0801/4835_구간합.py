T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    min = 100*10000
    max = 0
    for i in range(N-M+1):
        sum = 0
        for j in range(M):
            sum = sum + arr[i+j]
        if sum < min:
            min = sum
        if sum > max:
            max = sum

    difference = max - min

    print(f'#{tc} {difference}')

