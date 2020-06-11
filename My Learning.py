#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Node:
    def __init__(self):
        self.__data=None
        self.__next=None
    def set_data(self,data):
        self.__data=data
    def get_data(self):
        return self.__data
    def set_next(self,next_node):
        self.__next=next_node
    def get_next(self):
        return self.__next
class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None
    def set_head(self,head):
        self.__head=head
    def get_head(self):
        return self.__head
    def set_tail(self,tail):
        self.__tail=tail
    def get_tail(self):
        return self.__tail
    def add(self,data):
        new_node=Node()
        new_node.set_data(data)
        if(self.__head==None):
            self.__head=self.__tail=new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail=new_node
    def display(self):
        temp=self.__head
        while(temp is not None):
            print(temp.get_data())
            temp=temp.get_next()
    def find_node(self,data):
        temp=self.__head
        while(temp is not None):
            if(temp.get_data()==data):
                return temp
            temp=temp.get_next()
        return None
    def insert(self,data,data_before):
        new_node=Node()
        new_node.set_data(data)
        if(data_before==None):
            new_node.set_next(self.__head)
            new_node=self.__head
            if(new_node.get_next()==None):
                self.__tail=new_node
        else:
            node_before=self.find_node(data_before)
            if(node_before is not None):
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if(new_node.get_next()==None):
                    self.__tail=new_node
            else:
                print(data_before,"is not found")
                
l1=LinkedList()
while(True):
    data=input("Enter the data to store in the linked list")
    l1.add(data)
    l1.display()
    command=input("Do you want to store another data[Y/N]")
    if(command.upper()=="Y"):
        pass
    else:
        print(l1)
        print("Your data saved sucessfully")
        break
l1.insert("star","Lucky")
l1.display()


# In[1]:


def merge_data(list1,list2):
    merged_data=""
    j=len(list2)-1
    for i in range(len(list1)):
        data1=data2=""
        if(list1[i]):
            data1=list1[i]
        if(list2[j]):
            data2=list2[j]
        merged_data=merged_data+data1+data2
        j-=1
        if(i<len(list1)-1):
            merged_data+=" "
    return merged_data
list1=["i","lo","y"]
list2=["ou","ve",None]
res=merge_data(list1,list2)
print(res)


# Assignment 12 dsa

# In[1]:


def rearrange_balls(self,color):
        
        if(color=="Red"):  
            balls_container=self.red_balls_container
        elif(color=="Green"):  
            balls_container=self.green_balls_container
        elif(color=="Blue"):  
            balls_container=self.blue_balls_container
        elif(color=="Yellow"):  
            balls_container=self.yellow_balls_container
        
        ball_on_top=balls_container.pop()
        balls_container.push(ball_on_top)
        if ball_on_top.get_name()=="B":
            temp_container=Queue(2)
            while not balls_container.is_empty():
                temp_container.enqueue(balls_container.pop())
            
            while not temp_container.is_empty():
                balls_container.push(temp_container.dequeue())
    
    
def display_ball_details(self,color):
        if(color=="Red"):  
            temp_container=self.red_balls_container
        elif(color=="Green"):  
            temp_container=self.green_balls_container
        elif(color=="Blue"):  
            temp_container=self.blue_balls_container
        elif(color=="Yellow"):  
            temp_container=self.yellow_balls_container
        if(temp_container.is_empty()):
            print("The stack is empty!!")
        else:
            temp_container.display()


# Assignment-13

# In[2]:


def change_smallest_value(number_stack):
    temp_queue=Queue(number_stack.get_max_size())
    result_stack=Stack(number_stack.get_max_size())
    smallest_number=number_stack.pop()
    temp_queue.enqueue(smallest_number)
    while(not number_stack.is_empty()):
        number=number_stack.pop()
        if(number<smallest_number):
            smallest_number=number
        temp_queue.enqueue(number)
        
    temp_stack=Stack(number_stack.get_max_size())
    while not temp_queue.is_empty():
        temp_number=temp_queue.dequeue()
        if smallest_number==temp_number:
            result_stack.push(temp_number)
        else:
            temp_stack.push(temp_number)
            
    while not temp_stack.is_empty():
        result_stack.push(temp_stack.pop())
    return result_stack  


# Assignment14

# In[3]:


def check_numbers(number_queue):
    solution_queue1=Queue(number_queue.get_max_size())
    
    while (not number_queue.is_empty()): 
        count=0
        num=number_queue.dequeue()
        for j in range(1,11):
            if(num%j==0):
                count+=1
            else:
                break
          
        if(count==10):
            solution_queue1.enqueue(num)
    solution_queue1.display()  
    
   
    return solution_queue1


# Assignment 15

# In[4]:


def elapsed_time(self,no_of_mins):
        self.__time_elapsed+=no_of_mins
        if(self.__time_needed<=self.__time_elapsed):
            return True
        else:
            return False
    
from Kripa Shetty Kudva to All Participants:
def elapsed_time(self,no_of_mins):
        if(self.__allocated_job.elapsed_time(no_of_mins)):
                dequeued_job=self.__allocated_job
                print(self.__name, "has completed", dequeued_job.get_name())
                self.__allocated_job=None
                return dequeued_job
        return None
from Kripa Shetty Kudva to All Participants:
def allocate_new_job(self,job):
            allocated=0
            for employee in self.__employees:
                if(employee.get_allocated_job()==None):
                    employee.set_allocated_job(job)
                    allocated=1
                    break
                    
            if(allocated==0):
                self.__pending_jobs.enqueue(job)
            
        
from Laxmi AB to All Participants:
mam i understand the questions, but during implementation i fail to do so :(
from Kripa Shetty Kudva to All Participants:
def elapsed_time(self,no_of_mins):       
            completed_jobs=[]
            for employee in self.__employees:
                emp_completed_job=employee.elapsed_time(no_of_mins)
                if(emp_completed_job!=None):
                    completed_jobs.append(emp_completed_job)
                    employee.set_allocated_job(self.__pending_jobs.dequeue())
                    print(employee.get_name(),"is allocated", employee.get_allocated_job().get_name())
                    
               
            if(len(completed_jobs)==0):
                return None 
            else: 
                return completed_jobs


# In[2]:


a=10
print(id(a))
b=a
print(id(b))


# In[7]:


class Node:
    def __init__(self):
        self.data=None
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def add(self,data):
        new_node=Node()
        new_node.data=data
        if(self.head==None):
            self.head=self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
    def display(self):
        temp=self.head
        while (temp is not None):
            print(temp.data)
            temp=temp.next
    def find_node(self,data):
        temp=self.head
        while (temp is not None):
            if(temp.data==data):
                return temp
            else:
                temp=temp.next
        return None
    def insert(self,data,data_before):
        new_node=Node()
        new_node.data=data
        if(data_before==None):
            new_node.next(self.head)
            self.head=new_node
            if(new_node.next==None):
                self.tail=new_node
        else:
            node_before=self.find_node(data_before)
            if(node_before is not None):
                new_node.next=node_before.next
                node_before.next=new_node
                if(new_node.next==None):
                    self.tail=new_node
                        
            else:
                print(data_before,"is not found in the limkedlist")
l1=LinkedList()
l1.add("Sugar")
l1.add("honey")
l1.display()
l1.insert("Sugar","sweet")
l1.display()


# In[ ]:


def find_next_small(num_list,first_index):
    small_index=first_index
    last_index=len(num_list)
    for index in range(first_index,last_index,1):
        if(small_index>index):
            small_index=index
    return small_index
def selection_sort(num_list):
    last_index=len(num_list)-1
    for indx in range(0,last_index,1):
        small_value_index=find_next_small(num_list,indx)
        if(small_value_index != index):
            swap(num_list)


# In[ ]:


def find_next_min(num_list,first_index):
    smallest_index=first_index
    last_index=len(num_list)-1
    for index in range(first_index,last_index,1):
        if(index<smallest_index):
            smallest_index=index
    return smallest_index
def swap_element(num_list,first_index,second_index):
    


# In[ ]:


def precedence(op):
    if op=="+" or "-":
        return 1
    elif op=="*" or "/":
        return 2
    else:
        return 0
def applyOp(val1,val2,op):
    if op=="+":return val1+val2
    elif op=="-":return val1-val2
    elif op=="*":return val1*val2
    elif op=="/":return val1/val2
def calculate(expression):
    numbers=[]
    ops=[]
    i=0
    length=len(expression)
    while(i<length):
        if(expression[i]==" "):
            i+=1
            continue
        elif(expression[i]=="("):
            ops.append(expression[i])
            i+=1
        elif(expression[i].isdigit()):
            num=0
            while(i<length and expression[i].isdigit()):
                num=num*10+intexpression[i]
            numbers.append(num)
        elif(expression[i]==")"):
            while len(ops)!=0 and ops[-1]!="(":
                val2=numbers.pop()
                val1=numbers.pop()
                op=ops.pop()
                value=applyOp(val1,val2,op)
                numbers.append(value)
            ops.pop()
        else:
            while len(ops)!=0 and precedence(ops[-1])>=precedence(expression[i]):
                val2=numbers.pop()
                val1=numbers.pop()
                op=ops.pop()
                value=applyOp(val1,val2,op)
                numbers.append(value)
            ops.append(expression[i])
        i+=1
        while (len(ops)!=0):
            val2=numbers.pop()
            val1=numbers.pop()
            op=ops.pop()
            value=applyOp(val1,val2,op)
            numbers.append(value)
        return numbers[-1]
if __name__=="__main__":
    res=calculate("3+(4*5)/6")
    print(res)


# In[1]:


from itertool import count
import time


# In[2]:


from itertools import count
import time


# In[3]:


type(count(10))


# In[5]:


x=count(10)
print(x)


# In[6]:


while True:
    print(next(x))
    time.sleep(1)


# In[7]:


print(next(10))


# Assignment-15

# In[4]:


def find_product(first,second,third):
    if(first!=7 and second!=7 and third!=7):
        product=first*second*third
        print(product)
    elif(first==7 and second!=7 and third!=7):
        product=second*third
        print(product)
    elif(second==7 and third!=7):
        product=third
        print(product)
    else:
        print("-1")
numbers=input("Enter the three numbers")
arr=numbers.split(",")
first_num=int(arr[0])
second_num=int(arr[1])
third_num=int(arr[2])
find_product(first_num,second_num,third_num)


# Assignment-16

# In[8]:


one_coin=int(input("Enter Available Rs. 1 coins "))
five_coin=int(input("Enter Available Rs. 5 notes "))
Amount=int(input("Enter the amount to be made "))
if(Amount>1*one_coin+5*five_coin):
    print("-1")
elif(Amount>5*five_coin):
    five_coin_needed=five_coin
    one_coin_needed=Amount-5*five_coin
    print("five coin needed ",five_coin_needed)
    print("one coin needed ",one_coin_needed)
else:
    five_coin_needed=Amount//5
    one_coin_needed=Amount%5
    print("five coin needed ",five_coin_needed)
    print("one coin needed ",one_coin_needed)


# Code With Harry Day-1

# In[3]:


print("Hello World", end=" ")
print("Welcome to python")


# In[7]:


num=10
print("The number is ",num)


# In[8]:


print("Hello World","Welcome to python")


# In[9]:


print("Hello World\nWelcome to python")


# In[10]:


print("\")


# In[11]:


print("\\")


# In[15]:


a=10
print(a)
print(id(a))
a=20
print(id(a))
print(a)


# In[19]:


print(10*str((45+19))


# In[20]:


a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
c=a+b
print("result is ",c)


# In[2]:


my_str="My name is Amrit Kumar Sahoo"
print(my_str[10:2:-2])


# In[3]:


print(my_str[::-1])


# In[4]:


print(my_str.capitalize())


# In[5]:


print(my_str.upper())


# In[6]:


print(my_str.lower())


# In[7]:


print(my_str.casefold())


# In[14]:


print(my_str.center(50,"o"))


# In[15]:


print(my_str)


# In[16]:


print(my_str.count("a"))


# In[17]:


string="L\tu\tc\tk\ty"
print(string)


# In[24]:


print(string.expandtabs(8))


# In[25]:


print(my_str.find("Amrit"))


# In[29]:


txt = "2if"

x = txt.isidentifier()

print(x)


# In[8]:


n=int(input("Enter the row size:"))
for i in range(1,n+1):
    for j in range(0,i):
        print("*",end="")
    print()


# In[10]:


n=int(input("Enter the row size:"))
for i in range(1,n+1):
    for j in range(0,(n-i)):
        print(" ",end="")
    for k in range(0,i):
        print("*",end="")
    print()


# In[12]:


n=int(input("Enter the row size:"))
for i in range(1,n+1):
    for j in range(0,(n+1-i)):
        print("*",end="")
    print()


# In[15]:


n=int(input("Enter the row size"))
for i in range(0,n):
    for j in range(0,i):
        print(" ",end="")
    for k in range(0,(n-i)):
        print("*",end="")
    print()


# In[16]:


n=int(input("Enter the row size:"))
for i in range(0,n):
    for j in range(0,(n-1-i)):
        print(" ",end="")
    for k in range(0,2*i+1):
        print("*",end="")
    print()


# Pascal Tringle

# In[27]:


n=int(input("Enter the no of rows: "))
a=[]
for i in range(n):
    a.append([])
    a[i].append(1)
    for j in range(1,i):
        a[i].append(a[i-1][j-1]+a[i-1][j])
    if(n!=0):
        a[i].append(1)
for i in range(n):
    print("   "*(n-i),end=" ",sep=" ")
    for j in range(0,i+1):
        print('{0:6}'.format(a[i][j]),end=" ",sep=" ")
    print()


# In[1]:


tup=(21,32,45,17)
print(tup)


# In[2]:


tup.append(43)
print(tup)


# In[3]:


print(tup[1])


# In[4]:


tup.index(45)


# In[5]:


tup=(12,13,12,17,19)
print(tup)


# In[6]:


tup.index(12)


# List in Python

# In[1]:


List_of_Strings=["cat","dog","elephant"]
print(List_of_Strings)


# In[2]:


List_of_Numbers=[5,6,10,18,10,4]
print(List_of_Numbers)


# In[4]:


List_of_Mix=["Hello",5,"a",7.9,3+4j]
print(List_of_Mix)


# In[5]:


List_of_List=[List_of_Strings,List_of_Numbers,List_of_Mix]
print(List_of_List)


# In[6]:


empty_list=[]
print(empty_list)


# In[11]:


List_of_Strings.extend(List_of_Numbers)
print(List_of_Numbers)
print(List_of_Strings)


# In[14]:


List1=[1,2,3,4,5]
List2=[6,7,8,9,0]
List1.extend(List2)
print(List1)


# In[1]:


list(range(10))


# In[2]:


range(10)


# In[ ]:




