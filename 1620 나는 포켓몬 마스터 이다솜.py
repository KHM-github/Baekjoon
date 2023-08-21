from sys import stdin

#일반 input()으로는 시간 초과 발생
#따라서 stdin으로 input() 재정의

def input():
    return stdin.readline().rstrip()


n, m = map(int, input().split())
by_id = {}
by_name = {}

for i in range(1, n + 1):
    pokemon = input()
    by_id[i] = pokemon
    by_name[pokemon] = i

for _ in range(m):
    x = input()
    if x.isdigit():
        print(by_id[int(x)])
    else:
        print(by_name[x])
    
