startX, startY = list(map(int, input().split()))
endX, endY = list(map(int, input().split()))
numberOfCharges = int(input())

diffX = abs(endX - startX)
diffY = abs(endY - startY)
diff = diffX + diffY

numberOfChargesLeft = numberOfCharges - diff
if 0 <= numberOfChargesLeft and numberOfChargesLeft % 2 == 0:
    print("Y")
else:
    print("N")
