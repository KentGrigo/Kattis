reversePolishTerms = input().split()
expressionHeap = []
for reversePolishTerm in reversePolishTerms:
    if reversePolishTerm in ['+', '-', '*', '/']:
        term2 = expressionHeap.pop()
        term1 = expressionHeap.pop()
        term = f'({term1}{reversePolishTerm}{term2})'
        expressionHeap.append(term)
    else:
        expressionHeap.append(reversePolishTerm)

infixExpression = expressionHeap.pop()
print(infixExpression)
