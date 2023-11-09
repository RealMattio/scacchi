from Pezzo import Pezzo

class Regina(Pezzo):
    """La regina si puo muovere in ogni direzione verticale e orizzontale di quante caselle vuole"""

    def __init__(self, colore, posizione=None):
        super().__init__(colore, posizione, 'Regina')
        self.graphic_rep = '\u2655' if self.colore == 'W' else '\u265B'

    def verifica_mossa(self, destinazione):
        if super().verifica_mossa(destinazione):
            poss_dest=self.calcolaDestinazioni()
            if destinazione in poss_dest:
                #se la mossa e' fatibile dalla regina passo a controllare che non ci sia nessun pezzo nel tragitto
                if self.posizione[0]==destinazione[0] or self.posizione[1]==destinazione[1]: #se la destinazione e' sulla stessa riga o sulla stessa colonna eseguo i controlli della torre
                    #controllo posizione uguale alla torre, vedi Torre.py per maggiorni dettagli
                    if self.posizione[0] == destinazione[0]:
                        first = self.posizione[1] + 1 if self.posizione[1] + 1 < destinazione[1] else destinazione[1] + 1
                        last = destinazione[1] if self.posizione[1] + 1 < destinazione[1] else self.posizione[1]
                        for riga in range(first, last):
                            if not self.scacchiera.get_pezzo([destinazione[0], riga]) == None:
                                print(f"La mossa non è legale perché è presente un pezzo ({self.scacchiera.get_pezzo([destinazione[0], riga]).nome}) nella casella {destinazione[0]}{riga}")
                                return False
                        return True
                    elif self.posizione[1] == destinazione[1]:
                        first = ord(self.posizione[0]) + 1 if ord(self.posizione[0]) + 1 < ord(destinazione[0]) else ord(destinazione[0]) + 1
                        last = ord(destinazione[0]) if ord(self.posizione[0]) + 1 < ord(destinazione[0]) else ord(self.posizione[0])
                        for col in range(first, last):
                            if not self.scacchiera.get_pezzo([chr(col), destinazione[1]]) == None:  # la casella è occupata
                                print(f"La mossa non è legale perché è presente un pezzo ({self.scacchiera.get_pezzo([chr(col), destinazione[1]]).nome}) nella casella {chr(col)}{destinazione[1]}")
                                return False
                        return True
                else: #se la destinazione non e' in orizzontale o verticale allora faccio i controlli dell'alfiere
                    #controlli dell'alfiere, vedi Alfiere.py per maggiori dettagli
                    first = ord(self.posizione[0]) + 1 if ord(self.posizione[0]) + 1 < ord(destinazione[0]) else ord(destinazione[0]) + 1  # prima colonna da esaminare
                    last = ord(destinazione[0]) if ord(self.posizione[0]) + 1 < ord(destinazione[0]) else ord(self.posizione[0])
                    firstc = self.posizione[1] + 1 if self.posizione[1] + 1 < destinazione[1] else destinazione[1] + 1  # prima riga da esaminare
                    lastc = destinazione[1] if self.posizione[1] + 1 < destinazione[1] else self.posizione[1]  # ultma riga da esaminare
                    r = range(first, last)
                    s = range(firstc, lastc)
                    for col in r:
                        i = r.index(col)
                        if not self.scacchiera.get_pezzo([chr(col), s[i]]) == None:  # la casella è occupata
                            print(f"La mossa non è legale perché è presente un pezzo ({self.scacchiera.get_pezzo([chr(col), s[i]]).nome}) nella casella {chr(col)}{s[i]}")
                            return False
                    return True
            else:
                print(f"La mossa {self.posizione[0]}{self.posizione[1]}, {destinazione[0]}{destinazione[1]} non è legale per la Regina")
                return False
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
        for col in range(ord("A"),ord('H')+1):
            for row in range(1,9):
                if abs(ord(self.posizione[0]) - col) == abs(self.posizione[1] - row):
                    dest.append([chr(col), row])
        return dest