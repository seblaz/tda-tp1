class Antena:
    """
    Representa una antena que podría ser colocada en la ruta.
    """

    def __init__(self, kilometro, radio, nro_de_contrato):
        self.kilometro = kilometro
        self.radio = radio
        self.nro_de_contrato = nro_de_contrato

    def kilometro_inicial(self):
        return self.kilometro - self.radio

    def kilometro_final(self):
        return self.kilometro + self.radio

    def posterior_a(self, kilometro):
        return kilometro < self.kilometro_inicial()

    def anterior_a(self, kilometro):
        return self.kilometro_final() < kilometro

    def cubre_mas_kilometros(self, otra):
        return self.kilometro_final() > otra.kilometro_final()


class NoHayResultado(Exception):
    pass


def calcular_contratos(antenas, longitud_de_ruta):
    antenas.sort(key=lambda antena: antena.kilometro_inicial())
    antenas_contratadas = []
    antenas_evaluadas = 0

    while posicion_actual(antenas_contratadas) < longitud_de_ruta:
        antenas_evaluadas += mejor_nro_de_antena_para(
            posicion_actual(antenas_contratadas),
            antenas[antenas_evaluadas:]
        )
        antenas_contratadas.append(antenas[antenas_evaluadas])
        antenas_evaluadas += 1

    return antenas_contratadas


def posicion_actual(antenas):
    return 0 if len(antenas) == 0 else antenas[-1].kilometro_final()


def mejor_nro_de_antena_para(posicion, antenas):
    """
    Recibe una posicion (en kilometros) y una lista ordenada de antenas.
    Devuelve el número de antena que cubre más kilómetros para la posición.
    Eleva una excepción de tipo NoHayResultado en caso de que no encuentre una
    antena posible para la posción.
    """
    mejor_antena = None
    for nro, antena in enumerate(antenas):
        if antena.anterior_a(posicion):
            continue
        if antena.posterior_a(posicion):
            break
        if mejor_antena is None or antena.cubre_mas_kilometros(antenas[mejor_antena]):
            mejor_antena = nro

    if mejor_antena is None:
        raise NoHayResultado()
    return mejor_antena
