index = int(input())
calibratedBinaryNumber = "{:b}".format(index + 1)
luckyNumber = calibratedBinaryNumber \
                .replace("0", "4") \
                .replace("1", "7") \
                [1:]
print(luckyNumber)
