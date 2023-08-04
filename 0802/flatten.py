for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(N):
        max_v = 0
        min_v = 101
        for j in range(100):
            if arr[j] <= min_v:
                min_v = arr[j]
                min_idx = j
            if arr[j] >= max_v:
                max_v = arr[j]
                max_idx = j

        arr[min_idx] = arr[min_idx] + 1
        arr[max_idx] = arr[max_idx] - 1

        min_v = 101
        max_v = 0
        for j in arr:
            if j < min_v:
                min_v = j
            if j > max_v:
                max_v = j

        dif = max_v - min_v
        # dif = max(arr) - min(arr)
        if dif <= 1:
            break



    print(f'#{tc} {dif}')





