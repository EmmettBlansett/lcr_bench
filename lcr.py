from random import choice

def get_left(player_num, player_count):
    if(player_num - 1 < 0):
        return player_count-1
    else:
        return player_num - 1
        
def get_right(player_num, player_count):
    if(player_num + 1 > player_count-1):
        return 0
    else:
        return player_num + 1

def execute_roll(roll, game, player_count, player_num, center):
    for die in roll:
        if(die == '.'):
            continue
        game[player_num]-=1
        match die:
            case 'l':
                game[get_left(player_num, player_count)]+=1
            case 'c':
                center += 1
            case 'r':
                game[get_right(player_num, player_count)]+=1
    return game, center

def get_roll(chips, dice):
    if(chips == 0):
        return []
    return [choice(dice) for i in range(min(chips,3))]

def lcr_game_loop(game, player_count, dice):
    player_num = 0
    center = 0
    while(center + max(game) < player_count * 3):
        if(game[player_num] == 0):
            player_num+=1
            if(player_num == player_count):
                player_num = 0
            continue
        roll = get_roll(game[player_num], dice)
        game, center = execute_roll(roll, game, player_count, player_num, center)
        player_num+=1
        if(player_num == player_count):
            player_num = 0
    return [i for i, e in enumerate(game) if e != 0][0]+1
        