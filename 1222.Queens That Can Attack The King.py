from typing import List


class Solution:
    def queensAttacktheKing(
        self, queens: List[List[int]], king: List[int]
    ) -> List[List[int]]:
        board = [[None for y in range(8)] for x in range(8)]
        for queen in queens:

            board[queen[0]][queen[1]] = 1
        board[king[0]][king[1]] = 0
        directions = [
            [0, 1],
            [1, 0],
            [1, 1],
            [-1, -1],
            [1, -1],
            [-1, 1],
            [0, -1],
            [-1, 0],
        ]

        answer = []
        for direction in directions:
            exploringPosition = king.copy()
            print("direction = {}".format(direction))
            exploringPosition = self.getExploringPosition(exploringPosition, direction)
            while self.legit(exploringPosition, board):
                print("exploring {}".format(exploringPosition))
                if self.isQueen(exploringPosition, board):
                    print("is queen!")
                    answer.append(exploringPosition.copy())
                    break
                else:
                    exploringPosition = self.getExploringPosition(
                        exploringPosition, direction
                    )
        print(answer)
        return answer

    def getExploringPosition(self, exploringPosition, direction):
        exploringPosition[0] += direction[0]
        exploringPosition[1] += direction[1]
        return exploringPosition

    def isQueen(self, exploringPosition, board):
        return board[exploringPosition[0]][exploringPosition[1]] == 1

    def legit(self, exploringPosition, board):
        return (
            0 <= exploringPosition[0]
            and exploringPosition[0] < len(board)
            and 0 <= exploringPosition[1]
            and exploringPosition[1] < len(board)
        )


Solution().queensAttacktheKing(
    queens=[[0, 0], [1, 1], [2, 2], [3, 4], [3, 5], [4, 4], [4, 5]], king=[3, 3]
)

