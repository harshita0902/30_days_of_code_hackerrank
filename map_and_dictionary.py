n=int(input())
d = {}
for i in range(n):
     x = input().split()
     d[x[0]]=x[1]
while True:
    try:
        q = input()
        if q == "":
            break
        if q in d:
            print(''.join([q,"=",d[q]]))
        else:
            print("Not found")
    except:
        break
    

# Enter your code here. Read input from STDIN. Print output to STDOUT
