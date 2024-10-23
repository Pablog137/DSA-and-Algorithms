# Path to Learning Common Data Structures and Algorithms
This repo provides resources to learn everything from Big O Notation to common data structures and popular algorithms, along with real-world exercises that demonstrate their use.

## Table of contents
- [Big O Notation](#big-o-notation)
- [Pointers and references](#pointers-and-references)
- [LinkedList](#linked-list)
- [Doubly Linked list](#doubly-linked-list)
- [Stack](#stack)
- [Queue](#queue)
- [Trees](#trees)
- [Hash Tables](#hash-tables)
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

## Trees

**A tree data structure is a hierarchical structure that is used to represent and organize data in a way that is easy to navigate and search**. It is a collection of nodes that are connected by edges and has a hierarchical relationship between the nodes.

The topmost node of the tree is called the root, and the nodes below it are called the child nodes. Each node can have multiple child nodes, and these child nodes can also have their own child nodes, forming a recursive structure.

![tree_data_structure](https://github.com/user-attachments/assets/95ae3834-7fc6-4add-ba97-c91cb1340d0a)

### **Terminologies in Tree data structure**

- **Parent node** : The node which is a predecessor of a node is called the parent node of that node. (B) is the parent node of (D,E)
- **Child Node**: The node which is the immediate successor of a node is called the child node of that node. Examples: (D,E) are the child nodes of (B)
- **Root Node**: A non-empty tree must contain exactly one root node. (A) is the root node of the tree.
- **Leaf Node of External Node**: The nodes which do not have any child nodes are called leaf nodes (I,J,K,F,G,H) are the leaf nodes of the tree.
- **Sibling**: Children of the same parent node are called siblings. (D,E) are called siblings.

### Types of Tree Data Structure

- **Binary tree** : In a binary tree, each node can have a maximum of two children linked to it.
- **Ternary tree**: A Ternary tree is a tree data structure in which each node has at most three child nodes, usually distinguished as “left”, “mid” and “right”.

### Applications of Tree Data Structure

- **File System** : This allows for efficient navigation and organization of files
- **Database Indexing** : B-trees and other tree structures are used in database indexing to efficiently search for and retrieve data.

### Basic Operations of Tree Data Structure

- **Create** : Create a tree in the data structure
- **Insert** : Inserts data in a tree
- **Search** : Searches specific data in a tree to check whether it is present or not
- **Transversal**

### Binary Search Tree

Each node in a **Binary Search Tree** has at most two children, a **left** child and a **right** child, with the **left** child containing values less than the parent node and the **right** child containing values greater than the parent node. This hierarchical structure allows for efficient **searching**, **insertion**, and **deletion** operations on the data stored in the tree.

![bst-21](https://github.com/user-attachments/assets/819cb1b3-69aa-413f-a9ce-3a9a0fb9699e)

**Binary Search Tree Big O**

- **Search :**
    - **Best case (Balanced BST):** O(log n)
    - **Worst case (Unbalanced BST):** O(n)
- **Insertion**:
    - **Best case (Balanced BST):** O(log n)
    - **Worst case (Unbalanced BST):** O(n)
- **Deletion:**
    - **Best case (Balanced BST):** O(log n)
    - **Worst case (Unbalanced BST):** O(n)

> **Worst case**
> 
> 
> In the absolute worst case, a binary tree with `N` elements would be like a linked list.
> 
> Hence, there would be `N` levels, and a search would take `N` traversals.
> 
> ```
>       ~ Root ~
>                                       ____
>                                      | 42 |
>                                      |____|
>                                     /      \
>                                ____/        \
>                               | 13 |         X
>                               |____|
>                              /      \
>                         ____/        \
>                        | 11 |         X
>                        |____|
>                       /      \
>                      /        \
>                   ...          X
> ```
>



## Hash Tables

A hash table (or hash map) is a data structure that allows for fast data retrieval. It maps keys to values using a hash function, which transforms the key into an index in an array where the value is stored. Here's how it works:

- **Keys**: These are unique identifiers (like a person's name).
- **Hash Function**: This takes a key and converts it into a numerical value (an index in the array).
- **Values**: These are the pieces of data associated with the keys.

![ComponentsofHashing](https://github.com/user-attachments/assets/5066c0a4-dd2f-4e9b-9fff-06e4639c3c21)

***A hash table is conceptually the same as dictionaries in C#, Java and in other languages.***

### How does a hash table work ?

1. **Hash function**
    
    The first step in a hash table is the use of a hash function. It takes a key (which could be any data type) and converts it into an integer, which is called the hash code. 
    
    The hash code is then used to determine where to store or find the associated value in an underlying array.
    
    Example: Let's say the key is `"apple"`. The hash function might turn `"apple"` into the number`3`.
    
2. **Indexing**
    
    After the hash function generates a hash code, the next step is to map the hash code to an index in the array.
    
    Example: If the array size is 10, you take the hash code `3` and compute `3 % 10`, which results in `3`. This means that the value associated with `"apple"` will be stored at index 3 in the array.
    
3. **Storing the value**
    
    The value associated with the key is stored in the array at the computed index.
    
    Example: Let's say we are storing the value `"fruit"` for the key `"apple"`. After the hash function returns `3`, the value `"fruit"` gets stored in the array at index 3
    
4. **Handling collisions**
    
    Sometimes, two keys will produce the same hash code or index, which leads to a collision. This can happen because multiple keys might map to the same index. To handle this, hash tables use various techniques:
    
    - **Chaining**: Each index in the array holds a linked list (or another structure like a list) of key-value pairs. If multiple keys map to the same index, they are added to this list. During lookup, the correct key is found by traversing this list.
        
        Example: If `"apple"` and `"grape"` both map to index 3, a list at index 3 will hold both key-value pairs, and during a lookup, the list is searched for the correct key.
        
    - **Open Addressing**: When a collision occurs, the hash table searches for the next available spot in the array using a technique like linear probing (checking the next index) or double hashing (using a secondary hash function to find a new index).


## Bibliography

https://www.geeksforgeeks.org/

