def solution(targets) :
    class Node :
        def __init__(self, widths) :
            self.start, self.end = widths
            self.left = None
            self.middle = None
            self.right = None

    class TargetTree :
        def __init__(self) :
            self.head = None
            self.cnt = 0

        def link_target(self, widths) :
            if self.head is None :
                self.head = Node(widths)
                self.cnt += 1

            else :
                nodes = [self.head]
                while nodes :
                    n = nodes.pop()
                    # 범위가 통하는 경우
                    if n.start < widths[1] and n.start >= widths[0] :
                        if n.middle is None :
                            n.middle = [Node(widths)]
                        else :
                            n.middle.append(Node(widths))

                    # 값이 더 큰 경우
                    elif n.end <= widths[0] :
                        if n.right is None :
                            n.right = Node(widths)
                            self.cnt += 1
                        else :
                            nodes.append(n.right)
                    # 값이 더 작은 경우
                    else :
                        if n.left is None :
                            n.left = Node(widths)
                            self.cnt += 1
                        else :
                            nodes.append(n.left)
    targets.sort(key = lambda x : x[1] - x[0])
    t = TargetTree()
    for target in targets :
        t.link_target(target)
    return t.cnt