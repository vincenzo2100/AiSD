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


class Queue:
    def __init__(self):
        self._storage = None

    def peek(self)->Any:
        return self._storage

    def enqueue(self, element: Any) -> None:
        new_node = Node(element)
        current = self._storage
        if(self._storage)==None:
            self._storage = new_node
        else:
            while(current.next!=None):
                current = current.next
            current.next = new_node

            
            
    def dequeue(self) -> Any:
        current = self._storage
        self._storage = current.next
        return current.value

    def print(self):
        current = self._storage
        string = ""
        while(current!=None):
            string+=current.value+" "
            current = current.next
        return string

    def len(self):
        current = self._storage
        count = 0
        while(current!=None):
            count+=1
            current = current.next
        return count

queue = Queue()
print(queue.print())
queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')
print(queue.print())
client_first = queue.dequeue()
print(queue.print())
print(queue.len())