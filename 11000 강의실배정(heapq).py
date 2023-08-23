import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
lecture = []
# [시작 시간, 끝 시간] 형태로 강의를 저장한 lecture
# lecture는 시간 시간의 오름차순으로 정렬됨
for _ in range(N):
    heapq.heappush(lecture, list(map(int, input().split())))

# 강의의 끝나는 시간을 저장하는 end_points
end_points = []
while lecture:
    # 가장 일찍 시작하는 강의부터 꺼냄
    l = heapq.heappop(lecture)
    # 진행중인 강의가 있을 때
    if end_points:
        # l의 시작시간이 진행중인 강의중 가장 빨리 끝나는 것보다 늦거나 같다면
        if l[0] >= end_points[0]:
            # 그 강의실에서 다음 강의 진행
            heapq.heappop(end_points)
    # 그 강의실의 끝나는 시간을 l의 끝나는 시간으로 변경
    heapq.heappush(end_points, l[1])
    print(lecture)
    print(end_points)

print(len(end_points))

