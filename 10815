input()
CARD = list(map(int, input().split()))
CARD.sort()


def binary_search(target,data):
    start=0
    end=len(data)-1

    while start <= end:
        mid=(start+end) //2

        if data[mid] == target:
            return 1
        elif data[mid] < target:
            start=mid+1
        else:
            end=mid-1
    return 0

input()
for item in list(map(int,input().split())):
    print(binary_search(item,CARD),end=' ')
