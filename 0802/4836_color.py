T = int(input())

for tc in range(1, T+1):
    N = int(input())
    color_1 = []
    color_2 = []
    for _ in range(N):
        arr = list(map(int, input().split()))
        for i in range(arr[1], arr[3]+1):
            for j in range(arr[0], arr[2]+1):
                coord = str(i) + str(j)
                if arr[4] == 1:
                    color_1.append(coord)
                elif arr[4] == 2:
                    color_2.append(coord)

    color_1 = list(set(color_1))
    color_2 = list(set(color_2))
    count = 0
    for i in color_1:
        for j in color_2:
            if i == j:
                count += 1

    print(f'#{tc} {count}')



