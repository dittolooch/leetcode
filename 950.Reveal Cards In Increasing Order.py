from typing import List
from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck = sorted(deck)
        print(deck)
        simulated_indices = [x for x in range(len(deck) - 1, -1, -1)]
        print("simulated indices")
        print(simulated_indices)
        simulated_deque = deque(simulated_indices)
        results = []
        while len(simulated_deque):
            top = simulated_deque.pop()
            results.append(top)
            if len(simulated_deque):
                toPushBack = simulated_deque.pop()
                simulated_deque.appendleft(toPushBack)
        print("simulation result")
        print(results)
        final = [0] * len(results)
        for ind, original in enumerate(deck):
            final[results[ind]] = original
        print(final)


Solution().deckRevealedIncreasing([4, 1, 3, 5, 9])

