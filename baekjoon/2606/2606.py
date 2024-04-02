class Computer :
    def __init__(self, number) :
        self.number = number
        self.link = []

len_compute = int(input())
input_length = int(input())
computers = {}
for _ in range(input_length) :
    a, b = input().strip().split(' ')
    if a not in computers :
        computers[a] = Computer(a)
    if b not in computers :
        computers[b] = Computer(b)
    computers[a].link.append(computers[b])
    computers[b].link.append(computers[a])

wormed = set()
def worming(computer) :
    wormed.add(computer)
    links = computer.link
    targets = []
    for compute in links :
        if compute not in wormed :
            wormed.add(compute)
            targets.append(compute)
    for target in targets :
        worming(target)
if '1' in computers :
    worming(computers['1'])
    print(len(wormed)-1)
else :
    print(0)