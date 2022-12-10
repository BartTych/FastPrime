
import numpy as np

class LiczbyPierwsze:

    def __init__(self):
        self.scierzka = ""
        self.ListaLiczb = []
        self.ilosc_liczb = 0

    def policz_liczby(self,ilosc_liczb, scierzka):
        self.scierzka = scierzka
        self.ilosc_liczb = ilosc_liczb
        self._import_data(self.scierzka)
        return self._procedura_liczenia_liczb()

    @staticmethod
    def zapiszwynik( wynik, wielkoscSekcji, scierzka):
        licznik=0
        f = open(scierzka, "w")
        for i in wynik:
            f.write(str(i) + '\n')
        f.close()

    def _procedura_liczenia_liczb(self):
        liczba = self.ListaLiczb[-1] + 1
        while (len(self.ListaLiczb)< self.ilosc_liczb):
            k = int(np.sqrt(liczba)) + 1
            #k = self.ListaLiczb[-1]
            for i in range(len(self.ListaLiczb)):

                if  liczba % self.ListaLiczb[i] == 0:
                    liczba += 1
                    break
                if self.ListaLiczb[i] >= k :
                    self.ListaLiczb.append(liczba)
                    liczba += 1
                    break

    def _import_data(self, file):

        Listaliczb2 = open(file).read()
        Listaliczb2 = Listaliczb2.splitlines()
        print(len(Listaliczb2))
        Listaliczb3 = [int(n) for n in Listaliczb2]
        self.ListaLiczb = Listaliczb3
