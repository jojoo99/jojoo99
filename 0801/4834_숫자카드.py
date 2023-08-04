T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))
    new_arr = [0]*10
    for i in arr:
        new_arr[i] += 1
        print(new_arr)

    max_idx = 0
    max = 0
    for i in range(10):
        if new_arr[i] >= max:
            max = new_arr[i]
            max_idx = i

    print(f'#{tc} {max_idx} {max}')
