a1='A'
b1='P'
for l in range(1,5):
    for k in range(ord(a1),ord(a1)+l):

        print(chr(k),end=' ')
    for p in range(ord(b1)+l-1,ord(b1)+3):
        print(chr(p),end=' ')
    print()