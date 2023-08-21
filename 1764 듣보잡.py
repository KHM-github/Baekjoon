from sys import stdin
def input():
    return stdin.readline().rstrip()

N, M = map(int, input().split())
non_see=[]
non_heard=[]

for i in range(N):
    non_see.append(input())
for i in range(M):
    non_heard.append(input())

hash = {}

for i in non_see:
    if i in hash:
        hash[i] += 1
    else:
        hash[i] = 1

for i in non_heard:
    if i in hash:
        hash[i] += 1

non_see_heard=[]
for key,value in hash.items():
    if value ==2:
        non_see_heard.append(key)
non_see_heard.sort()

print(len(non_see_heard))
for item in non_see_heard:
    print(item)
