board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
for item in skill:
    if item[0] == 1:
        # print(item[1], item[2])
        # print(item[3], item[4])
        # print(item[5])
        for i in range(item[1], item[3]+1):
            for j in range(item[2], item[4]+1):
                board[i][j] = board[i][j] - item[5]
    else:
        for i in range(item[1], item[3]+1):
            for j in range(item[2], item[4]+1):
                board[i][j] = board[i][j] + item[5]
print(board)
count = 0
for item in board:
    for x in item:
        if x > 0:
            count += 1
print(count)