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
                #trasformazione in nuovo pezzo
                if self.colore=='W':
                    if destinazione[1]==8:
                        self.trasformaPedone(destinazione)
                else:
                    if destinazione[1]==1:
                        self.trasformaPedone(destinazione)
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
            poss.append([self.posizione[0], self.posizione[1]+1])
            if self.posizione[1]==2:
                poss.append([self.posizione[0], self.posizione[1]+2])
            if(self.posizione[0]=='A'):
                posiz_da_ver=[chr(ord(self.posizione[0])+1),self.posizione[1]+1]
                if not self.scacchiera.get_pezzo(posiz_da_ver)==None and self.scacchiera.get_pezzo(posiz_da_ver).colore != self.colore:
                    poss.append(posiz_da_ver)
            elif(self.posizione[0]=='H'):
                posiz_da_ver=[chr(ord(self.posizione[0]) - 1), self.posizione[1] + 1]
                if not self.scacchiera.get_pezzo(posiz_da_ver)==None and self.scacchiera.get_pezzo(posiz_da_ver).colore != self.colore:
                    poss.append(posiz_da_ver)
            else:
                posiz_da_ver1=[chr(ord(self.posizione[0]) + 1), self.posizione[1] + 1]
                posiz_da_ver2=[chr(ord(self.posizione[0]) - 1), self.posizione[1] + 1]
                if not self.scacchiera.get_pezzo(posiz_da_ver1)==None and self.scacchiera.get_pezzo(posiz_da_ver1).colore != self.colore:
                    poss.append(posiz_da_ver1)
                if not self.scacchiera.get_pezzo(posiz_da_ver2)==None and self.scacchiera.get_pezzo(posiz_da_ver2).colore != self.colore:
                    poss.append(posiz_da_ver2)
            return poss
        else:
            poss.append([self.posizione[0], self.posizione[1] - 1])
            if self.posizione[1]==7:
                poss.append([self.posizione[0], self.posizione[1]-2])
            if (self.posizione[0] == 'A'):
                posiz_da_ver = [chr(ord(self.posizione[0]) + 1), self.posizione[1] - 1]
                if not self.scacchiera.get_pezzo(posiz_da_ver) == None and self.scacchiera.get_pezzo(posiz_da_ver).colore != self.colore:
                    poss.append(posiz_da_ver)
            elif (self.posizione[0] == 'H'):
                posiz_da_ver = [chr(ord(self.posizione[0]) - 1), self.posizione[1] - 1]
                if not self.scacchiera.get_pezzo(posiz_da_ver) == None and self.scacchiera.get_pezzo(posiz_da_ver).colore != self.colore:
                    poss.append(posiz_da_ver)
            else:
                posiz_da_ver1 = [chr(ord(self.posizione[0]) + 1), self.posizione[1] - 1]
                posiz_da_ver2 = [chr(ord(self.posizione[0]) - 1), self.posizione[1] - 1]
                if not self.scacchiera.get_pezzo(posiz_da_ver1) == None and self.scacchiera.get_pezzo(posiz_da_ver1).colore != self.colore:
                    poss.append(posiz_da_ver1)
                if not self.scacchiera.get_pezzo(posiz_da_ver2) == None and self.scacchiera.get_pezzo(posiz_da_ver2).colore != self.colore:
                    poss.append(posiz_da_ver2)
            return poss

    def trasformaPedone(self, destinazione):
        check=True
        x=int(input('Specifica in che pezzo vuoi trasmormare il Pedone:\n1 = Regina;\n2 = Alfiere;\n3 = Cavallo;\n4 = Torre;\nInserisci un numero da 1 a 4: '))
        while check:
            if x==1:
                self.scacchiera.metti(Regina(self.colore),destinazione)
                self.scacchiera.togli(self.posizione)
                check=False
            elif x==2:
                self.scacchiera.metti(Alfiere(self.colore), destinazione)
                self.scacchiera.togli(self.posizione)
                check = False
            elif x==3:
                self.scacchiera.metti(Cavallo(self.colore), destinazione)
                self.scacchiera.togli(self.posizione)
                check = False
            elif x==4:
                self.scacchiera.metti(Torre(self.colore), destinazione)
                self.scacchiera.togli(self.posizione)
                check = False
            else:
                print("E' stato inserito un input errato, inserirne uno valido")

