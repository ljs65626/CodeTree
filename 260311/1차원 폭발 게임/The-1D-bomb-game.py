import copy
import sys
n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]


def get_end_index_of_explosion(start, numbers):
    for i in range(start+1, len(numbers)):
        if numbers[start]!=numbers[i]:
            return i-1
    return len(numbers)-1

while True:
    exploded=False

    for i, num in enumerate(numbers):

        if num==0:
            continue

        end = get_end_index_of_explosion(i, numbers)
        if end-i+1>=m:
            exploded=True
            numbers[i:end+1] = [0]*(end-i+1)
    
    numbers = list(filter(lambda x: x>0, numbers))
    # print(numbers)

    if exploded==False:
        break

print(len(numbers))
for i in numbers:
    print(i)



