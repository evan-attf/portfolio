"""
-------------------------------------------------------
Stack utilities
-------------------------------------------------------
Author:  Evan Attfield
ID:      180817010
Email:   attf7010@mylaurier.ca
__updated__ = "Jan 22, 2019"
-------------------------------------------------------
"""
from Stack_array import Stack
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue
from List_array import List

def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack, 
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while source != []:
        temp = source.pop()
        stack.push(temp)
    
    return 

def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while stack.is_empty() == False:
        temp = stack.pop()
        target.insert(0, temp) #adds temp to the beginning, while append adds temp to the end
    return 
    
def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and 
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    stack = Stack()
    dummy = []
    if stack.is_empty() == True:
        print('Stack is empty.')
    
    array_to_stack(stack, source)
    print('Converting source into a stack...')
    
    if stack.is_empty() == False:
        print('source has been transferred into stack!')
    
    print('\nPopping stack...')
    while stack.is_empty() == False:
        temp = stack.pop()
        print(temp)
        dummy.append(temp)
        
    print('\nstack is empty. Pushing values back into stack...')
    while dummy != []:
        temp = dummy.pop()
        print(temp)
        stack.push(temp)
        
    print('\nPushing complete! Peeking...')
    print(stack.peek())
    
    return
    
def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue, 
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    temp = None
    
    while source != []:
        temp = source.pop(0)
        queue.insert(temp)

    return
def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    temp = None
    
    while queue.is_empty() == False:
        temp = queue.remove()
        target.append(temp)

    return

def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq, 
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    temp = None
    
    while source != []:
        temp = source.pop(0)
        pq.insert(temp)

    return

def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    temp = None
    
    while pq.is_empty() == False:
        temp = pq.remove()
        target.append(temp)
    
    return

def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        the methods of Queue are tested for both empty and 
        non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    -------------------------------------------------------
    """
    queue = Queue()
    dummy = []
    if queue.is_empty() == True:
        print('Queue is empty.')
    
    array_to_queue(queue, a)
    print('Converting a into a queue...')
    
    if queue.is_empty() == False:
        print('a has been transferred into queue!')
    
    print('\nRemoving queue...')
    while queue.is_empty() == False:
        temp = queue.remove()
        print(temp)
        dummy.append(temp)
        
    print('\nqueue is empty. Inserting values back into queue...')
    while dummy != []:
        temp = dummy.pop()
        print(temp)
        queue.insert(temp)
        
    print('\nPushing complete! Peeking...')
    print(queue.peek())
    
    print('\nqueue is {} objects long!'.format(len(queue)))

    return

def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Use: pq_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        the methods of Priority_Queue are tested for both empty and 
        non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    -------------------------------------------------------
    """
    pq = Priority_Queue()
    dummy = []
    if pq.is_empty() == True:
        print('pq is empty.')
    
    array_to_pq(pq, a)
    print('Converting a into a pq...')
    
    if pq.is_empty() == False:
        print('a has been transferred into pq!')
    
    print('\nRemoving pq...')
    while pq.is_empty() == False:
        temp = pq.remove()
        print(temp)
        dummy.append(temp)
        
    print('\pq is empty. Inserting values back into queue...')
    while dummy != []:
        temp = dummy.pop()
        print(temp)
        pq.insert(temp)
        
    print('\nPushing complete! Peeking...')
    print(pq.peek())
    
    print('\npq is {} objects long!'.format(len(pq)))

    return

def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist, 
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while source: #a list is considered True as long as it is not empty
        llist.append(source.pop(0))
        
    return

def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while llist.is_empty() == False:
        target.append(llist.pop(0))
    
    return

def list_test(a):
    """
    -------------------------------------------------------
    Tests list implementation.
    The methods of List are tested for both empty and 
    non-empty lists using the data in a:
    is_empty, insert, remove, append, index, __contains__,
    find, count, max, min, __getitem__, __setitem__
    Use: list_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()
    
    if lst.is_empty() == True:
        print('lst is empty.')
    
    array_to_list(lst, a)
    print('Converting a into a lst...')
    
    if lst.is_empty() == False:
        print('a has been transferred into lst!')
    
    print('The movie at index 0 is {}'.format(lst[0]))
    
    print('/nRemoving the movie at index 0...')
    temp = lst.remove(lst[0])
    print('Now the movie at index 0 is {}'.format(lst[0]))
    
    print('/nInserting the movie at index 1...')
    lst.insert(1, temp)
    print('Now the movie at index 1 is {}'.format(lst[1]))
    
    print('/nRemoving the movie at index 0...')
    temp = lst.remove(lst[0])
    
    print('/nAppending the movie...')
    lst.append(temp)
    
    print('Peeking...')
    print(lst.peek())
    
    print('/nThe index of the movie is {}'.format(lst.index(temp)))
    
    print('/n{} appears {} time(s)'.format(temp, lst.count(temp)))
    
    print('/nThe max is {}'. format(lst.max()))
    print('The min is {}'. format(lst.min()))
    
    print('/nThe movie is at index {}'.format(lst.find(temp)))
    
    

    return
