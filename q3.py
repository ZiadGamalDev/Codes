class StudentNode:
    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_student(self, student_id, name, age, course):
        new_node = StudentNode(student_id, name, age, course)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def remove_student(self, student_id):
        current = self.head
        while current:
            if current.student_id == student_id:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                return
            current = current.next

    def display_students_forward(self):
        current = self.head
        while current:
            print(f"ID: {current.student_id}, Name: {current.name}, Age: {current.age}, Course: {current.course}")
            current = current.next

    def display_students_backward(self):
        current = self.tail
        while current:
            print(f"ID: {current.student_id}, Name: {current.name}, Age: {current.age}, Course: {current.course}")
            current = current.prev

# Example usage
dll = DoublyLinkedList()
dll.add_student(1, 'John Doe', 20, 'Computer Science')
dll.add_student(2, 'Jane Doe', 22, 'Mathematics')
dll.display_students_forward()
dll.display_students_backward()
dll.remove_student(1)
dll.display_students_forward()
