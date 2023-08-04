# N*N 배열
# M*M 배열
# N*N 배열 순회

# 열, 행 0부터 N-M까지 순회
# 각 경우의 합 리스트에 저장
# 리스트 내의 최댓값 찾기

'''
    N*N 배열 만드는데 파리 개수 담은체로 선언
    시작 위치 처음 부터해서 i+M j+M 다 찾으면 돼 근데 배열 인덱스 넘는건 안돼
    안넘는 현재 위치면 자기 i+M j+M 안에 있는거 모두 찾기
    ex) i, j = 0, 0
    -> 0, 0 / 0, 1/ 1, 0/ 1, 1
'''

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        line = list(map(int, input().split()))
        arr.append(line)

    max_sum = 0

    for i in range(N):
        for j in range(N):
            if i+M <= N and j+M <= N:
                sum_v = 0
                for k in range(M):
                    for l in range(M):
                        sum_v = sum_v + arr[i+k][j+l]

            if sum_v > max_sum:
                max_sum = sum_v

    print(f'#{tc} {max_sum}')






