
a=1
b="areeba"
c=9.087
d=False
print(type(a) )
print(type (b))
print(type (c))

print(a+c)
#print(a+b) # error : it cannot concatenate directly as we do in js 

########### Built in data types #######
# Numeric data types : int, float ,complex

complex_number=complex(8,2)
print(complex_number)

#list: order collection of datatypes 
#mutable == changeable 
list1=[3,2.2,[-4,5],"apple"]
print(list1)
#tuple: immutable == unchangable 
list2=(3,2.2,(-4,5),("apple","peach"))
print(list2)

#mapped data :dictionary 
#it means collection of key value pairs
dictionary={"name":"areeba",
            "age":20,
            "gender":"female"}
print(dictionary)
