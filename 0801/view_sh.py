
N = int(input())

arr = list(map(int,input().split()))

old_arr = len(arr)
arr.insert(0,0)
arr.insert(0,0)
arr.append(0)
arr.append(0)

view = 0

def find_view(a,b,c,d,e) :

    global view

    list = [a,b,c,d,e]

    if max(list) == c :

        list.sort(reverse = True)
        view = view + list[0] - list[1]

for i in range(2, 2 + old_arr) :

    find_view(arr[i-2],arr[i-1],arr[i],arr[i+1],arr[i+2])


print(f"#{tc} {view}")