def test(value, epsilon):
    start = 0
    end = value
    while True:
        half = start + (end - start) / 2 
        power = value ** (1 / float(half))
        if start == value:
            return None
        if power + epsilon < half:
            end = half
        elif half < power - epsilon:
            start = half
        else: # power - epsilon < half < power + epsilon:
            return half


epsilon = 10 ** -7
value = int(input())
result = test(value, epsilon)
print(result)
