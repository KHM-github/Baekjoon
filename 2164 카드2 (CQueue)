# 시간 초과 방지를 위해 원형 큐로 구현

class CQueue:
    def __init__(self,size):
        self.count=0
        self.front=0
        self.rear=0
        self.size=size
        self.cqueue=[None]*self.size
    def enqueue(self,item):
        self.rear=(self.rear+1)%self.size
        self.cqueue[self.rear]=item
        self.count+=1
    def dequeue(self):
        self.front=(self.front+1)%self.size
        item=self.cqueue[self.front]
        self.cqueue[self.front]=None
        self.count-=1
        return item

N=int(input())
q=CQueue(N)
for i in range(N):
    q.enqueue(i+1)
for i in range(N-1):
    q.dequeue()
    second=q.dequeue()
    q.enqueue(second)

print(q.cqueue[q.rear])
