import sys
N = int(int(sys.stdin.readline()))
array = [0] * 10000

for _ in range(N):
   array[(int(sys.stdin.readline()))-1] += 1

for i in range(10000):
   [print(i+1) for _ in range(array[i])]
