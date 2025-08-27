class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
         
        res = False

        def dfs(i, j, curr):
            nonlocal res # res from higher scope
            if res: # if res is true, return.
                return True
   
            if len(curr) >= len(word): # if we've exceed word length
                return False

            if i >= len(board) or j >= len(board[0]) or j < 0 or i < 0: # if we've exited the bounds of the board
                return False
            
            if board[i][j] != word[len(curr)]: 
                # if the board value is not the same the next letter in word.
                # eg if curr = "CA", len(curr) is 2, and now word[len(curr)] == "T", and if board[i][j] != "T", it's false
                return False

            if len(curr) == len(word) - 1:
                res = True
                return True
    
            tmp = board[i][j]       
            curr_n = curr + board[i][j]    # mar
            board[i][j] = "#" # mark al
            

            found = ( dfs(i+1, j, curr_n) or dfs(i-1, j, curr_n) or dfs(i, j+1, curr_n) or dfs(i, j-1, curr_n))
            board[i][j] = tmp
            return found

          # backtrack


        for i in range(len(board)):
            for j in range (len(board[0])):
                if not res:
                    dfs(i, j, "")
        return res