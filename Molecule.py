# -*- coding: utf-8 -*-

from Elements import elements

from enum import Enum


# Tipos de geometrías disponibles
class Geometry(Enum):
    UNDEFINED          = 0
    LINEAR             = 1
    TRIGONAL           = 2
    TETRAHEDRAL        = 3
    TRIGONALPYRAMIDAL  = 4
    SQUAREPLANAR       = 5
    SQUAREPYRAMIDAL    = 6
    SEESAW             = 7
    TSHAPE             = 8
    OCTAHEDRAL         = 9
    BENT               = 10
    PENTAGONAL         = 11
    LONE               = 12


# Clase usada para almacenar datos básicos de las moléculas que se quieren graficar:
# Elemento central, elemento acompañante, número de pares enlazados del elemento central
# número de pares no enlazados, geometría, color...

class Molecule( object ):

    def __init__(self, central, bonded, numBonded):
        self.central        = central        # Símbolo del átomo central de la molécula
        self.bonded         = bonded         # Símbolo de elemento enlazado
        self.numBonded      = numBonded      # Cantidad de enlaces asociados
        self.bonding_pairs  = 0              # Cantidad de pares enlazados
        self.lone_pairs     = 0              # Cantidad de pares no enlazados
        self.geometry       = None           # Geometría de la molécula
        self.central_color  = None
        self.bonded_color   = None
        self.valence = elements[self.central]["Valence"]
        self.setMol()


    # Establecer el número de pares no enlazados, se necesita para calcular la geometría
    def setLone(self):
        num = elements[self.central]["Valence"]        # Se recupera la valencia del átomo central
        self.lone_pairs = ( num - self.numBonded ) / 2 # Obtiene la cantidad de pares no enlazados
                                                       # restando a los electrones de valencia disponibles
                                                       # el número de enlaces asociados y dividiéndolos por 2

    def setBonding(self):
        num = elements[self.central]["Valence"]
        self.bonding_pairs = ( self.numBonded )


    def setGeometry(self):                             # Se define la geometría de la molécula con base en el número
        bonding = self.bonding_pairs                   # de pares enlazados y no enlazados
        lone    = self.lone_pairs
        if( bonding == 2 and lone == 0 ):
            self.geometry = Geometry.LINEAR
        elif( bonding == 3 and lone == 0 ):
            self.geometry = Geometry.TRIGONAL
        elif( bonding == 2 and lone == 2 ):
            self.geometry = Geometry.BENT
        elif( bonding == 4 and lone == 0 ):
            self.geometry = Geometry.TETRAHEDRAL
        elif( bonding == 3 and lone == 1 ):
            self.geometry = Geometry.TRIGONALPYRAMIDAL
        elif( bonding == 4 and lone == 1 ):
            self.geometry = Geometry.SEESAW
        elif( bonding == 3 and lone == 2):
            self.geometry = Geometry.TSHAPE
        elif( bonding == 6 and lone == 0 ):
            self.geometry = Geometry.OCTAHEDRAL
        elif( bonding == 5 and lone == 1 ):
            self.geometry = Geometry.SQUAREPYRAMIDAL
        elif( bonding == 4 and lone == 2 ):
            self.geometry = Geometry.SQUAREPLANAR
        elif( bonding == 7 and lone == 0 ):
            self.geometry = Geometry.PENTAGONAL
        elif( bonding == 0):
            self.geometry = Geometry.LONE
        else:
            self.geometry = Geometry.UNDEFINED

    def setColors(self):                                         # Recupera el color correspondiente a cada elemento para el gráfico
        self.central_color = elements[self.central]["Color"]
        self.bonded_color = elements[self.bonded]["Color"]


    def setMol(self):                                           # Inicializa el resto de los atributos
        self.setBonding()
        self.setLone()
        self.setGeometry()
        self.setColors()

    def printInfo(self):                                        # Imprime información de molécula: usado para debuggear
        print( "Elemento central: "   + str(self.central))
        print( "Elemento de enlace: " + str(self.bonded ))
        print( "Numero de enlaces: "  + str(self.numBonded))
        print( "Pares enlazados: "    + str(self.bonding_pairs))
        print( "Pares no enlazados: " + str(self.lone_pairs))
        print( "La geometría es: "    + str(self.geometry))



