xs=[]
for x in range(0,3):
    xs.append(input())
print(f"{xs}\n")

ys=xs[:]
ys.remove(ys[x])
print(ys)