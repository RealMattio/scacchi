from Pezzo import Pezzo

class Alfiere(Pezzo):
    """L'alfiere si puo' muovere in diagonale per un numero di caselle pari a quelle disponibili. Cattura occupando la
    posizione della pedina avversaria"""

    #costruttore
    def __init__(self, colore, posizione=None):
        super().__init__(colore, posizione, 'Alfiere')
        self.graphic_rep = '\u2657' if self.colore == 'W' else '\u265D'

    def verifica_mossa(self, destinazione):
        if super().verifica_mossa(destinazione):  # le condizioni generiche sono verificate
            #verifica che la destinazione sia in diagonale alla posizione
            if abs(ord(self.posizione[0])-ord(destinazione[0]))==abs(self.posizione[1]-destinazione[1]):
                #verifica che non ci sono pezzi in mezzo
                first = ord(self.posizione[0]) + 1 if ord(self.posizione[0]) + 1 < ord(destinazione[0]) else ord(destinazione[0]) + 1  # prima colonna da esaminare
                last = ord(destinazione[0]) if ord(self.posizione[0]) + 1 < ord(destinazione[0]) else ord(self.posizione[0])

                firstc = self.posizione[1] + 1 if self.posizione[1] + 1 < destinazione[1] else destinazione[1] + 1  # prima riga da esaminare
                lastc = destinazione[1] if self.posizione[1] + 1 < destinazione[1] else self.posizione[1]  # ultma riga da esaminare
                r=range(first, last)
                s=range(firstc,lastc)
                for col in r:
                    i=r.index(col)
                    if not self.scacchiera.get_pezzo([chr(col), s[i]]) == None:  # la casella è occupata
                        print(f"La mossa non è legale perché è presente un pezzo ({self.scacchiera.get_pezzo([chr(col), s[i]]).nome}) nella casella {chr(col)}{s[i]}")
                        return False
                return True
            else:
                print(f"La mossa {self.posizione[0]}{self.posizione[1]}, {destinazione[0]}{destinazione[1]} non è legale per l'Alfiere")
                return False
        else:
            print(f"La mossa {self.posizione[0]}{self.posizione[1]}, {destinazione[0]}{destinazione[1]} non è legale per l'Alfiere")
            return False

