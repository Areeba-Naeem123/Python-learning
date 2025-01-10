class Node:
    def __init__(self,data):
        self.data=data
        self.next=None



class linkedList:
    def __init__(self):
        self.head=None
    
    def insertAtStart(self,data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode
    

    def insertAtEnd(self,data):
        newNode=Node(data)
        if not self.head:
            newNode.next=self.head
            self.head=newNode
        else:
            currentNode=self.head

            while currentNode.next :
                currentNode=currentNode.next

            currentNode.next=newNode

    def delete_start(self):
        if not self.head:
            print("no node found")
            return 
        else :
            toDelete=self.head
            self.head=self.head.next
            toDelete=None
            return 

    def delete_end(self):
        if not self.head:
            print("No node found")
            return 
        else:
            current=self.head
            previous=self.head

            while current.next :
                previous=current
                current=current.next

            current=None 
            previous.next=None
        
    def print_list(self):
        if not self.head:
            print("Null list")
        else:
            current=self.head
            while current:
                print(f"{current.data} -> ",end="")
                current=current.next

    def mergeTwoLists(self, list1,list2):
        Dumy=Node(0)
        current=Dumy

        p1=list1.head
        p2=list2.head
        while p1 and p2:
            if p1.data < p2.data:
                current.next=p1
                p1=p1.next
            else:
                current.next=p2
                p2=p2.next 
            
            current=current.next
        
        if p1:
            current.next=p1
        if p2:
            current.next=p2

        mergedList=linkedList()
        mergedList.head=Dumy.next
        return mergedList
    






list1= linkedList()

print("\ndelete at start ")

list1.delete_start()
list1.print_list()

list1.insertAtEnd(1)
list1.insertAtEnd(1)
list1.insertAtEnd(3)
list1.insertAtEnd(43)
list1.insertAtEnd(43)
list1.insertAtEnd(82)
list1.print_list()
            
print("\nat end\n ")
list2= linkedList()
list2.insertAtEnd(10)
list2.insertAtEnd(20)
list2.insertAtEnd(30)
list2.insertAtEnd(40)
list2.insertAtEnd(50)
list2.insertAtEnd(60)
list2.insertAtEnd(70)
list2.insertAtEnd(80)
list2.print_list()
print("\ndelete at end\n ")
list2.delete_end()
list2.print_list()




# ===============================================
print("\n\nmerged\n")
l3=linkedList()
l3=l3.mergeTwoLists(list1,list2)
l3.print_list()



