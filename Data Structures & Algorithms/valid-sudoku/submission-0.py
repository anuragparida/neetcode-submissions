class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def whichbox(i,j):
            if i <= 2:
                if j <= 2:
                    return 0
                elif j <= 5:
                    return 1
                return 2
            elif i <= 5:
                if j <= 2:
                    return 3
                elif j <= 5:
                    return 4
                return 5
            else:
                if j <= 2:
                    return 6
                elif j <= 5:
                    return 7
                return 8
        cols = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                v = board[i][j]
                if v == ".":
                    continue
                if v in cols[j]:
                    return False
                if v in rows[i]:
                    return False
                bn = whichbox(i,j)
                if v in boxes[bn]:
                    return False
                cols[j].add(v)
                rows[i].add(v)
                boxes[bn].add(v)
        return True