#/usr/bin/python
#-*- coding:utf-8 -*-

def ChessBoard(tr, tc, dr, dc, size):
	global Board
	global tile

	if size == 1: return
	
	tile += 1
	t, s = tile, size/2

	if dr<tr+s and dc<tc+s:
			ChessBoard(tr, tc, dr, dc, s)
	else:
			Board[tr+s-1][tc+s-1] = t
			ChessBoard(tr, tc, tr+s-1, tc+s-1, s)

	if dr<tr+s and dc>=tc+s:
			ChessBoard(tr, tc+s, dr, dc, s)
	else:
			Board[tr+s-1][tc+s] = t
			ChessBoard(tr, tc+s, tr+s-1, tc+s, s)

	if dr>=tr+s and dc<tc+s:
			ChessBoard(tr+s, tc, dr, dc, s)
	else:
			Board[tr+s][tc+s-1] = t
			ChessBoard(tr+s, tc, tr+s, tc+s-1, s)

	if dr>=tr+s and dc>=tc+s:
			ChessBoard(tr+s, tc+s, dr, dc, s)
	else:
			Board[tr+s][tc+s] = t
			ChessBoard(tr+s, tc+s, tr+s, tc+s, s)

def printBoard():
	global Board
	for i in range(len(Board)):
			for item in Board[i]:
					print item,'\t',
			print '\r'

if __name__ == "__main__":
		SIZE, dr, dc = input("size:"), input("dr:"), input("dc:")
		Board = [[0 for i in range(SIZE)] for i in range(SIZE)]

		tile = 0

		ChessBoard(0, 0, dr, dc, SIZE)
	
		printBoard()	
