from katalogas.irasas import Irasas


class Islaidos(Irasas):
    def __init__(self, suma, atsiskaitymo_metodas, preke_paslauga):
        super().__init__(suma)
        self.atsiskaitymo_metodas = atsiskaitymo_metodas
        self.preke_paslauga = preke_paslauga
