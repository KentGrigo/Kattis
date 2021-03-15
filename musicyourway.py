attributes = input().split()
numberOfSongs = int(input())
songs = []
for _ in range(numberOfSongs):
    songAttributes = input().split()
    song = {}
    for attribute, songAttribute in zip(attributes, songAttributes):
        song[attribute] = songAttribute

    songs.append(song)

isFirstSorting = True
numberOfSortingCommands = int(input())
for _ in range(numberOfSortingCommands):
    if isFirstSorting:
        isFirstSorting = False
    else:
        print("")

    sortingCommand = input()
    songs.sort(key = lambda song: song[sortingCommand])
    print(" ".join(attributes))
    for song in songs:
        print(" ".join(song.values()))
