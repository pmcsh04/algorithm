# (정렬) 통계학

from collections import Counter

N = int(input())

array=[]
for _ in range(N):
    array.append(int(input()))

one = 0
for i in array:
    one += i
one /= len(array)
one = round(one)
print(one) # 첫번째

two = sorted(array)
print(two[len(array)//2]) # 두번째

c = Counter(array)
order = c.most_common()
maximum = order[0][1]

modes = []
for num in order:
    if num[1] == maximum:
        modes.append(num[0])

#three = sorted(list(set(array)))

modes = sorted(modes)

if len(modes) >= 2 : # 여러개 있을때
    print(modes[1])
else: # 최빈값이 있을때
    print(modes[0])
#print(modes)

four = max(array) - min(array)
print(four) # 네번째