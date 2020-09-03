N = int(input())
array=[]
for _ in range(N):
    array.append(input())
#print(array)
array = list(set(array))
array = sorted(array, key = lambda x : (len(x), x))
#print(array)
for i in range(len(array)):
    print(array[i])