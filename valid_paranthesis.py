# stack in linked list with class---------------------------------------------------->
# for node
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class Stack:
    def __init__(self):
        self.top=None
        
    def isEmpty(self):    #for empty stack checking
        # return self.top==None
        if self.top == None:
            return True   #"yes stack is empty"
        else:
            return False  #"stack  is not empty"

    def push(self,value): #for pushing vlaue into stack
        new_node=Node(value)
        new_node.next=self.top
        self.top=new_node
        
    def peek(self):        #peak value (top value) from stack
        if self.top == None:
            return 'stack is empty'
        else:
            print(f"peek element is :{self.top.data}")
        
    def traversal(self):   #traverase and count the elemnts in stack
        count=0
        temp=self.top
        while temp is not None:
            count+=1
            data=temp.data
            # print(data)  optional*
            temp=temp.next
        print(f"total elements in stack is {count}")
            
    def pop(self):         #pop or delete last element
        temp=self.top
        if temp is None:
            print("stack is now empty you cant pop up now")
        else:
            data=self.top.data
            self.top = self.top.next
            # print(f"removed element is {temp.data}") #for printing removed element
            return data
        
    

s=Stack()   # s is a object from stack() class

def valid_paranthesis(expression):
    open={'(':')','[':']','{':'}'}
    close={')',']','}'}
    s=Stack()              #new object of stack called 's'
    for char in expression:
        if char in open:
            s.push(char)    #pushing open parantesis into stack
        elif char in close:
            if s.isEmpty():
                return False
            else:
                peak=s.pop()
                if open[peak]!=char: #if peak is ']' open[peak] gives opposite '[' from open dict as key value
                    return False
    return s.isEmpty()   #if stack is empty returns true value

print(valid_paranthesis("[{(a+b))-(a-b)}]"))