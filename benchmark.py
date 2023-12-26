import lcr

from alive_progress import alive_bar

def benchmark(player_count: int, iterations: int, fp: str):
    f = open(fp, 'a')
    dice = ['.','.','.','l','c','r']
    with alive_bar(iterations) as bar:
        for _ in range(iterations):
            game = [3] * player_count
            w = lcr.lcr_game_loop(game, player_count, dice)
            f.write(f'{w}\n')
            bar()
    f.close()

if __name__ == '__main__':
    fp = f'data/lcr_player_data6.txt'

    benchmark(6, 1000000, fp)
