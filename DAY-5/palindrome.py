'''s=input()
i=0;
j=len(s)-1
while (i<=j):
    if s[i]!=s[j]:
        print("Not palindrome")
        break
    i+=1
    j=-1
else:
    print("Palindrome")'''
def fun(s,i,j):
    if i>j:
        return True
    if s[i]!=s[j]:
        return False
    return fun(s,i+1,j-1)
s=input()
print(fun(s,0,len(s)-1))

    
