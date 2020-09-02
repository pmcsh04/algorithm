N = int(input())
array=[]
for _ in range(N):
    x, y = map(int, input().split(" "))
    array.append((x,y))

#print(array)
#array.sort()
p = sorted(array, key= lambda x: (x[1], x[0]))
for i in p:
    print(str(i[0])+" "+str(i[1]))
#print(array)