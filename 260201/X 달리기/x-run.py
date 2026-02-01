X = int(input())

# Please write your code here.
velocity = 1
distance = 0


def remain(N):
    return N*(N+1)//2

def velocity_is(cur_location, cur_velocity):
    remain_distance = X - cur_location
    if remain_distance>=remain(cur_velocity+1):
        return cur_velocity+1
    elif remain_distance>=remain(cur_velocity):
        return cur_velocity
    return cur_velocity-1

ans=0
for _ in range(X):
    distance+=velocity
    velocity = velocity_is(distance, velocity)
    ans+=1
    if distance==X:
        break

print(ans)
