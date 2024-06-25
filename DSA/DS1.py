class Queue(object):
    def __init__(self):
        self.queue = []
        self.front = -1
        self.rear = -1
        self.size = 0
        self.max = 10

    #enqueue
    def enqueue(self,data):
        if self.size >= self.max:
            return "Enqueue not possible"

        if self.size == 0:
            self.front+=1
        self.rear+=1
        self.queue.append(data)
        self.size+=1

    #dequeue
    def dequeue(self):
        if self.size <= 0:
            return "Underflow"

            # Remove the front element from the queue
        removed_element = self.queue[self.front]

        # Move front pointer to the next element
        self.front += 1

        # Update size
        self.size -= 1

        return removed_element
    #display

    def print_queue(self):
        if self.size==0:
            print("Queue is empty")

        for i in range(self.front,self.rear+1):
            print(self.queue[i],end=" ")
        print()



class Stack(object):
    def __init__(self):
        self.stack = []
        self.top = -1
        self.size = 0;
        self.max = 10

    def push(self,data):
        if self.size>=self.max:
            return "Stack Overflow"

        self.stack.append(data)
        self.top+=1
        self.size+=1

    def pop(self):
        if self.size <= 0:
            return "Stack Empty"

        data = self.stack[self.top]
        self.stack.pop()  # Remove the top element from the stack
        self.top -= 1
        self.size -= 1
        return data

    def print_stack(self):
        if self.size == 0:
            print("Stack is empty")
        for i in range(0,self.top+1):
            print(self.stack[i],end=' ')
        print()


# LinkedList
class Node(object):
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = None

    def insert(self,data):
        new_node = Node(data,self.head)
        self.head = new_node

    def insert_at(self,index,data):
        if index<0:
            return
        #base case
        self.head = self.insert_at_recursive(self.head,index,data)

    def insert_at_recursive(self,current,index,data):
        if index==0 or current is None:
            new_node = Node(data)
            new_node.next = current
            return new_node

        current.next = self.insert_at_recursive(current.next,index-1,data)
        return current
    def delete(self):
        if self.head is None:
            print("Head is empty")
            return
        self.head = self.head.next

    def printLL(self):
        if self.head is None:
            print("LL is empty")
            return

        listr = ''
        itr = self.head
        while itr:
            listr += str(itr.data)+' '
            itr = itr.next
        print(listr)

def fibonacci(n):
    memo = {}
    def f(m):
        if m==1 or m==2:
            return 1
        if m in memo:
            return memo[m]
        memo[m] =  f(m-1) + f(m-2)
        return memo[m]
    return f(n)

# print(list(fibonacci(i) for i in range(1,10)))

def factorial(n):
    return (1 if n==0 or n==1 else n*factorial(n-1))
print(list(factorial(i) for i in range(0,10)))

#main function
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert(1)
    ll.insert(23)
    ll.insert(25)
    ll.insert_at(0,100)
    # ll.delete()
    # ll.delete()
    # ll.delete()
    ll.printLL()

