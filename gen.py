
import random

def randolist(list):
    rnd = random.randint(0, len(list)-1)
    return list[rnd]

def generate_start_place(num_players, level):
    # TODO make this do something cool
    if lvl == 'A':
       location_start.pop(1)
    elif lvl == 'B':
        #some other pop
        pass
    return randolist(location_start)

def generate_goal_place(num_players, level):
    if lvl == 'A':
        location_goal.pop(7)
        location_goal.pop(6)
    return 0

def d_20():
    return random.randint(1,20)

location_start = [
    'A old growth forest, perfect for foraging.',
    'Deep in a fae forest, how did we get here?',
    'A noisy inn.',
    'A quiet, calm inn.',
    'A still pond.',
    'A bridge, what is it over?',
    'At the edge of a rushing river.',
    'A town in a cave system.',
    'A desert village.',
    'A lonely cabin.',
]

location_goal = [
    'A cave deep under a town.',
    'A temple in ruin.',
    'An abandonded village, who lived here? Why did they leave?',
    'A travelling circus.',
    'I got writers block writing this.',
    'The bottom of a ravine, I think it was formed unnaturally...',
    'A place very similar, but very different from where you started.',
    'An underwater city.',
    'A gate, of one sort or another.',
    'A castle, but perhaps not one of a king.',
    'The annoying guys house.',
    'Inside a very large plant, or maybe a normal sized plant and you are very small.'
]

lvl = input('enter level choice (A for 1-3, B for 4-6, C for 7-10):')

# FIXME this is kinda cruel, should let user type again
if lvl != 'A' and lvl != 'B' and lvl != 'C':
    print('you failed!')
    exit()


num_players = input('number of players (1-10):')
# FIXME validate 1-10

start_place = generate_start_place(num_players, lvl)
print(start_place)


