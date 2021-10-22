from typing import Any


class Node: 
    def __init__(self,value: Any)->None:
        self.value: Any = value 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self,value: Any)->None:
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append(self,value: Any) -> None:
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

   
    def insert(self, value: Any, after: Node) -> None:
        new_node = Node(value)
        current = self.head
        count = 0
        while(current):
            if(count==after):
                tmp = current.next
                current.next=new_node
                new_node.next = tmp
            count+=1
            current = current.next
    
    def pop(self)->Any:
        current = self.head
        self.head = current.next
        return current.value
 
    def remove_last(self)->Any:
        current = self.head
        while(current.next.next!=None):
            current = current.next
        last_node = current.next
        print(last_node.value)
        current.next = None
        last_node = None

    def remove(self, after: Node) -> Any:
        current = self.head
        count = 0
        while(current):
            if(count==after):
                tmp = current.next
                current.next = current.next.next
            count+=1
            current = current.next

    def print(self):
        current = self.head
        string = ""
        while(current!=None):
            if current.next!=None:
                string+=str(current.value)+"->"
            else:
                string+=str(current.value)
            current = current.next
        return string

    def len(self):
        current = self.head
        count = 0
        while(current!=None):
            count+=1
            current = current.next
        return count


list_ = LinkedList()
assert list_.head == None
list_.push(1)
list_.push(0)
print(list_.print())
list_.append(9)
list_.append(10)
print(list_.print())
middle_node = list_.node(at=1)
list_.insert(5, after=middle_node)
print(list_.print())
first_element = list_.node(at=0)
returned_first_element = list_.pop()
print(returned_first_element)
print(list_.print())
last_element = list_.node(at=3)
returned_last_element = list_.remove_last()
returned_last_element
print(list_.print())
second_node = 1
list_.remove(second_node)
print(list_.print())
