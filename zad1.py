from typing import Any


class Node: 
    def __init__(self,value: Any)->None:
        self.value: Any = value 
        self.next = None

   


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self,value: Any):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append(self,value: Any):
        new_node = Node(value)
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node

    def node(self, at:int)->Node:
        current = self.head
        count = 0
        while (current):
            if(count==at):
                return current.value
            count+=1
            current = current.next

    def insert(self,value:Any,after):
       new_node = Node(value)
       current = self.head
       count = 0
       while(current):
           if(count==after):
               current = new_node.next



    
        
    def __str__(self):
        
        # defining a blank res variable
        res = ""
          
        # initializing ptr to head
        ptr = self.head
          
       # traversing and adding it to res
        while ptr:
            res += str(ptr.value) + ", "
            ptr = ptr.next
  
       # removing trailing commas
        res = res.strip(", ")
          
        # chen checking if 
        # anything is present in res or not
        if len(res):
            return "[" + res + "]"
        else:
            return "[]"

list_ = LinkedList()
list_.push(1)
list_.push(0)
list_.push(9)
list_.push(10)
list_.append(13)
list_.push(15)
list_.append(1223)
list_.push(2137)
list_.append(4200)
print(list_)
list_.node(5)
print(list_.insert(11231237,1))
print(list_)
