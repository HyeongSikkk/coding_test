def solution(n, wires) :

    class ElectroTree :
        def __init__(self, wires) :
            self.wires = wires
            self.build()


        def build(self) :
            towers = {}
            for wire in self.wires :
                a, b = wire
                if a in towers :
                    node_a = towers[a]
                else :
                    node_a = Node(a)
                    towers[a] = node_a

                if b in towers :
                    node_b = towers[b]
                else :
                    node_b = Node(b)
                    towers[b] = node_b

                node_a.connect(node_b)
            self.towers = towers


        def split_test(self) :
            def count(node, links) :
                links.add(node)
                for n in node.link :
                    if not n in links :
                        count(n, links)
                return links

            min_value = len(self.wires)
            for wire in self.wires :
                a_link, b_link = set(), set()
                a, b = wire
                node_a, node_b = self.towers[a], self.towers[b]
                node_a.disconnect(node_b)
                a_link = count(node_a, a_link)
                b_link = count(node_b, b_link)
                len_a, len_b = len(a_link), len(b_link)
                if len_b > len_a :
                    len_a, len_b = len_b, len_a
                value = len_a - len_b
                if value < min_value :
                    min_value = value
                node_a.connect(node_b)
            return min_value


    class Node :
        def __init__(self, area) :
            self.area = area
            self.link = None


        def connect(self, other) :
            if self.link == None :
                self.link = [other]
            else :
                self.link.append(other)

            if other.link == None :
                other.link = [self]
            else :
                other.link.append(self)


        def disconnect(self, other) :
            self.link.remove(other)
            other.link.remove(self)

    t = ElectroTree(wires)
    return t.split_test()
