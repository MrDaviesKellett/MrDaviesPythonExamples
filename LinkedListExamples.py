class LinkedListSingle():
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def push(self,data):
        if self.next == None:
            self.next = LinkedListSingle(data)
        else:
            self.next.push(data)

    def __str__(self):
        s = str(self.data)
        if self.next != None:
            s = s + ', ' + str(self.next)
        return s

    def first(self):
        return self.data


LL = LinkedListSingle(5)
LL.push(7)
LL.push(6)
LL.push(2)
LL.push(3)
LL.push(4)
LL.push(10)
print(LL)
print(LL.first())
print(LL.last())