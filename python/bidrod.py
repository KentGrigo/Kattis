numberOfSongs = int(input())
songs = list(map(int, input().split()))
uniqueSongs = list(dict.fromkeys(songs))
print(*uniqueSongs)
