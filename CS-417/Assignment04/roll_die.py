import sys
import random
from typing import List

def cummulative_probabilities(probs: List[float]) -> List[float]:
    '''
    Parameter:
    ---------
    probs: a list of probabilities

    Returns:
    a list of cummulative probabilities
    '''
    # Or create an initial list using:   [0] * <the length>

    cumm_probs = []

    # Here, build the table of cummulative probabilities.
    # It should obey this pattern:
    # first one:  cumm_probs[0] = probs[0]
    # all others: cumm_probs[i] = cumm_probs[i-1] + probs[i]
    cumm_probs.append(probs[0])
    for i in range(1, len(probs)):
        cumm_probs.append(cumm_probs[i-1] + probs[i])

    return cumm_probs

def biased_generator(cumm_probs: List[float], n_runs: int) -> None:
    '''
    Parameters:
    cumm_probs: A list of cummulative probabilities,
    n_runs: how many times to yield

    Yield: A number from 0 to len(cumm_probs)-1,
           generated with biased probability.
    '''

    for run in range(n_runs):

        # Here, generate a random value (x = random.random()),

        # Then find k, the index where it falls in the cummulative table.
        # To do this, loop through the indexes into cumm_prob, and
        # find the first k that has x < cumm_prob[k]
        # (and break out of your loop!)

        # Here, YIELD the index where the value falls
        x = random.random()
        for k, prob in enumerate(cumm_probs):
            if prob > x:
                break
        yield k

def main():
    probs  = [0.1, 0.2, 0.1, 0.2, 0.15, 0.25]

    cumm_probs = cummulative_probabilities(probs)
    for x in biased_generator(cumm_probs, 10000):
        print (x)

if __name__ == '__main__':
        main()
