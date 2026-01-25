a, b = map(int, input().split())
c, d = map(int, input().split())

# Please write your code here.

cleaning=0
if b<c or d<a:
    cleaning+=((b-a)+(d-c))
else:
    cleaning+=(max(a,b,c,d)-min(a,b,c,d))

print(cleaning)