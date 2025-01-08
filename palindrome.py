def palindrome(x):
    original=x
    if x<0:
        return False
    reverse=0
    while (x!=0):
        remainder=x%10
        reverse=reverse*10+remainder
        x=x//10

    
    if reverse==original:
        return True
    else:
        return False
    
ans=palindrome(121)
print(ans)
