# Node class structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        currentNode = self.head

        while currentNode:
            print(currentNode.data)
            currentNode = currentNode.next

    def push(self, new_data):  # O(1) ST
        new_node = Node(new_data)  # Creating new node
        new_node.next = self.head  # Pointing new node to the next
        self.head = new_node  # Move the head to the new node

    def insert_after_node(self, prev_node, new_data):  # O(1) ST
        if prev_node is None:
            print("There is no previous node")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insert_after_value(self, target_value, new_data):  # O(n) Time & O(1) Space
        currentNode = self.head

        while currentNode:
            if currentNode.data == target_value:
                new_node = Node(new_data)
                new_node.next = currentNode.next
                currentNode.next = new_node
                print("New node has been inserted")
                break
            currentNode = currentNode.next
            if currentNode == None:
                print("The target value is not available in the Linked list")
                return

    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node

        lastNode = self.head
        while lastNode.next:
            # Traversing through the linked list until we find a node that's next pointer is Null
            lastNode = lastNode.next

        lastNode.next = new_node

    def delete(self, target_value):
        temp = self.head

        if temp is not None:
            if temp.data == target_value:
                self.head = temp.next
                temp = None
                return
            else:
                while temp.next != None:
                    if temp.data == target_value:
                        break

                    prev = temp
                    temp = temp.next

                if temp == None:
                    print("Node not found")
                    return

                prev.next = temp.next
                return


# Initiating with the empty list
first = LinkedList()

# Creating the head node
first.head = Node(1)

# Creating three other nodes
second = Node(2)
third = Node(3)
four = Node(4)

# Linking them with each other
first.head.next = second
second.next = third
third.next = four

print("Printing linked list for the first time:")
first.printList()

first.push(12)

print("\nLinked list after adding 12 in the beginning")
first.printList()

first.insert_after_node(second, 22)

print("\nPrinting Linked list after adding 22 after second node(2)")
first.printList()

first.insert_after_value(24, 33)

print("\nAfter adding new node after the value 22")
first.printList()

first.append(78)

print("\nAfter appending 78 to the linked list")
first.printList()

first.delete(1)
print("\nAfter deleting 12")
first.printList()
