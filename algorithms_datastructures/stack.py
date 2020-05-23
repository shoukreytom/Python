class Stack(object):
    def __init__(self, head):
        self.storage = [head]
    
    def enqueue(self, new_element):
        self.storage.append(new_element)
    
    def peek(self):
        return self.storage[0]
    
    def dequeue(self):
        return self.storage.pop(0)


def main():
    stack = Stack(1)
    stack.enqueue(3)
    stack.enqueue(5)
    print (stack.peek())
    stack.dequeue()
    print(stack.peek())


if __name__ == "__main__":
    main()
