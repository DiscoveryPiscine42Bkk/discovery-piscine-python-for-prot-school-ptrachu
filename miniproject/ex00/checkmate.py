def checkmate(board):
    board = str(board).split()
    n = len(board)
    king_pos = None 
    
    directions = {
        'R': [(0, 1), (1, 0), (0, -1), (-1, 0)],
        'B': [(1, 1), (1, -1), (-1, 1), (-1, -1)],
        'Q': [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)],
    }

    pawn_moves = [(-1, -1), (-1, 1)]

    i = 0
    while i < n and king_pos is None:
        j = 0
        while j < n:
            if board[i][j] == 'K':  
                king_pos = (i, j)
                break
            j += 1
        if king_pos:
            break
        i += 1

    if not king_pos:
        print("Fail")
        return
    
    def can_attack(i, j, x, y, piece):
        if piece in directions:
            for di, dj in directions[piece]:
                ni, nj = i + di, j + dj
                while 0 <= ni < n and 0 <= nj < n:
                    if (ni, nj) == (x, y):
                        return True
                    if board[ni][nj] in "PQRB":
                        break
                    ni, nj = ni + di, nj + dj
        
        elif piece == 'P':
            for di, dj in pawn_moves:
                if (i + di, j + dj) == (x, y):
                    return True
        
        return False

    i = 0
    while i < n:
        j = 0
        while j < n:
            piece = board[i][j]
            if piece in directions or piece == 'P':
                if can_attack(i, j, king_pos[0], king_pos[1], piece):
                    print("Success")
                    return
            j += 1
        i += 1
    
    print("Fail")
