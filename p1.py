n = int(input())
l = []

if n<0:
    print("invalid Input")
elif n==0:
    print("invalid Input")
else:
    for i in range(n+1):
        inp = input()
        l.append(inp)

    lens = sorted(l, key = len)
    print(lens)    
    print(lens[0])
