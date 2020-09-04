# (정렬) 나이순 정렬
N = int(input())
array=[]
for _ in range(N):
    x, y = input().split(" ")
    array.append((x,y))
array = sorted(array, key = lambda x: (int(x[0])))
for i in array:
    print(str(i[0])+ " "+ str(i[1]))