import sys
len = len(list(sys.argv))
i = 1
while i < len:
    if 'ism' not in sys.argv[i]:
        print(sys.argv[i]+'ism')
    i += 1