def removeDuplicated(nums):
    index=0
    k=1
    size=len(nums)
    
    while index < size-1:
        # print("in")
        if nums[index]==nums[index+1]:
            check=index+1
            while check+1<size:
                nums[check]=nums[check+1]
                check+=1

            # nums[check]='_'
            size -= 1 

        else:
            index+=1
            k+=1

    # index=0
    # while nums[index] != '_':
    #     k+=1
    #     index+=1

    return k,nums 




array=[1,1,3,4,5,5]
k,result=removeDuplicated(array)
print(k,result)

            

            



        
