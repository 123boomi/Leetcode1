ops=[]
n=int(input("no: of operations"))
while n>0:
    ops.append(input("enter operations"))
    n=n-1
stack=[]
for item in ops:
    if item.isnumeric():
        if type(item)==int:
            stack.append(int(item))
        elif item=="C":
            stack.pop()
        elif item=="D":
            top=stack[-1]
            stack.append(2*top)
        elif item=='+':
            a=stack[-1]
            b=stack[-2]
            stack.append(a+b)
print(sum(stack))
