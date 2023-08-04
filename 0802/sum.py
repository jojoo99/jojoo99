for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    sum_list = []

    for i in range(100):
        sum_v = 0
        for j in range(100):
            sum_v = sum_v + arr[i][j]
        sum_list.append(sum_v)

    for i in range(100):
        sum_v = 0
        for j in range(100):
            sum_v = sum_v + arr[j][i]
        sum_list.append(sum_v)

    for i in range(100):
        sum_v = 0
        for j in range(100):
            if i == j:
                sum_v = sum_v + arr[i][j]
    sum_list.append(sum_v)

    sum_v = 0
    for i in range(100):
        sum_v = sum_v + arr[i][99-i]
    sum_list.append(sum_v)

    print(sum_list)

    max_v = max(sum_list)

    print(f'#{N} {max_v}')

