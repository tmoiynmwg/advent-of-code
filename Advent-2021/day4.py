
class Cell:
    def __init__(self, num):
        self.num = num
        self.marked = False

    def __str__(self):
        return f'({self.num}, {self.marked})'

class Board:
    def __init__(self):
        self.rows = []

    def __str__(self):
        output = ''
        for row in self.rows:
            for cell in row:
                output += str(cell) + ', '
            output = output[:-2] + '\n'
        output += '\n'
        return output

    def add_row(self, row):
        self.rows.append(row.copy())

    def mark(self, num):
        #print(f'   {num}')
        for row in self.rows:
            for cell in row:
                #print(cell.num)
                if cell.num == num:
                    #print('nah')
                    cell.marked = True

    @classmethod
    def check_row(cls, row):
        for cell in row:
            if not cell.marked:
                return False
        return True

    def win(self):
        for row in self.rows:
            if Board.check_row(row):
                return True
        for i in range(len(self.rows[0])):
            if Board.check_row([row[i] for row in self.rows]):
                return True
        return False

    def unmarked_sum(self):
        total = 0
        for row in self.rows:
            for cell in row:
                if not cell.marked:
                    total += cell.num
        return total

def bingo(filename, first_win):
    with open(filename) as input_file:
        seq = [int(x) for x in input_file.readline().split(',')]
        input_file.readline()   # skip a line
        boards, board = [], Board()
        for line in input_file:
            if line.isspace():
                boards.append(board)
                #print(board)
                #print(check_board(board))
                board = Board()
            else:
                row = [int(x) for x in line.split()]
                board.add_row([Cell(num) for num in row])

        for num in seq:
            for board in boards[:]:
                board.mark(num)
                #print(board)
                if board.win():
                    if first_win or len(boards) == 1:
                        return num * board.unmarked_sum()
                    else:
                        boards.remove(board)

def main():
    print(bingo("day4-input", False))

if __name__ == "__main__":
    main()