N, M = map(int,input().split(" "))
a = list(map(int,input().split(" ")))

num = 0
answer = []
for i in range(0,N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            num = a[i] + a[j] + a[k]
            if num <= M:
                answer.append(num)

print(max(answer))
