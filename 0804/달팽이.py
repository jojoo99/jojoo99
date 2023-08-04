# 1> N*N 배열이 필요하다. value를 다 0으로 초기화. 끝
# 2> list[0][0]에서 출발한다.
# 3> 시작은 오른쪽으로 가면서 시작 if 박스를 벗어날거같으면 방향 변경,
# 이미 숫자가 존재하면 단 숫자가 0이면 아님
# 4> 방향 순서는 우 하 좌 상
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    snail_list = [[0]*N]*N # 1>

    dr = [0, 1, 0, -1] # 4>
    dc = [1, 0,-1, 0]
    dist = 0

    row = 0 # 2>
    col = 0
    for i in range(1, N*N+1):
        snail_list[row][col] = i
        row += dr[dist]
        col += dc[dist]
        # 3>
        if row < 0 or row >= N or col < 0 or col >= N or snail_list[row][col] != 0:
            row -= dr[dist]
            col -= dc[dist]

            dist = (dist + 1) % 4

            row += dr[dist]
            col += dc[dist]