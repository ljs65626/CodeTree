N = int(input())
moves = [tuple(map(int, input().split())) for _ in range(N)]


# Please write your code here.

#1이 이기는 경우. 1=가위
#2가 이기는 경우. 2=바위
#3이 이기는 경우. 3=보
cnt11=0
cnt12=0
cnt21=0
cnt22=0
cnt31=0

for a, b in moves:
    if (a==1 and b==3) or (a==3 and b==2) or (a==2 and b==1):
        cnt11+=1
    if (a==1 and b==2) or (a==2 and b==3) or (a==3 and b==1):
        cnt12+=1
    if (a==1 and b==2) or (a==2 and b==3) or (a==3 and b==1):
        cnt21+=1
    if (a==1 and b==3) or (a==2 and b==1) or (a==3 and b==2):
        cnt22+=1
    if (a==1 and b==3) or (a==2 and b==1) or (a==3 and b==2):
        cnt31+=1
    if (a==1 and b==2) or (a==2 and b==3) or (a==3 and b==1):
        cnt32+=1
    

print(max(cnt11, cnt12, cnt21, cnt22, cnt31, cnt32))