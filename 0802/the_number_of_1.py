T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))
    arr.append(0)
    count = 0
    cnt_lst = []
    for i in range(N):
        if arr[i] == 1:
            count += 1
            if arr[i+1] == 0:
                cnt_lst.append(count)
                count = 0


    max_v = max(cnt_lst)
    print(f'#{tc} {max_v}')