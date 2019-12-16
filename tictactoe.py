count = {'games': 0, 'X': 0, 'O': 0, 'tie': 0}


def gameplay():
    position_table = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' '],
                      ]
    player_turn = 0
    winner = ''

    def gameboard(table):
        for x in range(0, 3):
            print(' ...' * 3)
            print('| ' + str(table[x][0]) + ' | ' + str(table[x][1]) + ' | ' + str(table[x][2]) + ' |')
        print(' ...' * 3)

    def player_input(turn):
        if turn % 2 == 0:
            choice = input('Player 1 chose row 1-3 and column 1-3, sep. by comma 1,3 for X:')
            choice = choice.split(',')
            choice.insert(0, 'X')
        else:
            choice = input('Player 2 chose row 1-3 and column 1-3, sep. by comma 1,3 for O:')
            choice = choice.split(',')
            choice.insert(0, 'O')
        return choice

    def rewrite_table(place, table):
        if table[int(place[1]) - 1][int(place[2]) - 1] != 'X' \
                and table[int(place[1]) - 1][int(place[2]) - 1] != 'O':
            table[int(place[1]) - 1][int(place[2]) - 1] = place[0]
        else:
            print('This position is already taken! Chose other')
            rewrite_table(player_input(player_turn), table)

    def check_winer(matrix, turn):
        for i in range(0, 3):
            if matrix[0][i] == matrix[1][i] == matrix[2][i] != ' ':
                print('The winer is ' + str(matrix[0][i]))
                return str(matrix[0][i])
        for i in range(0, 3):
            if matrix[i][0] == matrix[i][1] == matrix[i][2] != ' ':
                print('The winer is ' + str(matrix[i][0]))
                return str(matrix[i][0])
        if matrix[0][0] == matrix[1][1] and matrix[1][1] == matrix[2][2] != ' ':
            print('1st diag, The winer is ' + str(matrix[2][2]))
            return str(matrix[2][2])
        elif matrix[0][2] == matrix[1][1] and matrix[1][1] == matrix[2][0] != ' ':
            print('2nd diag, The winer is ' + str(matrix[2][0]))
            return str(matrix[2][0])
        elif turn == 8:
            print("It's a tie!")
            return 'tie'
        else:
            return ''

    while player_turn < 9 and winner == '':
        mark_position = player_input(player_turn)
        rewrite_table(mark_position, position_table)
        winner = check_winer(position_table, player_turn)
        player_turn += 1
        gameboard(position_table)

    return winner


if __name__ == '__main__':
    while True:
        key = gameplay()
        count['games'] += 1
        count[key] += 1
        play = input('Would you like to play again? Y/N ')
        if play == 'N' or play == 'n':
            break

    for arg, val in count.items():
        print(arg, val)
