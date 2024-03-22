romans={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
exp=list(input())
prev=0
total=0
for i in exp:
    total+=romans[i]
    if romans[i]>prev:
        total-=2*prev
    prev=romans[i]
print (total)
    
