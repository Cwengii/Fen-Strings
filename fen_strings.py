fen ="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
# fen = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1"
# fen = "rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR w KQkq c6 0 2"
a = fen.split(" ")
display_board = a[0].split('/')

for line in display_board:
    row = ""
    for item in line:
        if item.isdigit():
            row += " . " * int(item)
        else:
            row += f" {item} "
    print(row)

a.remove(a[0])

Players = a[0]
Castling = a[1]
Passant = a[2]
Half_move = a[3]
Full_move = a[4]

if Players == 'w':
    print("White to move")
else:
    print("Black to move")

white_castle = "both sides" if 'K' in Castling and 'Q' in Castling else "kingside" if 'K' in Castling else "queenside" if 'Q' in Castling else "no sides" 

black_castle = "both sides" if 'k' in Castling and 'q' in Castling else "kingside"if 'k' in Castling else "queenside" if 'q' in Castling else "no sides"


print(f"White can castle {white_castle}") 
print(f"Black can castle {black_castle}") 

if Passant == '-':
    print("No en passant square")
else:
    print('None')

print(f"Halfmove clock: {Half_move}") 
print(f"Fullmove number: {Full_move}")
