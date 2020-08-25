num = int(input())
answer = 0

for i in range(1,num+1):
    array = map(int,list(str(i)))
    answer = i + sum(array)
    if answer == num:
        print(i)
        break
    if i == num:
        print(0)
