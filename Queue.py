class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        return f"{item} added to the queue."

    def dequeue(self):
        if not self.is_empty():
            removed = self.queue.pop(0)
            return f"{removed} removed from the queue."
        return "Queue is empty."

    def peek(self):
        if not self.is_empty():
            return f"Front of the queue: {self.queue[0]}"
        return "Queue is empty."

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        return f"Queue: {self.queue}" if not self.is_empty() else "Queue is empty."

queue = Queue()

print("Queue Operations:")
print("1. Enqueue (Add item to queue)")
print("2. Dequeue (Remove item from queue)")
print("3. Peek (View front item)")
print("4. Display (View all items)")
print("5. Exit")

while True:
    try:
        choice = int(input("Enter your choice (1-5): ").strip())

        if choice == 1:
            num_items = int(input("How many items do you want to enqueue? ").strip())
            for _ in range(num_items):
                item = input("Enter the item to enqueue: ").strip()
                print(queue.enqueue(item))
        elif choice == 2:
            print(queue.dequeue())
        elif choice == 3:
            print(queue.peek())
        elif choice == 4:
            print(queue.display())
        elif choice == 5:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 5.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")
