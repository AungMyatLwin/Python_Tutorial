class Node:
    def __init__(self,value):
        self.value=value
        self.next=None


class LinkedList:
    def __init__(self,value):
        new_node=Node(value=value)
        self.head=new_node
        self.tail=new_node
        self.lenght=1

    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=self.next


    def append(self,value):
        new_node=Node(value=value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.lenght+=1
        return True           

    def pop(self):
        if self.lenght==0:
            return None
        temp=self.head
        pre=self.head
        while(temp.next):
            pre=temp
            temp=temp.next
        self.tail=pre
        self.tail.next=None
        if self.lenght==0:
            self.head=None
            self.tail=None
        return temp

    def prepend(self):
        pass
    def pop_first(self):
        pass
    

my_linked_list=LinkedList(4)
print(my_linked_list.head.value)