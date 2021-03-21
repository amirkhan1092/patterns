a1='A'
b1='P'
for l in range(1,5):
    for k in range(ord(a1),ord(a1)+l):

        print(chr(k),end=' ')
    for p in range(ord(b1)+l-1,ord(b1)+3):
        print(chr(p),end=' ')
    print()
    
    
'''
   A
  AM
 AMI
AMIR 
'''  
name = input('Enter the name ')
ln = len(name)
for i in range(ln):
    print(f'{{0:>{ln}}}'.format(name[:i+1]))
