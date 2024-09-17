dictionary1={

    "student1":"Areeba",
        "student2":"Zain",
    "student3":"hifza",
    "student4":"khadija",
    "student5":"Ali",


}

print("-----------task1 ----------")
sorted_dic= dict(sorted(dictionary1.items(), key=lambda item: item[1]))

print(sorted_dic)

dictionary2={

    "student1":"usman",
        "student2":"ali",
    "student1":"faiq"}


# # dictionary.sort()
# # print(dictionary1)


print("-----------task2 ----------")
check="Ali"
print(check in dictionary1)

print("-----------task3 ----------")

dictionary1.update(dictionary2)
print(dictionary1)


print("-----------task 4 and 5 ----------")

tupple1=(
    "apple",123,"macbook","m1"
)
tupple2=("areeba",)
print(tupple1+tupple2)





print("-----------task6 ----------")

list1=[1,2,3]

print("Sum of list values:",sum(list1))

print("-----------task7 ----------")

list1=[1,2,3,4,5,68,7]

print(max(list1))

print("-----------task8 ----------")
set1={1,2,3,45}
set1.update([5,9,7])
print(set1)



print("-----------task9 ----------")
array1=[1,2,3,4,5]
array1.reverse()

print(array1)

print("-----------task10 ----------")
array2=[1,2,3,4,5]
print(array2[0],array2[1],array2[2],array2[3],array2[4])
