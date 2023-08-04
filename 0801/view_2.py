for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    building_with_view = 0
    for i in range(2, N-2):
        if arr[i] > arr[i-1] and arr[i] > arr[i-2] and arr[i] > arr[i+1] and arr[i] > arr[i+2]:
            max_height = arr[i-2]
            for j in range(i-2,i+3):
                if j == i:
                    continue

                if arr[j] > max_height:
                    max_height = arr[j]
            building_with_view += arr[i] - max_height

    print(f'#{tc} {building_with_view}')