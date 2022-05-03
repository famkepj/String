# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

player_one = 'Ruud Gullit'
player_two = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = (f'{player_one} {str(goal_0)}, {player_two} {str(goal_1)}')
print (scorers)

report = (f'{player_one} scored in the {goal_0}nd minute\n{player_two} scored in the {goal_1}th minute')
print(report)

player = 'Frank Rijkaard'
first_name = (player[:5])
last_name_len = (len(player[6:]))
name_short = (player[:1]) + '. ' + (player[6:])
chant = (first_name +'!'+ ' ') * (len(player[:5-1])) + (first_name +'!')
good_chant = (chant[:-1] !=' ')
print(good_chant)