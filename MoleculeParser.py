# -*- coding: utf-8 -*-
from MolValidator import *
from Molecule import *
from Graph import *


import ply.lex as lex
import ply.yacc as yacc


# Lexer
tokens = (
    'MODEL'  ,
    'ELEMENT',
    'NUMBER' ,
    'BOND'   ,
    'LCURL'  ,
    'RCURL'
    )

# Expresiones regulares asociadas a los tokens
t_MODEL   = r'(spaceFill|line|stickBall)'
t_ELEMENT = r'(Br|Mg|Li|Pb|Si|As|Sn|Rb|Sb|Po|Se|Be|Fr|Sr|Tl|Ba|Cl|Ca|Te|Al|Ge|At|Ga|Na|Cs|Bi|Ra|B|C|F|S|H|K|O|P|I|N)'
t_BOND    = r'-'
t_LCURL   = r'{'
t_RCURL   = r'}'


# Función para retornar el valor numeral correspondiente al encontrar el token número
def t_NUMBER(t):
    r'[1-9]'
    t.value = int(t.value)
    return t

# Función para ignorar tabulaciones y espacios en blanco en toda ocasión
t_ignore  = ' \t'

# Función para hacer el conteo de líneas, probablemente no se use
def t_newline(t):
    r'\n'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Símbolo '%s' no aceptado" % t.value[0])
    t.lexer.skip(1)
lex.lex()


# Prueba léxica
#lex.input(" spaceFill{ CH3- AlNa3(CO2)2-OH2  }")
#for tok in iter(lex.token, None):
    #rint repr(tok.type), repr(tok.value)


# -------------Variable global que almacena todas las moléculas con sus estructuras -------------------------------------
global chain
chain = []                                                                                                                    #|
# -----------------------------------------------------------------------------------------------------------------------|

#Parser y reglas sintácticas

#Gramática usada
# S -> A { L }
# A -> MODEL
# L -> B
# B -> ELEMENT
# B -> ELEMENT ELEMENT NUMBER
# B -> ELEMENT ELEMENT NUMBER BOND B


# Regla que maneja el modelo del gráfico 3D. Hay 3 opciones:
# 1. Modelo de líneas (line)
# 2. Modelo de esferas(spaceFill)
# 3. Modelo de líneas y esferas (stickBall)
# p_model recibe el tipo de modelo así como la lista (chain) que almecena
# los objetos molecule con la información necesaria para
# realizar el dibujo
def p_model(p):
    '''S : A LCURL L RCURL'''
    p[0] = p[3]
    draw3D( p[1], p[3])

# Se recupera el tipo de modelo 3D
def p_modeltype(p):
    '''A : MODEL '''
    p[0] = p[1]

# Se recupera la lista de objetos "Molecule"
def p_list(p):
    '''L : B'''
    p[0] = chain

# Caso que contempla que se ingrese solo el símbolo de un elemento, aislado.
# Se dibujará el átomo junto con sus electrones de valencia.
# Solo en este modelo se da esto.
# En p_lone, p_central y p_centralBonded se da la creación de un objeto Molecule
# con la información recibida de la hilera de entrada.
def p_lone(p):
    '''B : ELEMENT'''
    p[0] = p[1]
    central = p[1]
    mol = Molecule(central, central, 0)
    chain.append(mol)

# Caso que contempla un elemento central con solo un tipo de elemento a su alrededor (sin contar algún enlace)
# Se hace una validación semántica tomando en cuenta el número de valencia del átomo central y el
# Si hay enlaces al lado izquierdo ( p[-1] ) entonces se agrega uno a la cantidad de enlaces formados por el
# átomo central.
def p_central(p):
    '''B : ELEMENT ELEMENT NUMBER'''
    p[0] = ( p[1] , p[2] ,  p[3] )

    bonds = 0
    if( p[-1] == "-"):
        lbond = True
    else:
        lbond = False
    if( lbond ): bonds += 1

    bonds += p[3]

    central    = p[1]
    bonded     = p[2]
    mol = Molecule(central, bonded, bonds)     # Se crea objeto Molecule y se enlaza a "chain"
    chain.append(mol)                          # Esta lista se pasa a la clase Graph.py para que llame a los métodos de graficación

    if not ( validateOctect( p[1], bonds )):
        raise ValueError("No se cumple con el octeto")
    if not ( validateBondOctect( p[2]) ):
        raise ValueError("No se cumple con el octeto")


def p_centralBonded(p):
    '''B : ELEMENT ELEMENT NUMBER BOND B'''

    p[0] = ( p[1] , p[2] ,  p[3], p[4], p[5] )

    bonds = 1 # empieza en 1 pues ya se está tomando en cuenta el enlace de la derecha
    if( p[-1] == "-"):
        lbond = True
    else:
        lbond = False
    if( lbond ): bonds += 1

    bonds += p[3]

    central    = p[1]
    bonded     = p[2]

    mol = Molecule(central, bonded, bonds)
    chain.append(mol)
    assert validateOctect( p[1], bonds)
    if not ( validateOctect( p[1], bonds) ):
        raise ValueError("No se cumple con el octeto en átomo central")
    if not ( validateBondOctect( p[2]) ):
        raise ValueError("No se cumple con el octeto")




def p_error(p):
    print("Error sintáctico en la entrada")


yacc.yacc()

# Casos de Prueba exitosos -----------------------------------------------------

# 1.
data = "stickBall { SeF3-CH2-IF5-NH1-SF4-TeCl4-CH3 }"
# 2.
# data = "spaceFill{ BiH3 }"
# 3.
#data = "stickBall { CH3-PCl1-SF5 }"
# 4.
# data = "stickBall { I }"
# 5.
# data = "line{ BiF2 - CH2 - OF1  }"

# Casos de Prueba fracasados ---------------------------------------------------
# 1.
# data = "spaceFill{ -ClF-O- }"            #-------> Error sintáctico
# 2.
# data = "spaceFill{ FH1 - CH2 - AtF1  }" # ------> Error semántico, no cumple el octeto
# 3.
# data = "line { FeH2 }"                  #-------> Error léxico


# Acción principal que finalmente realiza el parsing de la hilera recibida
yacc.parse(data)





