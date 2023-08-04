T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    for i in range(2*N+1):
        for j in range(2*N+1):
            if ((N-i)**2 + (N-j)**2)**(1/2) <= N:
                cnt += 1

    print(f'#{tc} {cnt}')