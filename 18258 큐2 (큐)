from sys import stdin
def input():
    return stdin.readline().rstrip()

# 단순 리스트로 구현하면 시간 초과 발생
# COUNT를 이용하여 pop 시 리스트 전체 재정렬을 막음
class Queue:
    def __init__(self):
        self.queue=[]
        self.COUNT= 0
    def push(self, item):
        self.queue.append(item)
    def pop(self):
        if len(self.queue) > self.COUNT:
            print(self.queue[self.COUNT])
            self.COUNT += 1
        else:
            print("-1")
    def size(self):
        print(len(self.queue)-self.COUNT)
    def empty(self):
        if len(self.queue) == self.COUNT:
            print("1")
            self.COUNT=0
            self.queue=[]
        else:
            print("0")
    def front(self):
        if len(self.queue) > self.COUNT:
            print(self.queue[self.COUNT])
        else:
            print("-1")
    def back(self):
        if len(self.queue) > self.COUNT:
            print(self.queue[-1])
        else:
            print("-1")

N=int(input())
myQueue=Queue()
for i in range(N):
    INPUT=input().split()
    if INPUT[0] == 'push':
        myQueue.push(int(INPUT[1]))
    elif INPUT[0] == 'pop':
        myQueue.pop()
    elif INPUT[0] == 'size':
        myQueue.size()
    elif INPUT[0] == 'empty':
        myQueue.empty()
    elif INPUT[0] == 'front':
        myQueue.front()
    elif INPUT[0] == 'back':
        myQueue.back()
        
