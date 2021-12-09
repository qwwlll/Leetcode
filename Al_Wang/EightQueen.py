from typing import List
#### eight Queens
BOARD_SIZE = 8
solution_count = 0
queen_list = [0] * BOARD_SIZE
def eightQueens(cur_column: int):
    if cur_column >= BOARD_SIZE:
        global solution_count
        solution_count += 1
        print(queen_list)
    else:
        for i in range(BOARD_SIZE):
            if vaild_pos(cur_column, i):
                queen_list[cur_column] = i
                eightQueens(cur_column + 1)

def vaild_pos(cur_column: int, pos: int) -> bool:
    i = 0
    while i < cur_column:
        if queen_list[i] == pos:
            return False
        elif cur_column - i == abs(queen_list[i]- pos):
            return False
        else:
            i += 1
    return True


if __name__ == '__main__':
    print('--- eight queens sequence ---')
    eightQueens(0)

    print('\n--- solution count ---')
    print(solution_count)