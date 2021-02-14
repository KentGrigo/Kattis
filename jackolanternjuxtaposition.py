from functools import reduce
from operator import mul

designs = list(map(int, input().split()))
result = reduce(mul, designs, 1)
print(result)
