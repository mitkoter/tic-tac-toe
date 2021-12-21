from player import RandomComputerPlater,HumanPlayer

class TicTacToe:
    def __init__(self):
        self.board = ['*' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[xx * 3:(xx + 1) * 3] for xx in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def prin_board_nums():
        number_board = [[str(xx) for xx in range(yy * 3, (yy + 1) * 3)] for yy in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        moves = [ind for ind, value in enumerate(self.board) if (value == '*')]
        return moves

    def empty_squares(self):
        if '*' in self.board:
            return True
        else:
            return False

    def num_empty_squares(self):
        return self.board.count('*')

    def make_move(self, square, letter):
        if self.board[square] == '*':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind * 3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        if square % 2 == 0:
            diag_1 = [self.board[xx] for xx in [0,4,8]]
            diag_2 = [self.board[xx] for xx in [2,4,6]]

            if all([spot == letter for spot in diag_1]) or all([spot == letter for spot in diag_2]):
                return True
        
        return False

def play(game, x_player, o_player, print_game = True):
    if print_game:
        game.prin_board_nums()
    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        if game.make_move(square, letter):
            if print_game:
                print (letter + ' makes a move to {}'.format(square))
                game.print_board()
                print('')
            
            if game.current_winner:
                print(letter + ' Wins!')
                return letter
            letter = 'O' if letter == 'X' else 'X'

    if print_game:
        print('Its a tie!')

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlater('O')
    tic_tac_toe = TicTacToe()
    play(tic_tac_toe, x_player, o_player, print_game=True)