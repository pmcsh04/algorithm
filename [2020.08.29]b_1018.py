N, M = map(int,input().split(" "))
map = [list(input()) for _ in range(N)]
array = []

for a in range(N-7):
    for b in range(M-7):
        x = 0
        y = 0
        for c in range(a, a + 8):
            for d in range(b, b + 8):
                if (c+d)%2 ==0:
                    if map[c][d] != 'W':
                        x += 1
                    if map[c][d] != 'B':
                        y += 1
                else:
                    if map[c][d] != 'B':
                        x += 1
                    if map[c][d] != 'W':
                        y += 1
        array.append(x)
        array.append(y)
print(min(array))