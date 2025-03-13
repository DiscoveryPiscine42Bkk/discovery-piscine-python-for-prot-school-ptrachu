import sys
if len(sys.argv) == 3:
    word = sys.argv[1]
    i = 0
    count = 0
    while i < len(sys.argv[2].split()):
        if word in sys.argv[2].split()[i]:
            count += 1
        i += 1
    print(count)
else:
    print('none')