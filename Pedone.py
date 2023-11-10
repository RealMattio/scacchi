from Pezzo import Pezzo
from Alfiere import Alfiere
from Cavallo import Cavallo
from Regina import Regina
from Torre import Torre

class Pedone(Pezzo):

    def __init__(self, colore, posizione=None):
        super().__init__(colore, posizione, 'Cavallo')
        self.graphic_rep = '\u2659' if self.colore == 'W' else '\u265F'


    #il pedone si leva e mette una nuova pedina!

    def possibili_posizioni(self):
        poss=[]
        if(self.posizione[0]=='A'):
            variabile=1;
        elif(self.posizione[0]=='H'):

        else:
