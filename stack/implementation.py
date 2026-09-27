# this is the implementation through list.

class stack:
    def __init__(self):
        self.st = []

    def push(self, x):
        self.st.append(x)

    def pop(self):
        if len(self.st) == 0:
            return -1
        x = self.st[-1]
        self.st.pop()
        return x

    def top(self):
        if len(self.st) == 0:
            return -1
        return self.st[-1]

    def size(self):
        return len(self.st)

    def display(self):
        if len(self.st) == 0:
            print("empty stack..")
            return
        for i in range(len(self.st)-1, -1, -1):
            print(self.st[i])


s = stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.push(60)
s.pop()
print(s.pop())
print(s.top())
print(s.size())
s.display()

# linked list representattion of stack.

class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def push(self, x):
        self.length += 1
        if self.top is None:
            self.top = node(x)
            return

        newNode = node(x)
        newNode.next = self.top
        self.top = newNode

    def pop(self):
        if self.top == None:
            return -1
        self.length -= 1
        x = self.top.data
        self.top = self.top.next
        return x

    def topElement(self):
        if self.top == None:
            return -1
        return self.top.data

    def size(self):
        return self.length

    def display(self):
        for i in range(self.length):
            print(self.top.data)
            self.top = self.top.next


s = stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.pop()
s.pop()
print(f"size of stack is - {s.size()}")
print(f"top element of the stack - {s.topElement()}")
print("stack elements are : ", end="\n")
s.display()
