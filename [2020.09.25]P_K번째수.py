def solution(array, commands):
    answer = []
    for a in range(len(commands)):
        [i, j, p] = commands[a]
        array_sort = sorted(array[i - 1:j])
        answer.append(array_sort[p - 1])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
