import sys
parameter_count = len(sys.argv)-1
character_count = 0
if len(sys.argv) > 1:
    print('parameter(s):',parameter_count)
    for parameter in sys.argv[1:]:
        print(parameter+':',len(parameter))
else:
    print('none')
