keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
        "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
        "SPACE", "CAPS", "DELETE", "SHIFT_DOWN", "SHIFT_UP"]
sounds = ["clank", "bong", "click", "tap", "poing", "clonk", "clack", "ping", "tip", "cloing", "tic", "cling", "bing",
          "pong", "clang", "pang", "clong", "tac", "boing", "boink", "cloink", "rattle", "clock", "toc", "clink", "tuc",
          "whack", "bump", "pop", "dink", "thumb", ]

soundToKey = {}
for key, sound in zip(keys, sounds):
    soundToKey[sound] = key

isCapitalized = False
text = ""
numberOfSounds = int(input())
for _ in range(numberOfSounds):
    sound = input()
    key = soundToKey[sound]
    if key in ["CAPS", "SHIFT_DOWN", "SHIFT_UP"]:
        isCapitalized = not isCapitalized
    elif key == "DELETE":
        text = text[:-1]
    elif key == "SPACE":
        text += " "
    else:
        letter = key
        if isCapitalized:
            letter = letter.upper()

        text += letter

print(text)
