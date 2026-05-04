class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        if not self.head:
            print("List is empty.")
            return

        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        if not self.head:
            raise IndexError("Cannot delete from an empty list.")

        if n <= 0:
            raise ValueError("Index should be 1 or greater.")

        # Deleting the head
        if n == 1:
            deleted_data = self.head.data
            self.head = self.head.next
            print(f"Deleted node at position {n} with value '{deleted_data}'")
            return

        current = self.head
        count = 1

        # Traverse to the (n-1)th node
        while current and count < n - 1:
            current = current.next
            count += 1

        # If the (n-1)th node is None or the nth node doesn't exist-
        if not current or not current.next:
            raise IndexError(f"Index {n} is out of range.")

        deleted_data = current.next.data
        current.next = current.next.next
        print(f"Deleted node at position {n} with value '{deleted_data}'")


if __name__ == "__main__":
    ll = LinkedList()

    while True:
        print("\nChoose an operation:")
        print("1. Add a node")
        print("2. Print the list")
        print("3. Delete the nth node")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            try:
                data = int(input("Enter the value to add: "))
                ll.add_node(data)
                print(f"Added {data} to the list.")
            except ValueError:
                print("Please enter a valid integer.")

        elif choice == '2':
            print("Current Linked List:")
            ll.print_list()

        elif choice == '3':
            try:
                n = int(input("Enter the position (1-based index) to delete: "))
                ll.delete_nth_node(n)
            except ValueError:
                print("Please enter a valid integer for position.")
            except Exception as e:
                print("Error:", e)

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")



#Sample Testing

if __name__ == "__main__":
    # Creating a linked list
    ll = LinkedList()

    print("\n======= Sample Testing Example with a list ========\n")
    # Adding nodes now
    ll.add_node(10)
    ll.add_node(20)
    ll.add_node(30)
    ll.add_node(40)

    print("Original List:")
    ll.print_list()

    print("\nDeleting 3rd node...")
    ll.delete_nth_node(3)
    ll.print_list()

    print("\nDeleting 1st node...")
    ll.delete_nth_node(1)
    ll.print_list()

    print("\nTrying to delete node at index 10 (out of range):")
    try:
        ll.delete_nth_node(10)
    except Exception as e:
        print("Error:", e)

    print("\nTrying to delete from empty list:")
    empty_list = LinkedList()
    try:
        empty_list.delete_nth_node(1)
    except Exception as e:
        print("Error:", e)

