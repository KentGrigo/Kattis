line1 = input().split('|')
line2 = input().split('|')
sentence = ""
for word1, word2 in zip(line1, line2):
    if sentence != "":
        sentence += " "

    sentence += word1 + word2

print(sentence)
