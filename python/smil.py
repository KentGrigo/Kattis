symbols = list(input())

penpreviousSymbol = '1'
previousSymbol = '1'
for index, currentSymbol in enumerate(symbols):
    twoSymbols = previousSymbol + currentSymbol
    threeSymbols = penpreviousSymbol + previousSymbol + currentSymbol
    if twoSymbols == ":)" or twoSymbols == ';)':
        print(index - 1)

    if threeSymbols == ":-)" or threeSymbols == ";-)":
        print(index - 2)

    penpreviousSymbol = previousSymbol
    previousSymbol = currentSymbol
