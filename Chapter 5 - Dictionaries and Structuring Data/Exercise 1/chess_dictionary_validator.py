CHESS_PIECE_NAMES = ["king", "queen", "rook", "bishop", "knight", "pawn"]
CHESS_PIECE_COLORS = "wb"  # 'w' as a white and 'b' as a black
Y_COORDINATES = "abcdefgh"
X_COORDINATES = "12345678"
MAX_PAWNS = 8
MAX_KINGS = 1


def validate_chess_board(position):
    # Validating coordinates
    if not all([coordinate[0] in X_COORDINATES and coordinate[1] in Y_COORDINATES for coordinate in position.keys()]):
        print("There was piece with invalid x or y coordinate.")
        return False

    # Validating piece colors
    if not all([piece[0] in CHESS_PIECE_COLORS for piece in position.values()]):
        print("There was piece that was not black or white, or you didn't specify the color")
        return False

    # Validating piece names
    if not all([piece[1:] in CHESS_PIECE_NAMES for piece in position.values()]):
        print("There was piece with name that does not exist in chess")
        return False

    # Validating Kings
    if not len(list(filter(lambda x: x == "wking", [piece for piece in position.values()]))) == 1:
        print("There should be exactly one white king")
        return False

    if not len(list(filter(lambda x: x == "bking", [piece for piece in position.values()]))) == 1:
        print("There should be exactly one black king")
        return False

    return True


if __name__ == "__main__":
    position = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '6c': 'bqueen', '3e': 'wking'}
    print([key + " " + value for key, value in position.items()])
    if validate_chess_board(position):
        print("This position IS possible in chess")
    else:
        print("This position IS NOT possible in chess")