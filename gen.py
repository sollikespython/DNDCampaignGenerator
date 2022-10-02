
from formatter import NullFormatter
import random
from readline import set_completion_display_matches_hook

def randolist(list):
    rnd = random.randint(0, len(list)-1)
    return list[rnd]

def generate_start_place(num_players, lvl):
    # TODO make this do something cool
    if lvl == 'a':
       location_start.pop(1)
    elif lvl == 'b':
        # some other pop
        pass
    elif lvl == 'c':
        # some other pop
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

def lvl_select():
    # returns a string of a, b, or c
    selection_valid = False
    user_selection = None

    while selection_valid is False:
        valid_selections = ('a', 'b', 'c')
        selection_input = input('Enter level choice (A for 1-3, B for 4-6, C for 7-10: ').lower()

        if selection_input not in valid_selections:
            input('That  is not a valid selection, press any key to try again... ')
            
        else:
            user_selection = selection_input
            selection_valid = True

    return user_selection

def num_players():
    # validate 1 - 10
    # No idea if this is a good way to make a check like this
    selection_valid = False
    user_selection = None

    while selection_valid is False:
        valid_selections = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        selection_input = input('Enter the number of players (1 - 10): ')

        try:
            selection_input = int(selection_input)

            if selection_input not in valid_selections:
                input('That is not a valid selection, press any key to try again... ')

            else:
                user_selection = selection_input
                selection_valid = True
        except:
            input('Please enter an integer between 1 and 10. Press any key to try again... ')

    return user_selection

start_place = generate_start_place(num_players(), lvl_select())
print(start_place)


