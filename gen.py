
def generate_start_place(num_players, level, alignment):
    # TODO make this do something cool
    return f'place = {num_players} + {level} + {alignment} FIXME'

def generate_goal_place(num_players, level, alignment):
    return 0


lvl = input('enter level choice (A for 1-3, B for 4-6, C for 7-10):')

# FIXME this is kinda cruel, should let user type again
if lvl != 'A' and lvl != 'B' and lvl != 'C':
    print('you failed!')
    exit()

num_players = input('number of players (1-10):')
# FIXME validate 1-10
alignment = input('alignment:')
# FIXME validate alignment

start_place = generate_start_place(num_players, lvl, alignment)
print(start_place)


