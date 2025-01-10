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
        


list1= linkedList()
list1.insertAtStart(2)
list1.insertAtStart(3)
list1.insertAtStart(4)
list1.insertAtStart(5)
list1.insertAtStart(6)
list1.print_list()
print("\ndelete at start ")

list1.delete_start()
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



