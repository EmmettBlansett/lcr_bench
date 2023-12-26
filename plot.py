import matplotlib.pyplot as plt
import numpy as np

def add_to_plot(fp = ''):
    if(fp == ''):
        fp = f'data/lcr_player_data6.txt'
    w = []
    for line in open(fp, 'r'):
        w.append(int(line))

    fig, ax = plt.subplots()
    ax.hist(w, bins = np.arange(1,8), align='left', weights=np.ones(len(w))/len(w), edgecolor='black')
    exp = ax.axhline(y=1/6, color = 'r', linestyle = 'dotted', label = f'Expected Win Rate({str(round(1/6,4))})')
    ax.set_ylim([.15,.18])
    plt.xlabel('Player Number')
    plt.ylabel('Win Rate')
    plt.title(f'Win Rate by Player Number (6 players)')
    plt.legend()
    for c in ax.containers:
        ax.bar_label(c)
    plt.rcParams.update({'font.size': 9})


if __name__ == '__main__':
    add_to_plot()

    plt.savefig(f'data/plot6')
