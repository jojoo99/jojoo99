T = int(input())

for tc in range(1, T+1):
    D, A, B, F = map(float, input().split())

    ans = D*F/(A+B)
    # ans = 0     # 파리가 이동한 거리
    # cnt = 1     # 파리 편도 이동 횟수
    # while D > 0:
    #     if cnt % 2 != 0:    # 파리가 기차 B로 이동할 때
    #         time = D/(F+B)  # 파리가 기차에 닿을 때까지 걸린 시간
    #         ans = ans + (F*time)
    #         D = D - (A+B)*time
    #         cnt += 1
    #     elif cnt % 2 == 0:  # 파리가 기차 A로 이동할 때
    #         time = D/(F+A)
    #         ans = ans + (F*time)
    #         D = D - (A+B)*time
    #         cnt += 1

    print(f'#{tc} {ans}')