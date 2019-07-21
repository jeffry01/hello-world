sentence=str(input())
x=int(input())
y=int(input())

a=list(sentence)
for i in range(0,len(a)):
    askii=ord(a[i])
    if askii>=97 and askii<=122:
         askii=askii+x
         a[i]=chr(askii)
    if askii>=48 and askii<=57 :
        
        askii=askii+y
        a[i]=chr(askii)
   
    else:
        continue

        
       
final=''.join(a)
print(final)
        
        
        
