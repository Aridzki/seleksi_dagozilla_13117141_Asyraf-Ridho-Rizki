#!/usr/bin/env python

'''
SELEKSI CALON KRU PROGRAMMING DAGOZILLA 2018
Take Home Test
File name: sudoku.py
Problem 2: Code Comprehension
'''

import sys
import numpy as np

def read_from_file(filename, board):                #Fungsi untuk membaca input
    with open(filename) as f:                       #Membuka file
        data = f.readlines()

    for i in range(9):
        for j in range(9):                          #Memasukan data input ke array data untuk diolah
            if data[i][j] == '-':
                board[i][j] = int(0)
            else:
                board[i][j] = int(data[i][j])


# What does this function do?
# ANS Mencetak sodoku seperti pada file input
def print_board(board):                             #Fungsi untuk print data input
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                print '-',
            else:
                print board[i][j],
        print('')
 

def save_board(filename, board):                                #Menyimpan sodoku yang ingin disolve
    np.savetxt(filename, board, delimiter=' ', fmt='%i')


# What does this function do?
# ANS Mencari sel yang memiliki nilai 0
def find_empty_location(board, l):
    for row in range(9):
        for col in range(9):
            # What happens inside the 'if' section?
            # ANS Menyimpan row dan kolom sel kosong ke dalam array
            if(board[row][col]==0):
                l[0]=row
                l[1]=col
                return True
    return False
    # Why does this function return a boolean value?
    # ANS untuk dijadikan syarat if


def used_in_row(board, row, num):
    for i in range(9):
        if(board[row][i] == num):
            return True
    return False


def used_in_col(board, col, num):
    for i in range(9):
        if(board[i][col] == num):
            return True
    return False


def used_in_block(board, row, col, num):
    for i in range(3):
        for j in range(3):
            if(board[i+row][j+col] == num):
                return True
    return False


def is_valid(board, row, col, num):
    return not used_in_row(board, row, num) \
        and not used_in_col(board,col,num) \
        and not used_in_block(board,row - row%3,col - col%3,num)
    # What makes this function return True (what makes it valid for a number in a given location)?
    # ANS ketika angka num tidak dipakai 2 kali dalam row, col, dan block


# Explain the algorithm in this function!
# ANS Program akan mencari sel kosong (bernilai 0) lalu menyimpan row dan col nya ke array l
#Jika tidak ada sel yang kosong sudoku selesai
#Ketika menemukan sel yang kosong, program akan ciba memasukan nilai 1 sampai 9 ke dalam sel
#Di setiap pengecekan, program akan mengecek setiap row, col, dan block (3x3)
#Jika di semua percobaan (1 sampai 9) terjadi kegagalan, maka program akan melakukan backtracking
#Backtracking dilakukan dengan kembali ke sel yang kosong sebelumnya dan mengecek kemungkinan lain untuk mengisi sel kosong tersebut
#Back tracking akan dilakukan sampai sudoku penuh
def solve_sudoku(board):
     
    # 'l' is a list that stores rows and cols in find_empty_location Function
    l=[0,0]
     
    # What does this 'if' block check?
    # ANS apakah semua sel sudah terisi
    # What will happen if the program enters the following 'if' block?
    # ANS program akan mencari apakah masih ada sel yang kosong
    if(not find_empty_location(board, l)):
        # In what way does this True value affect the program?
        # ANS saat sudoku sudah terisi semua maka solve_sudoku akan berhenti
        return True

    # Assigning list values to row and col that we got from the above Function 
    row=l[0]
    col=l[1]

    # What does this block do?
    # ANS mencoba memasukan nilai pada sel yang kosong
    for num in range(1,10):
        if is_valid(board, row, col, num):
            board[row][col]=num

            # What does this 'if' section check?
            # ANS mengecek apakah angka num tersebut sudah dipakai di row,col, dan block
            if solve_sudoku(board):
                return True
 
            # Else it fails, undo 
            board[row][col] = 0
             
    # What is this False value for? Will this function always return False?
    # ANS false berarti kemungkinan jawaban yang kita coba salah dan akan memulai kemungkinan selanjutanya dari sel tertentu
    # Tidak, karena ketika kemungkinan jawaban kita benar (suatu nilai tidak muncul 2 kali dalam row,col, dan block) akan mereturn true
    return False


# Driver main function to test above functions
if __name__=="__main__":
    # What is this 'if' for?
    # ANS untuk memastikan module berjalan hanya untuk program sendirian bukan untuk diimport ke module lain
    # Is there any other way to check and handle error like this without using 'if else'?
    # ANS
    # What does the value of len(sys.argv) represent?
    # ANS Menghitung jumlah argument
    if len(sys.argv) < 3:
        print "Error: ..."
    else:
        board = [[0 for i in range(9)] for j in range(9)]

        # What is sys.argv[1]?
        # ANS argumen pertama yang dimasukan ke program yaitu problemfilename
        read_from_file(sys.argv[1], board)

        print "Your board:"
        print_board(board)
        print "-----------------"

        if solve_sudoku(board):
            print "Solution:"
            print_board(board)
            save_board(sys.argv[2], board)
        else:
            print "No solution found"