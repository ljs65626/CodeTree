import sys
words = input()
d={}
# Please write your code here.
for word in words:
    if word in d:
        d[word]+=1
    else:
        d[word]=1

for word in words:
    if d[word]==1:
        print(word)
        sys.exit()

print('None')