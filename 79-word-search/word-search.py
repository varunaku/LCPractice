class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
         
        res = False

        def dfs(i, j, curr, visited):
            nonlocal res # res from higher scope
            if res: # if res is true, return.
                return
   
            if len(curr) >= len(word): # if we've exceed word length
                return 

            if i >= len(board) or j >= len(board[0]) or j < 0 or i < 0: # if we've exited the bounds of the board
                return
            
            if board[i][j] != word[len(curr)]: 
                # if the board value is not the same the next letter in word.
                # eg if curr = "CA", len(curr) is 2, and now word[len(curr)] == "T", and if board[i][j] != "T", it's false
                return 

            if (i, j) in visited:
                return # mark all visited
            
            curr = curr + board[i][j]

            if curr == word:
                res = True
                return 

            visited.add((i, j))

            dfs(i+1, j, curr, visited)
            dfs(i-1, j, curr, visited)
            dfs(i, j+1, curr, visited)
            dfs(i, j-1, curr, visited)

            visited.remove((i, j))  # backtrack



        for i in range(len(board)):
            for j in range (len(board[0])):
                if not res:
                    dfs(i, j, "", set())
        return res