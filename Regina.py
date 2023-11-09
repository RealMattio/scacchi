import Pezzo from Pezzo

class Regina(Pezzo):
    """La regina si puo muovere in ogni direzione verticale e orizzontale di quante caselle vuole"""

    def __init__(self, colore, posizione=None):
        super().__init__(colore, posizione, 'Regina')
        self.graphic_rep = '\u2655' if self.colore == 'W' else '\u265B'

    def verifica_mossa(self, destinazione):
        if super().verifica_mossa():

        else:
            print(f"La mossa {self.posizione[0]}{self.posizione[1]}, {destinazione[0]}{destinazione[1]} non è valida per la Regina")
            return False


    def calcolaDestinazioni(self):
        dest=[]

        for row in range(1,9):
            if not self.posizione[1]==row:
                dest.append([self.posizione[0], row])
        for col in range(ord('A'),ord('H')+1):
            if not self.posizione[0]==chr(col):
                dest.append([chr(col), self.posizione[1]])