**Stack** 
    A Stack is a linear data structure that follows the LIFO principle. This means the last element added ti the stack will be the very first one to be removed.

**Core Stack Opertations** 
    A stack has few fundamental operations, all of which run in **O(1)** constant time.

1. **Push** :- Adds an element to te top of the stack
2. **POP** :- Remove or return the top element from the stack. If the stack is empty tis cause an underflow situation.
3. **PEEK** :- Return the top element without removing that.
4. **isEmpty** :- Checks if the stack as no element.
5. **isFull** :- Checks if the stack has reached its max memory capacity (relevant for fixed size array)

**Implementation of stack** 
1. **Using array** :- When we need a fixed memory size and fast access time.
2. **Using LL** :- When we need a dyanamic memory size.

**Array based Stack**
    **Rules**
1. **Initialization** :- An array of size capacity is allocated and top =-1
2. **Push Operation** :- Increments top by 1 and places te new element at array[top]. If top == capacity - 1, te stack throws a stack overflow error.
3. **POP Operation** :- Retrives te element at array[top] and decrements top by 1. If top == -1 the stack throws a stack underflow error.
