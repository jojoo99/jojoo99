T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr_integer = [2, 3, 5, 7, 11]
    cnt_list = [0, 0, 0, 0, 0]
    for i in arr_integer:
        while N % i == 0:
            N = N/i
            idx = arr_integer.index(i)
            cnt_list[idx] += 1

    print(f'#{tc}', *cnt_list)


