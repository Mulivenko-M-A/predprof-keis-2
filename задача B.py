a = input() + " "
b = []
B = -1
co1 = True
co2 = True
for i in range(0,a.count(" ")):
    b.append(a[:a.find(" ")])
    a = a[a.find(" ")+1:]
for j in range(0,len(b)):
    c = b.copy()
    del c[j]
    for k in range(0,len(c)):
        A = int(c[k])
        if not(B < A):
            co1 = False
        B = A
    if co1:
        print("true")
        co2 = False
        break
    co1 = True
    B = -1
if co2:
    print("false")