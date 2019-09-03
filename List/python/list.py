N = int(input())

L=[]
for i in range (N):
    n=[(x) for x in input().split(' ')]
    if n[0]=='insert':
        L.insert(int(n[1]),int(n[2]))
    if n[0]=='remove':
        L.remove(int(n[1]))
    if n[0]=='append':
        L.append(int(n[1]))
    if n[0]=='sort':
        L.sort()
    if n[0]=='pop':
        L.pop()
    if n[0]=='reverse':
        L.reverse()
    if n[0]=='print':
        print(L)
