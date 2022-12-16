from katalogas.pajamos import Pajamos
from katalogas.islaidos import Islaidos


class Biudzetas:
    def __init__(self):
        self.israsai = []

    def pajamos(self, suma, siuntejas, info):
        pajamu_irasas = Pajamos(suma, siuntejas, info)
        self.israsai.append(pajamu_irasas)

    def islaidos(self, suma, atsiskaitymo_metodas, preke_paslauga):
        islaidu_irasas = Islaidos(suma, atsiskaitymo_metodas, preke_paslauga)
        self.israsai.append(islaidu_irasas)

    def biudzeto_balansas(self):
        balansas = 0
        for irasas in self.israsai:
            if isinstance(irasas, Pajamos):
                balansas += irasas.suma
            if isinstance(irasas, Islaidos):
                balansas -= irasas.suma
        return balansas

    def ataskaita(self):
        for irasas in self.israsai:
            if isinstance(irasas, Pajamos):
                print(f"Pajamos: {irasas.suma} {irasas.siuntejas} {irasas.info}")
            if isinstance(irasas, Islaidos):
                print(f"Išlaidos: {irasas.suma} {irasas.atsiskaitymo_metodas} {irasas.preke_paslauga}")
