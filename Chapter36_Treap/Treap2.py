import random


# A Treap Node
class TreapNode:
    def __init__(self, key):
        self.key = key
        self.priority = random.randint(0, 99)
        self.left = None
        self.right = None


# T1, T2 and T3 are subtrees of the tree rooted with y
# (on left side) or x (on right side)
#			 y							 x
#			 / \	 Right Rotation		 / \
#			 x T3 – – – – – – – >	 T1 y
#			 / \	 < - - - - - - -		 / \
#		 T1 T2	 Left Rotation		 T2 T3 */

# A utility function to right rotate subtree rooted with y
# See the diagram given above.

def rightRotate(y):
    x = y.left
    T2 = x.right

    # Perform rotation
    x.right = y
    y.left = T2

    # Return new root
    return x


def leftRotate(x):
    y = x.right
    T2 = y.left

    # Perform rotation
    y.left = x
    x.right = T2

    # Return new root
    return y


def insert(root, key):
    # If root is None, create a new node and return it
    if not root:
        return TreapNode(key)

    # If key is smaller than root
    if key <= root.key:
        # Insert in left subtree
        root.left = insert(root.left, key)

        # Fix Heap property if it is violated
        if root.left.priority > root.priority:
            root = rightRotate(root)
    else:
        # Insert in right subtree
        root.right = insert(root.right, key)

        # Fix Heap property if it is violated
        if root.right.priority > root.priority:
            root = leftRotate(root)
    return root


def deleteNode(root, key):
    if not root:
        return root

    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif key > root.key:
        root.right = deleteNode(root.right, key)
    else:
        # IF KEY IS AT ROOT

        # If left is None
        if not root.left:
            temp = root.right
            root = None
            return temp

        # If right is None
        elif not root.right:
            temp = root.left
            root = None
            return temp

        # If key is at root and both left and right are not None
        elif root.left.priority < root.right.priority:
            root = leftRotate(root)
            root.left = deleteNode(root.left, key)
        else:
            root = rightRotate(root)
            root.right = deleteNode(root.right, key)

    return root


# A utility function to search a given key in a given BST
def search(root, key):
    # Base Cases: root is None or key is present at root
    if not root or root.key == key:
        return root

    # Key is greater than root's key
    if root.key < key:
        return search(root.right, key)

    # Key is smaller than root's key
    return search(root.left, key)


# A utility function to print tree
def inorder(root):
    if root:
        inorder(root.left)
        print("key:", root.key, "| priority:", root.priority, end="")
        if root.left:
            print(" | left child:", root.left.key, end="")
        if root.right:
            print(" | right child:", root.right.key, end="")
        print()
        inorder(root.right)


# Driver Program to test above functions
if __name__ == '__main__':
    random.seed(0)

    root = None
    root = insert(root, 50)
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 70)
    root = insert(root, 60)
    root = insert(root, 80)

    print("Inorder traversal of the given tree")
    inorder(root)

    print("\nDelete 20")
    root = deleteNode(root, 20)
    print("Inorder traversal of the modified tree")
    inorder(root)

    print("\nDelete 30")
    root = deleteNode(root, 30)
    print("Inorder traversal of the modified tree")
    inorder(root)

    print("\nDelete 50")
    root = deleteNode(root, 50)
    print("Inorder traversal of the modified tree")
    inorder(root)

    res = search(root, 50)
    if res is None:
        print("50 Not Found")
    else:
        print("50 found")

# This code is contributed by Amit Mangal.
