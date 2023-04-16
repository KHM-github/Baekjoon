from sys import stdin
def input():
    return stdin.readline().rstrip()

n = input()
card = list(map(int,input().split()))
m = input()
test = list(map(int,input().split()))

hash = {}

for i in card:
    if i in hash:
        hash[i] += 1
    else:
        hash[i] = 1

for i in test:
    if i in hash:
        print(hash[i], end=' ')
    else:
        print(0, end=' ')     
