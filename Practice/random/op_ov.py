class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, __head=None):
        self.__head = __head

    def push(self, val):
        newnode = Node(val)
        if not self.__head:
            self.__head = newnode
            return
        newnode.next = self.__head
        self.__head = newnode

    def __str__(self):
        result = ''
        currentnode = self.__head
        while currentnode:
            result += f'{currentnode.val} -> '
            currentnode = currentnode.next
        return result + 'end'
    
    def __add__(self, other):
        if not self.__head:
            self.__head = other.__head
            return self
        currentlistnode = self.__head
        while currentlistnode.next:
            currentlistnode = currentlistnode.next
        currentlistnode.next = other.__head
        return self

    
ll1 = LinkedList(Node(1, Node(2, Node(3))))
ll2 = LinkedList(Node(4, Node(5, Node(6))))
ll3 = LinkedList() + ll2

ll3.push(3)

print(ll2, ll3)

        