words = input().split()
numberOfWords = 0
numberOfOstgotskaWords = 0
for word in words:
    numberOfWords += 1
    if "ae" in word:
        numberOfOstgotskaWords += 1

percentage = numberOfOstgotskaWords / numberOfWords * 100
if 40 <= percentage:
    print("dae ae ju traeligt va")
else:
    print("haer talar vi rikssvenska")
