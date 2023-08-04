A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    ans_list = []
    for i in range(1 << 12):
        sub_subset_list = []
        total = 0
        for j in range(12):
            if i & (1 << j):
                sub_subset_list.append(A[j])
                total += A[j]
        num = len(sub_subset_list)
        ans_list.append([num, total])

    cnt = 0
    for i in range(1 << 12):
        if ans_list[i][0] == N and ans_list[i][1] == K:
            cnt += 1

    print(f'#{tc} {cnt}')




