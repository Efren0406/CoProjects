move_record = ['0']

class Record:
    def add(self, piece, id, i, j):
        if piece in ('Q', 'K', 'p', 'queen', 'king', 'pawn'):
            move_record.append(piece[0] + "2" + str(i) + str(j))
        else:
            move_record.append(piece[0] + str(id) + str(i) + str(j))

    def last_movement(self):
        return move_record[-1]

    def is_in_record(self, piece, id, color):
        for i in range(1, len(move_record)):
            move = move_record[i]
            if (move[0] == piece[0] and color == 'white'
               and str(id) == move[1]
               and i%2):
                return True
            elif (move[0] == piece[0] and color == 'black'
               and str(id) == move[1]
               and not i%2):
                return True
        
        return False
