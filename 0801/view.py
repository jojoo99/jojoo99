# 4개의 최댓값 구한구 가장 높으면 얼마나 높은가
T = 10
for tc in range(1, T + 1):
    N = int(input())
    heights = list(map(int, input().split()))
    new_list = []
    for i in range(2, N-1):
        if (heights[i] - heights[i-2]) > 0:
            left_2 = heights[i] - heights[i-2]
            if (heights[i] - heights[i - 1]) > 0:
                left_1 = heights[i] - heights[i - 1]
                if left_2 >=left_1:
                    left = left_1
                elif left_1 > left_2:
                    left = left_2
            else:
                new_list.append(0)
        else:
            new_list.append(0)


        if (heights[i] - heights[i+2]) > 0:
            right_2 = heights[i] - heights[i+2]
            if (heights[i] - heights[i + 1]) > 0:
                right_1 = heights[i] - heights[i + 1]
                if right_2 >= right_1:
                    right = right_1
                elif right_1 > right_2:
                    right = right_2
            else:
                new_list.append(0)
        else:
            new_list.append(0)

        if left >= right:
            new_list.append(right)
        else:
            new_list.append(left)

    sum = 0
    print(new_list)
    for i in new_list:
        sum = sum + i






