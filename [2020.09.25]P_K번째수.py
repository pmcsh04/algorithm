def solution(array, commands):
    answer = []
    for a in range(len(commands)):
        [i, j, p] = commands[a]
        array_sort = sorted(array[i - 1:j])
        answer.append(array_sort[p - 1])
    return answer
