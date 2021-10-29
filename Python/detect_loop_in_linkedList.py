# Python Demonstration to detect loop/circle in linked list in two different approches:
# 1. Two pointer approch
# 2. Hashing approch
# 3. Normal approch by marking visited nodes and checking if a cycle exists.


# Two pointer approch
def detectLoop_TwoPointer(head):
    slow = head  # initializing slow pointer to point to head of the linked list
    fast = (
        head.next
    )  # initializing fast pointer to point next node to head node of the linked list
    flag = 0  # initializing flag to 0
    while (
        slow and fast and fast.next
    ):  # checks if slow pointer, fast pointer and next to fast pointer are not pointing to None
        slow = slow.next  # setting slow pointer to point to it's next node
        fast = fast.next.next  # setting fast pointer to point to it's next to next node
        if slow == fast:
            flag = (
                1  # set flag to 1 if slow and fast pointers points to the same node and
            )
            break  # break from the loop
    if flag:
        return True
    return False


# Hashing approch
def detectLoop_Hashing(head):
    hashmap = set()  # Initializing the hashmap
    temp = head  # assign head node to temp
    while temp:  # if temp node is not None, execute the following code

        if (
            temp in hashmap
        ):  # If we have already has this node in hashmap it means their is a cycle (Because you we encountering the node second time).
            return True

        hashmap.add(
            temp
        )  # If we are seeing the node for the first time, insert it in hashmap
        temp = temp.next  # changing temp to temp.next

    return False


# Marking visited nodes without modifying the linked list data structure.
def detectLoop(head):
    temp = ""  # initialize temp to be empty/null
    while (
        head != None
    ):  # checking the condition, if head is None, if it is isn't None... enters the while loop.

        # This condition is for the case, when there is no loop
        if head.next == None:
            return False

        if (
            head.next == temp
        ):  # Check if next node is pointing to empty/null (since temp is empty)
            return True

        next_pointer = head.next  # Store the pointer to the next node
        head.next = temp  # Make next pointer to temp (indirectly, make the current node's next pointer to None)
        head = next_pointer  # Get to the next node in the linked list

    return False


# Driver code
# Creating Node class
class Node:
    # Constructor
    def __init__(self, data):
        self.data = data
        self.next = None


# Creating Linked List class
class LinkedList:
    # Constructor
    def __init__(self):
        self.head = None

    # insert method creates a new node with given value and appends it at the end of the linked list
    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node


# Found function
def Found(found):
    if found:
        print("Through Two-Pointer approch: Cycle exists in linked list")
    else:
        print("Through Two-Pointer approch: No cycle exists in lisked list")


# Creating a linked list which doesn't contain cycle
linked_list = LinkedList()
linked_list.insert(20)
linked_list.insert(4)
linked_list.insert(15)
linked_list.insert(10)

## Checking without creating the cycle
print("**-------------------Without Cycle in linked list-------------------***")
Found(
    detectLoop_TwoPointer(linked_list.head)
)  # check if cycle exists through detectLoop_TwoPointer function
Found(
    detectLoop_Hashing(linked_list.head)
)  # check if cycle exists through detectLoop_Hashing function
Found(detectLoop(linked_list.head))  # check if cycle exists through detectLoop function

# Output:
"""
"***-------------------Without Cycle in linked list-------------------***"
Through Two-Pointer approch: No cycle exists in lisked list
Through Hashing approch: No cycle exists in lisked list
Through marking visited nodes approch: No cycle exists in lisked list
"""


# Creating a linked list which contains cycle
linked_list = LinkedList()
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(4)
linked_list.insert(5)

# Creating a cycle in linked list
linked_list.head.next.next.next.next.next = (
    linked_list.head.next.next
)  # Node which contains the value '5' is pointing to the node containing the value '3'

# Checking after creating a cycle
print("\n***---------------------With Cycle in linked list---------------------***")
Found(
    detectLoop_TwoPointer(linked_list.head)
)  # check if cycle exists through detectLoop_TwoPointer function
Found(
    detectLoop_Hashing(linked_list.head)
)  # check if cycle exists through detectLoop_Hashing function
Found(detectLoop(linked_list.head))  # check if cycle exists through detectLoop function

# Output:
"""
***---------------------With Cycle in linked list---------------------***
Through Two-Pointer approch: Cycle exists in linked list
Through Hashing approch: Cycle exists in linked list
Through marking visited nodes approch: Cycle exists in linked list
"""
