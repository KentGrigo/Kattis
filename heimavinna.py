intervals = input().split(";")

numberOfChapters = 0
for interval in intervals:
    interval = interval.split("-")
    startChapter = int(interval[0])
    endChapter = int(interval[1]) if len(interval) == 2 else startChapter
    difference = endChapter - startChapter + 1
    numberOfChapters += difference

print(numberOfChapters)
