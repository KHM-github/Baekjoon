import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = []
total = 1

for i in range(N):
    a,b = map(int, input().split())
    arr.append((a,b))
    
# 튜플의 두번째 요소 우선, 같을 경우 첫번째 요소를 고려하여 오름차순 정렬
arr.sort(key = lambda x : (x[1],x[0]))
end_time = arr[0][1]

for i in range(1,N):
    if arr[i][0] >= end_time:
        end_time = arr[i][1]
        total += 1

print(total)
