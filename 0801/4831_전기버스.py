T = int(input())

for tc in range(1, T+1):
    k, N, M = map(int, input().split())
    busstop = [0] + list(map(int, input().split())) + [N]
    count = 0
    for i in range(M-1):
        if busstop[i+2] - busstop[i] >= k:
            count += 1

