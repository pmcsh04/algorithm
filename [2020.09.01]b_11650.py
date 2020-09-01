N = int(input())
array=[]
for _ in range(N):
    x, y = map(int, input().split(" "))
    array.append((x,y))

#print(array)
array.sort()
for i in array:
    print(str(i[0])+" "+str(i[1]))
#print(array)