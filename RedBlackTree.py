from enum import Enum


class RedBlackTree():
    def __init__(self):
        self.root = None

        # These tags will be set to perform a rotation in the next recursion
        # The rotation must be performed at the level above the two consecutive red nodes
        self.ll = False
        self.lr = False
        self.rl = False
        self.rr = False

    def insert(self, key):
        self.root = self._insert(key, self.root)
        self.root.is_red = False

    def _insert(self, key, curr):
        if curr == None:
            return RedBlackNode(key)
        elif key < curr.key:
            curr.left = self._insert(key, curr.left)
            curr.left.parent = curr
        elif key > curr.key:
            curr.right = self._insert(key, curr.right)
            curr.right.parent = curr


        # Do rotations if necessary
        if self.ll:
            curr = self.rotate_right(curr)
            curr.is_red = False
            curr.right.is_red = True
            self.ll = False

        elif self.lr:
            curr.left = self.rotate_left(curr.left)
            curr.left.parent = curr
            curr = self.rotate_right(curr)
            curr.is_red = False
            curr.right.is_red = True
            self.lr = False

        elif self.rl:
            curr.right = self.rotate_right(curr.right)
            curr.right.parent = curr
            curr = self.rotate_left(curr)
            curr.is_red = False
            curr.left.is_red = True
            self.rl = False

        elif self.rr:
            curr = self.rotate_left(curr)
            curr.is_red = False
            curr.left.is_red = True
            self.rr = False


        # Check for violation (parent and child are both red)
        # curr is parent

        if curr.left is not None:
            if curr.is_red and curr.left.is_red:  # Red violation on the left side
                if curr is curr.parent.left:  # curr is left child of parent (LL)

                    # CASE 2.1 - AUNT IS BLACK OR NONE (LL RED VIOLATION)
                    if curr.parent.right is None or not curr.parent.right.is_red:
                        self.ll = True

                    # CASE 1 - AUNT IS RED (LL RED VIOLATION)
                    else:  # Aunt of curr.left (sibling of curr) is red
                        # Recolour parent and aunt black, grandparent red
                        curr.is_red = False
                        curr.parent.is_red = True
                        curr.parent.right.is_red = False
                        
                else:  # curr is right child of parent (RL)

                    # CASE 2.2 - AUNT IS BLACK OR NONE (RL RED VIOLATION)
                    if curr.parent.left is None or not curr.parent.left.is_red:
                        self.rl = True

                    # CASE 1 - AUNT IS RED
                    else:  # Aunt of curr.left (sibling of curr) is red
                        # Recolour parent and aunt black, grandparent red
                        curr.is_red = False
                        curr.parent.is_red = True
                        curr.parent.left.is_red = False
                        
        if curr.right is not None:
            if curr.is_red and curr.right.is_red:  # Red violation on the right side
                if curr is curr.parent.left:  # curr is left child of parent (LR)

                    # CASE 2.2 - AUNT IS BLACK (LR RED VIOLATION)
                    if curr.parent.right is None or not curr.parent.right.is_red:
                        self.lr = True

                    # CASE 1 - AUNT IS RED
                    else:  # Aunt of curr.right (sibling of curr) is red
                        # Recolour parent and aunt black, grandparent red
                        curr.is_red = False
                        curr.parent.is_red = True
                        curr.parent.right.is_red = False

                else:  # curr is right child of parent (RR)

                    # CASE 2.1 - AUNT IS BLACK (RR RED VIOLATION)
                    if curr.parent.left is None or not curr.parent.left.is_red:
                        self.rr = True

                    # CASE 1 - AUNT IS RED
                    else:  # Aunt of curr.right (sibling of curr) is red
                        # Recolour parent and aunt black, grandparent red
                        curr.is_red = False
                        curr.parent.is_red = True
                        curr.parent.left.is_red = False

        return curr
    

    def rotate_left(self, root):
        x = root.right
        y = x.left
        x.left = root
        root.right = y
        root.parent = x
        if y is not None:
            y.parent = root
        return x

    def rotate_right(self, root):
        x = root.left
        y = x.right
        x.right = root
        root.left = y
        root.parent = x
        if y is not None:
            y.parent = root
        return x


    # Returns a string representation of the tree using parentheses
    def __str__(self):
        if self.root is None:
            return ""
        return self.___str__(self.root)

    # Helper function for __str__() used for recursion
    # curr is the root of the currently examined subtree
    def ___str__(self, curr):
        string = str(curr.key)
        string += "R" if curr.is_red else "B"

        has_left = curr.left
        has_right = curr.right

        if has_left:
            string += "(" + self.___str__(curr.left) + ")"
        elif has_right:
            string += "()"  # Indicate that the only child is a right node

        if has_right:
            string += "(" + self.___str__(curr.right) + ")"

        return string



class RedBlackNode():
    def __init__(self, key):
        self.key = key
        self.is_red = True
        self.left = None
        self.right = None
        self.parent = None


def main():
    t = RedBlackTree()
    t.insert(8)
    t.insert(18)
    t.insert(5)
    t.insert(15)
    t.insert(17)
    t.insert(25)
    t.insert(40)
    t.insert(80)
    print(t)


if __name__ == "__main__":
    main()