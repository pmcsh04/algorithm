def solution(numbers, target):
    # DFS
    tree = [0]  # top node
    for num in numbers:  # 배열안에 있는 숫자: num
        sub_tree = []
        for tree_num in tree:  # tree에 있는 숫자를 다 빼와서 num과 연산
            sub_tree.append(tree_num + num)
            sub_tree.append(tree_num - num)
        tree = sub_tree  # tree 갱신 -> 다음 num을 빼온다.

    return tree.count(target)  # target의 값을 찾는다.