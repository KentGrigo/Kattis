class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left == None:
                self.left = BinaryTree(value)
            else:
                self.left.insert(value)
        elif self.value < value:
            if self.right == None:
                self.right = BinaryTree(value)
            else:
                self.right.insert(value)
        else:
            raise ValueError("Value '{}' has already been added to the tree".format(value))

    def sameShape(self, other):
        noLeftChildren = self.left == None and other.left == None
        noRightChildren = self.right == None and other.right == None
        sameLeftChildren = self.left != None and other.left != None and self.left.sameShape(other.left)
        sameRightChildren = self.right != None and other.right != None and self.right.sameShape(other.right)
        return (noLeftChildren or sameLeftChildren) and (noRightChildren or sameRightChildren)

def hasUniqueShape(tree, shapes):
    for shape in shapes:
        if tree.sameShape(shape):
            return False

    return True


numberOPrototypes, numberOfLayers = list(map(int, input().split()))
uniqueShapes = []
for _ in range(numberOPrototypes):
    layers = list(map(int, input().split()))
    root = BinaryTree(layers[0])
    for layer in layers[1:]:
        root.insert(layer)

    if hasUniqueShape(root, uniqueShapes):
        uniqueShapes.append(root)

numberOfUniqueShapes = len(uniqueShapes)
print(numberOfUniqueShapes)
