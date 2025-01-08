
def twosum(array,target):
    output=list()
    for index_i,i in enumerate(array):
        for index_j,j in enumerate(array[index_i+1:], start=index_i+1):

            if(target== (i+j)):
                output.append(index_i)
                output.append(index_j)
                return output
            
    
    return output
    
    
array=[2,7,11,15]
target=9
ans=twosum(array,target)

print (ans )
