from tkinter import *;
import tkinter as tk;

class TicTacToe():
    def __init__(self, O=0, X=0):
        # Variables
        self.O = O; self.X = X; self.root = Tk(); self.Oturn = False; self.Xturn = False; self.letter = ''; self.spots = []; self.spotLetter = []; self.winner = False;
        self.winConditions = [
        ('button1', 'button4', 'button7'), ('button2', 'button5', 'button8'), ('button3', 'button6', 'button9'),
        ('button1', 'button2', 'button3'), ('button4', 'button5', 'button6'), ('button7', 'button8', 'button9'),
        ('button1', 'button5', 'button9'),('button3', 'button5', 'button7')
        ];

    def update(self):
        truth = True; self.Oturn = False; self.Xturn = False;
        if self.O == self.X and truth == True: # O's turn/update
            self.O += 1; truth = False; self.Oturn = True; self.letter = 'O';
        if self.O != self.X and truth == True: # X's turn/update
            self.X += 1; truth = False; self.Xturn = True; self.letter = 'X';

    def mainMethod(self, ButtonNum='', Xcord=0, Ycord=0):
        vars()[ButtonNum] = Label(self.root, bg='White', bd=0, text=self.letter, font=('arial', 42)); vars()[ButtonNum].place(width=150, height=150, x=Xcord, y=Ycord);
        self.spots.append(ButtonNum); self.spotLetter.append(self.letter);

    def winning(self):
        for i in self.winConditions:
            if i[0] in self.spots and i[1] in self.spots and i[2] in self.spots:
                index1 = self.spots.index(i[0]); index2 = self.spots.index(i[1]); index3 = self.spots.index(i[2]);
                if self.spotLetter[index1] == self.spotLetter[index2] and self.spotLetter[index2] == self.spotLetter[index3]:
                    self.winner = True;
                    winnerLabel = Label(self.root, bg='White', bd=4, relief='solid', text=(str(self.spotLetter[index1]) + ' is the winner!'), font=('arial', 18, 'bold', )); winnerLabel.place(width=190, height=45, x=130, y=1);


def MainFunc():

    tic=TicTacToe();
    # Main Window Setup
    tic.root.geometry('460x460'); tic.root.title("TicTacToe"); tic.root.maxsize(width=460, height=460); tic.root.minsize(width=460, height=460); photo = PhotoImage(file = 'tictactoe2.png'); tic.root.iconphoto(False,  photo);
    # Buttons
    button1 = Button(tic.root, bg='White', bd=0, cursor="plus", command=lambda:[tic.update(), tic.mainMethod(ButtonNum='button1', Xcord=1, Ycord=1), tic.winning()]); button1.place(width=150, height=150, x=1, y=1);
    button2 = Button(tic.root, bg='White', bd=0, cursor="plus", command=lambda:[tic.update(), tic.mainMethod(ButtonNum='button2', Xcord=155, Ycord=1), tic.winning()]); button2.place(width=150, height=150, x=155, y=1);
    button3 = Button(tic.root, bg='White', bd=0, cursor="plus", command=lambda:[tic.update(), tic.mainMethod(ButtonNum='button3', Xcord=310, Ycord=1), tic.winning()]); button3.place(width=150, height=150, x=310, y=1);
    button4 = Button(tic.root, bg='White', bd=0, cursor="plus", command=lambda:[tic.update(), tic.mainMethod(ButtonNum='button4', Xcord=1, Ycord=155), tic.winning()]); button4.place(width=150, height=150, x=1, y=155);
    button5 = Button(tic.root, bg='White', bd=0, cursor="plus", command=lambda:[tic.update(), tic.mainMethod(ButtonNum='button5', Xcord=155, Ycord=155), tic.winning()]); button5.place(width=150, height=150, x=155, y=155);
    button6 = Button(tic.root, bg='White', bd=0, cursor="plus", command=lambda:[tic.update(), tic.mainMethod(ButtonNum='button6', Xcord=310, Ycord=155), tic.winning()]); button6.place(width=150, height=150, x=310, y=155);
    button7 = Button(tic.root, bg='White', bd=0, cursor="plus", command=lambda:[tic.update(), tic.mainMethod(ButtonNum='button7', Xcord=1, Ycord=310), tic.winning()]); button7.place(width=150, height=150, x=1, y=310);
    button8 = Button(tic.root, bg='White', bd=0, cursor="plus", command=lambda:[tic.update(), tic.mainMethod(ButtonNum='button8', Xcord=155, Ycord=310), tic.winning()]); button8.place(width=150, height=150, x=155, y=310);
    button9 = Button(tic.root, bg='White', bd=0, cursor="plus", command=lambda:[tic.update(), tic.mainMethod(ButtonNum='button9', Xcord=310, Ycord=310), tic.winning()]); button9.place(width=150, height=150, x=310, y=310);
    # Lines
    line1 = Canvas(tic.root, width=5, height=460, bg='Black'); line1.place(width=10, height=470, x=150, y=0);
    line2 = Canvas(tic.root, width=5, height=460, bg='Black'); line2.place(width=10, height=470, x=300, y=0);
    line3 = Canvas(tic.root, width=5, height=460, bg='Black'); line3.place(width=470, height=10, x=0, y=150);
    line4 = Canvas(tic.root, width=5, height=460, bg='Black'); line4.place(width=470, height=10, x=0, y=300);

    tic.root.mainloop();

MainFunc();
