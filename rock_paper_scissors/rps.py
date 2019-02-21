#!/usr/bin/python

import sys

plays = ['rock', 'paper', 'scissors']


def rock_paper_scissors(n):
    # define possible plays, and make list of  possibleOutcomes
    outcomes = []
    plays = ['rock', 'paper', 'scissors']

    # make helper function that can take the rounds left (n), and the result(empty [])
    #  as long as there are plays left, for every item in the plays array, it will add it to the results array
    # if there are no rounds left, it will take all the results and put it in the outcomes array
    #  call the helper function, and return the outcomes array to get your answer
    def possibleOutcomes(roundsLeft, result):
        if roundsLeft == 0:
            outcomes.append(result)
            return
        for play in plays:
            possibleOutcomes(roundsLeft - 1, result + [play])

    possibleOutcomes(n, [])
    return outcomes


print(rock_paper_scissors(3))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
