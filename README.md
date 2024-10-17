# Path to Learning Common Data Structures and Algorithms
This repo provides resources to learn everything from Big O Notation to common data structures and popular algorithms, along with real-world exercises that demonstrate their use.

## Table of contents
- [Big O Notation](#big-o-notation)
- [Pointers and references](#pointers-and-references)
- [LinkedList](#linked-list)
- [Doubly Linked list](#doubly-linked-list)
- [Stack](#stack)
- [Queue](#queue)
- [Bibliography](#bibliography)

<br>


## Big O Notation

Big O notation is a powerful tool used to describe the time complexity or space complexity of algorithms. It provides a standardized way to compare the efficiency of different algorithms in terms of their worst-case scenario/performance.

Big O is a way to express the upper bound of an algorithm’s time complexity, since it analyses the **worst case** situation of an algorithm.

It’s denoted as **O(f(n))**, where **f(n)** is a function that represents the number of operations (steps) that an algorithm performs to solve a problem of size **n**.

### Common Big-O notations:

- **Linear Time Complexity : Big O(n) Complexity**

Linear time complexity means that the running time of an algorithm grows linearly with the size of the input.

```python
def print_items(n):
    for i in range(n):
        print(i)
```

It does not matter if we have 2n operations, it’s still O(n). As long as it uses the same value

  

```python
def print_items(n):
    for i in range(n):
        print(i)

    for i in range(n):
        print(i)
```

However, if we have two different inputs, we can't say that the function is O(n) or O(m). We have to say that it is O(n + m) or O(a + b). We can't simplify it.

```python

def print_items(n, m):
    for i in range(n):
        print(i)

    for i in range(m):
        print(i)
```

- **Constant Time Complexity : Big O(1) Complexity**

It doesn’t matter how big n is, it will always be 1 operation. It’s the most efficient algorithm.

```python
def print_items(n):
    print(n)
```

- **Quadratic Time Complexity: Big O(n²) Complexity**

Quadratic time complexity means the running time of an algorithm is proportional to the square of the input size.

```python
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
```

If we have a O(n² + n) it will still remain like O(n²). In this equation n² is the most important, n is insignificant in comparison.

```python
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

    for i in range(n):
        print(i)
```

- **Logarithmic Time Complexity: Big O(log n) Complexity**

Logarithmic time complexity means that the running time of an algorithm is proportional to the logarithm of the input size.

For example, binary search. If we have a list of 16 elements, we need 4 operations to find the element (**log₂(16) = 4**).

*How many times do we need to divide 16 by 2 to get 1? 4 times.*

**Example :** 

log₂1073741824 = 31
****O(log n) is very efficient. We would need 31 operations to find an element in a list of 10,737,418,24 elements.

```python
int binarySearch(int arr[], int l, int r, int x)
{
    if (r >= l) {
        int mid = l + (r - l) / 2;
        if (arr[mid] == x)
            return mid;
        if (arr[mid] > x)
            return binarySearch(arr, l, mid - 1, x);
        return binarySearch(arr, mid + 1, r, x);
    }
    return -1;
}
```

- **Cubic Time Complexity: Big O(n3) Complexity**

Cubic time complexity means that the running time of an algorithm is proportional to the cube of the input size.

```python
def print_items(n):
    for i in range(n):
        for j in range(n):
	        for p in range(n):
            print(i, j, p)
```



## Pointers and references

In Python, variables are essentially references (or pointers) to objects in memory. 

In Python, everything is an object. 

```python
>>> isinstance(1, object)
True
>>> isinstance(list(), object)
True
>>> isinstance(True, object)
True
>>> def foo():
...     pass
...
>>> isinstance(foo, object)
True
```

Each object contains at least three pieces of data: 

- Reference count
- Type
- Value

Not all objects are the same though. There is one other important distinction you’ll need to understand : inmutable vs mutable objects.

### **Immutable vs Mutable Objects**

1. **Immutable objects** can’t be changed
2. **Mutable objects** can be changed

| **Type** | **Inmutable**? |
| --- | --- |
| int | Yes |
| float | Yes |
| bool | Yes |
| complex | Yes |
| tuple | Yes |
| str | Yes |
| list | No |
| set | No |
| dict | No |

### Mutable objects

**To prove than a primitive type is inmutable we can write some Python code :**

```python

num1 = 10
print("num1 points to", id(num1))
num1+=1
print("num1 points to", id(num1))

....
num1 points to 140714042385608
num1 points to 140714042385640
```

Even though the above code appears to modify the value of `x`, **you’re getting a *new* object as a response.**

Same with strings :

```python
str1 = "Hello"
print("str1 points to", id(str1))
str1+=" World"
print("str1 points to", id(str1))

....
str1 points to 1557739449696
str1 points to 1557739535664
```

When we assign **num2 = num1 it doesn’t copy the value, it creates a reference to num1**. However, when you change num2, python creates a new integer object at a different memory location, and now num2 points to the new object. The previous value is left without a reference so it’s then removed by the garbage collector.

```python
num1 = 11
num2 = num1

print("num1 points to", id(num1))
print("num2 points to", id(num2))

--- 
num1 points to 140714017809640
num2 points to 140714017809640

# If we change num2, it will point to a different memory address.
num2 = 22

print("num1 points to", id(num1))
print("num2 points to", id(num2))

---
num1 points to 140714017809640
num2 points to 140714017809992
```

- When you do `a = "hello"`, a string is created in memory with the value `"hello"`, and `a` points to that memory address.
- With `b = a`, both variables (`a` and `b`) are pointing to the same object in memory.
- When you reassign `a = "world"`, a new string `"world"` is created in a different memory address, and `a` now points to that new string. However, `b` continues to point to `"hello"`.

```python
a = "hello"
b = a
a = "world"
print(b)  # Output: "hello"
```

### **In contrast there are some mutable objects, like *list* :**

```python
my_list = [1, 2, 3]
print("my_list points to", id(my_list))
my_list.append(4)
print("my_list points to", id(my_list))

....
my_list points to 1871348213440
my_list points to 1871348213440
```

**Dictionaries** (and other complex data structures like lists and sets) are **mutable**. This means you can change their contents without changing the memory address they are stored at.

```python
dict1 = {"name": "John"}
dict2 = dict1

print("dict1 points to", id(dict1))  # Points to some memory address A
print("dict2 points to", id(dict2))  # Points to the same memory address A

dict2["name"] = "Jane"

print("dict1 points to", id(dict1))  # Still points to memory address A
print("dict2 points to", id(dict2))  # Still points to memory address A

```



## Linked List

A linked list is a linear data structure, in which elements are not stored at a contiguous location, rather they are linked using pointers. Linked List forms a series of connected nodes, where each node stores the data and the address of the next node.

![image](https://github.com/user-attachments/assets/96798c0d-0a11-43af-add9-f21a2a0a0290)

A node in a linked list typically consists of two components:

- **Data** : it holds the actual value or data associated with the node
- **Pointer or reference** : It stores the memory address (reference) on the next node in the sequence.

**Head and Tail** : The linked list is accessed through the head node, which points to the first node in the list. The last node in the list points to NULL or nullity, indicating the end of the list. This node is known as the tail node. 

### When should we use a linked list?

The main cases where we prefer linked list over other data structures is due to ease of insertion and deletion in linked list. Without a linked list, if we want to insert or delete a value the list will have to reorder itself and move the require elements so it can be pretty expensive.


## Doubly Linked List

A doubly linked list is a data structure than consist of a set of nodes, each of which contains a data element and two links pointing to the next and previous node in the sequence. This allows for **more efficient operations** such as **transversals**, **insertions** and **deletions** because it can be done in both directions.

![image](https://github.com/user-attachments/assets/62257293-c26b-4da9-8b3b-1f4a9adabade)


A doubly linked list is represented using nodes that have three fields:

1. Data
2. A pointer to the next node
3. A pointer to the previous node

![image](https://github.com/user-attachments/assets/ed919dc8-7d2c-41b5-8fb2-1e58c712c0f5)


## Stack

A stack i a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-in/Last-Out (FILO) manner. In stack, a new element is added at one end and an element is removed from the end only. The insert and delete operations are often called push a pop.

<img width="407" alt="stack" src="https://github.com/user-attachments/assets/9312acfe-ede8-48bf-a9b1-4746baab1f47">

**Example** : In web browsers, when you navigate from one webpage to another, the previously visited pages are stored in a stack. Each time a new page is visited, it’s pushed onto the stack. If the “Back” button is pressed, then the current page is popped from the stack, revealing the last page that was visited.


## Queue

Like a stack, the queue is a linear data structure that stores items in First In First Out (FIFO) manner. With a queue, the least recently added item is removed first. A good example of a queue is any queue of consumers for a resource where the consumer that came first is served first.

<img width="946" alt="queue" src="https://github.com/user-attachments/assets/34633776-8a0e-4f86-a970-83b627559b89">

Operations associated with queue are :

- **Enqueue**: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition.
- **Dequeue**: Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty, then it is said to be an Underflow condition.
- **Front:** Get the front item from queue.
- **Rear:** Get the last item from queue.

<br>

## Bibliography

https://www.geeksforgeeks.org/

