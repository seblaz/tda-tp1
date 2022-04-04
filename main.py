#!/usr/bin/env python3
import sys

from src.model import Antena, calcular_contratos, NoHayResultado


def leer_antenas(nombre_de_archivo):
    antenas = []
    with open(nombre_de_archivo) as f:
        for line in f:
            nro, posicion, radio = line.split(",")
            antenas.append(Antena(float(posicion), float(radio), nro))
    return antenas


def main():
    antenas = leer_antenas(sys.argv[2])
    try:
        contratadas = calcular_contratos(antenas, float(sys.argv[1]))
        print(",".join(map(lambda antena: antena.nro_de_contrato, contratadas)))
    except NoHayResultado:
        print("No se encontró un resultado posible")


if __name__ == '__main__':
    main()
