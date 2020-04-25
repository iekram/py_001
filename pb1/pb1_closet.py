class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_tail(self, data) -> None:
        if self.head is None:
            self.insert_head(data)
        else:
            tmp = self.head
            while tmp.next:
                tmp = tmp.next
            tmp.next = Node(data)

    def insert_head(self, data) -> None:
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
        self.head = new_node

    def print_list(self):
        tmp = self.head
        while tmp:
            print(tmp.data)
            tmp = tmp.next

    def delete_head(self):
        tmp = self.head
        if self.head:
            self.head = self.head.next
            tmp.next = None
        return tmp

    def delete_tail(self):
        tmp = self.head
        if self.head:
            if self.head.next is None:
                self.head = None
            else:
                while tmp.next.next:
                    tmp = tmp.next
                tmp.next, tmp = None, tmp.next
        return tmp

    def is_empty(self) -> bool:
        return self.head is None

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def __repr__(self):
        current = self.head
        string_repr = ""
        while current:
            string_repr += f"{current} --> "
            current = current.next
        return string_repr + "END"

    def __getitem__(self, item):
        current = self.head
        if current is None:
            raise IndexError("The Linked List is empty")
        for _ in range(item):
            if current.next is None:
                raise IndexError("Index is out of range.")
            current = current.next
        return current

    def __setitem__(self, index, data):
        current = self.head
        if current is None:
            raise IndexError("The Linked List is empty")
        for i in range(index):
            if current.next is None:
                raise IndexError("Index out of range.")
            current = current.next
        current.data = data


def main():
    a = LinkedList()
    a.insert_head(input("Insert 1st at head: ").strip())
    a.insert_head(input("Insert 2nd at head: ").strip())
    a.insert_head(input("Insert 3rd at head: ").strip())
    print("\nPrint list:")
    a.print_list()
    a.insert_tail(input("\nInserting 1st at tail ").strip())
    a.insert_tail(input("Inserting 2nd at tail ").strip())
    print("\nPrint list:")
    a.print_list()
    print("\nDelete head")
    a.delete_head()
    print("Delete tail")
    a.delete_tail()
    print("\nPrint list:")
    a.print_list()
    print("\nReverse linked list")
    a.reverse()
    print("\nPrint list:")
    a.print_list()
    print("\nString representation of linked list:")
    print(a)
    print("\nReading/changing Node data using indexing:")
    print(f"Element at Position 1: {a[1]}")
    a[1] = input("Enter New Value: ").strip()
    print("New list:")
    print(a)


if __name__ == '__main__':
    main()

print('test')