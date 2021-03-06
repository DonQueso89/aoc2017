import sys
from collections import defaultdict
from itertools import cycle


def solve1(num_players, num_marbles):
    players = cycle(range(num_players))
    scores = defaultdict(int)
    # idx -> marble
    marbles = [0, 2, 1]

    marble_idx = 1
    for marble in range(3, num_marbles + 1):
        player = next(players)
        if marble % 23 == 0:
            scores[player] += marble
            marble_idx -= 7
            if marble_idx < 0:
                marble_idx = len(marbles) + marble_idx
            scores[player] += marbles.pop(marble_idx)
        else:
            insertion_idx = marble_idx + 2
            if insertion_idx == len(marbles):
                marbles.append(marble)
            else:
                insertion_idx %= len(marbles)
                marbles.insert(insertion_idx, marble)
            marble_idx = insertion_idx
    print('Part 1: ' + str(sorted([(k, v) for k, v in scores.items()], key=lambda x: x[1])[-1]))
    print(list(scores))


def solve2(num_players, num_marbles):
    """
    Growth by 22 elems every 23 marbles
    Index == ((((((0 + 2 % 2) + 2) % 2) + 2) % 2) ... -7) % 2
    """
    pass


if __name__ == '__main__':
    data = open('input9').read().split()
    num_players, num_marbles = int(data[0]), int(data[6] * int(sys.argv[1]))
    solve1(num_players, num_marbles)
