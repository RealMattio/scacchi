from Pezzo import Pezzo
from Alfiere import Alfiere
from Cavallo import Cavallo
from Regina import Regina
from Torre import Torre
from Scacchiera import Scacchiera

class Pedone(Pezzo):

    def __init__(self, colore, posizione=None):
        super().__init__(colore, posizione, 'Pedone',)
        self.graphic_rep = '\u2659' if self.colore == 'W' else '\u265F'


    def verifica_mossa(self, destinazione):
        if super().verifica_mossa(destinazione):
            dest=self.possibili_posizioni()
            if destinazione in dest:
                return True
            else:
                print(f'La mossa {self.posizione[0]}{self.posizione[1]}, {destinazione[0]}{destinazione[1]} non è legale per il Pedone')
                return False
        else:
            print(f'La mossa {self.posizione[0]}{self.posizione[1]}, {destinazione[0]}{destinazione[1]} non è legale per il Pedone')
            return False
    #il pedone si leva e mette una nuova pedina!

    def possibili_posizioni(self):
        poss=[]
        if self.colore=='W':
            if(self.posizione[0]=='A'):
                poss.append([self.posizione[0], self.posizione[1] + 1])
                s=[chr(ord(self.posizione[0])+1),self.posizione[1]+1]
                if not self.scacchiera.get_pezzo(s)==None and self.scacchiera.get_pezzo(s).colore != self.colore:
                    poss.append([chr(ord(self.posizione[0])+1),self.posizione[1]+1])
            elif(self.posizione[0]=='H'):
                poss.append([self.posizione[0], self.posizione[1] + 1])
                s=[chr(ord(self.posizione[0]) - 1), self.posizione[1] + 1]
                if not self.scacchiera.get_pezzo(s)==None and self.scacchiera.get_pezzo(s).colore != self.colore:
                    poss.append([chr(ord(self.posizione[0])-1),self.posizione[1]+1])
            else:
                poss.append([self.posizione[0], self.posizione[1] + 1])
                s1=[chr(ord(self.posizione[0]) + 1), self.posizione[1] + 1]
                s2=[chr(ord(self.posizione[0]) - 1), self.posizione[1] + 1]
                if not self.scacchiera.get_pezzo(s1)==None and self.scacchiera.get_pezzo(s1).colore != self.colore:
                    poss.append([chr(ord(self.posizione[0])+1),self.posizione[1]+1])
                if not self.scacchiera.get_pezzo(s2)==None and self.scacchiera.get_pezzo(s2).colore != self.colore:
                    poss.append([chr(ord(self.posizione[0])-1),self.posizione[1]+1])
            return poss
        else:
            if (self.posizione[0] == 'A'):
                poss.append([self.posizione[0], self.posizione[1] - 1])
                s = [chr(ord(self.posizione[0]) + 1), self.posizione[1] - 1]
                if not self.scacchiera.get_pezzo(s) == None and self.scacchiera.get_pezzo(s).colore != self.colore:
                    poss.append([chr(ord(self.posizione[0]) + 1), self.posizione[1] - 1])
            elif (self.posizione[0] == 'H'):
                poss.append([self.posizione[0], self.posizione[1] - 1])
                s = [chr(ord(self.posizione[0]) - 1), self.posizione[1] - 1]
                if not self.scacchiera.get_pezzo(s) == None and self.scacchiera.get_pezzo(s).colore != self.colore:
                    poss.append([chr(ord(self.posizione[0]) - 1), self.posizione[1] - 1])
            else:
                poss.append([self.posizione[0], self.posizione[1] - 1])
                s1 = [chr(ord(self.posizione[0]) + 1), self.posizione[1] - 1]
                s2 = [chr(ord(self.posizione[0]) - 1), self.posizione[1] - 1]
                if not self.scacchiera.get_pezzo(s1) == None and self.scacchiera.get_pezzo(s1).colore != self.colore:
                    poss.append([chr(ord(self.posizione[0]) + 1), self.posizione[1] - 1])
                if not self.scacchiera.get_pezzo(s2) == None and self.scacchiera.get_pezzo(s2).colore != self.colore:
                    poss.append([chr(ord(self.posizione[0]) - 1), self.posizione[1] - 1])
            return poss
