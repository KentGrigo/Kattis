class1 = input()
class2 = input()
mergedClass = class1 + class2
mergedClass = list(mergedClass)
mergedClass.sort()
mergedClass = "".join(mergedClass)
print(mergedClass)
