a=list(map(int,input().split()))
b=[]
for i in range(len(a)-1):
    if a[i]> max(a[i+1:]):
        b.append(a[i])
b.append(a[-1])
print(b)
