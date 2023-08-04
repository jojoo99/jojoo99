T = int(input())


def cnt_binary_search(start, end, key):
    cnt = 0
    while start <= end:
        cnt += 1
        mid = int((start + end) / 2)
        if mid == key:
            return cnt
        elif mid > key:
            end = mid
        else:
            start = mid



for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    cnt_A = cnt_binary_search(1, P, Pa)
    cnt_B = cnt_binary_search(1, P, Pb)

    if cnt_A < cnt_B:
        result = 'A'
    elif cnt_A > cnt_B:
        result = 'B'
    else:
        result = 0

    print(f'#{tc} {result}')