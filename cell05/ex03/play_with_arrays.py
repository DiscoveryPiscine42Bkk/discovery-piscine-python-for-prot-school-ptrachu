arrays = [1, -1, 5, 9, 11, 9, 1, 54, -48, 99]
arrays2 = []
for x in arrays:
    if x>5:
        arrays2.append(x+2)
arrays2 = list(dict.fromkeys(arrays2))
print(arrays)
print(arrays2)
input()