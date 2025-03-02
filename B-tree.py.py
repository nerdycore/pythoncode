class BTreeNode:
    def __init__(self, t, is_leaf=True):
        self.t = t
        self.keys = []
        self.children = []
        self.is_leaf = is_leaf

    def insert_non_full(self, key):
        i = len(self.keys) - 1
        if self.is_leaf:
            while i >= 0 and key < self.keys[i]:
                i -= 1
            self.keys.insert(i + 1, key)
        else:
            while i >= 0 and key < self.keys[i]:
                i -= 1
            i += 1
            if len(self.children[i].keys) == 2 * self.t - 1:
                self.split_child(i)
                if key > self.keys[i]:
                    i += 1
            self.children[i].insert_non_full(key)

    def split_child(self, i):
        t = self.t
        y = self.children[i]
        z = BTreeNode(t, is_leaf=y.is_leaf)
        z.keys = y.keys[t:]
        y.keys = y.keys[:t - 1]
        if not y.is_leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]
        self.children.insert(i + 1, z)
        self.keys.insert(i, y.keys.pop())

    def traverse(self):
        for i in range(len(self.keys)):
            if not self.is_leaf:
                self.children[i].traverse()
            print(self.keys[i], end=" ")
        if not self.is_leaf:
            self.children[-1].traverse()


class BTree:
    def __init__(self, t):
        self.t = t
        self.root = BTreeNode(t)

    def insert(self, key):
        root = self.root
        if len(root.keys) == 2 * self.t - 1:
            new_root = BTreeNode(self.t, is_leaf=False)
            new_root.children.append(self.root)
            new_root.split_child(0)
            self.root = new_root
            new_root.insert_non_full(key)
        else:
            root.insert_non_full(key)

    def display(self):
        if self.root is not None:
            self.root.traverse()


def main():
    t = int(input("Enter the minimum degree (t) of the B-tree: "))
    b_tree = BTree(t)
    print("\nEnter the numbers to insert into the B-tree. Type 'done' when finished.")
    while True:
        user_input = input("Enter a number: ")
        if user_input.lower() == 'done':
            break
        try:
            num = int(user_input)
            b_tree.insert(num)
            print("Inserted:", num)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    print("\nThe keys in the B-tree are:")
    b_tree.display()


main()
