lvl = input('enter level choice (A for 1-3, B for 4-6, C for 7-10):')

# FIXME this is kinda cruel, should let user type again
if lvl != 'A' and lvl != 'B' and lvl != 'C':
    print('you failed!')
    exit()

# this tells them they did it right
print(f'you chose {lvl}, winner')
