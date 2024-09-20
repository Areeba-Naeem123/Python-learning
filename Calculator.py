var1=float(input("Please Enter number 1:"))
var2=float(input("Please Enter number 2:"))
option=int(input("Choose from following:1-Addition\n2- Subtraction\n3- Multiplication\n4- Division \n5- Flooral division\n 6- Exponential"))
if(option==1): 
    print("num1+num2:",var1+var2)
elif(option==2):
    print("num1-num2:",var1-var2)
elif(option==3):
    print("num1*num2:",var1*var2)
elif(option==4):
    if(var2==0):
        print("num1/num2:",var2/var1)
        print("num1/num2:",var1/var2)
    elif((var1==0 )and (var2==0)):
        print("0/0 Condition not valid")

elif(option==5):
    print("num1//num2:",var1/var2)
elif(option==2):
    print("num1**num2:",var1**var2)    
