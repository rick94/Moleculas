# -*- coding: utf-8 -*-
from Geometries import *
from Molecule import *

# Módulo encargado de llamar a las funciones graficas de Geometries.py, dependiendo de la información
# que se encuentre en los objetos de clase "Molecule" recibidos desde MoleculeParser.py

# Figuras iniciales a partir de las cuales se van a construir las geometrías
ball   = sphere(pos = scene.center, radius = 8, color =  (0.196, 0.803, 0.196))
ball1  = sphere(pos = scene.center, radius = 8, color =  (0.60, 0, 0.18))
stick  = cylinder(pos = ball.pos, axis=(20,20,0), radius = 1, color = (0.827, 0.827, 0.827))
attach(ball, ball1, stick)

# Elige la geometría a agregar a la estructura ya dibujada, dependiendo de la geometría definida
# en el objeto Molecule
def defineGeometry( geom , atom, bond, time, colors):
    if  ( geom == Geometry.LINEAR):
        lastbond = attachLinear(atom, bond, time, colors)
    elif( geom == Geometry.TRIGONAL):
        lastbond = attachTrigonal(atom, bond, time, colors)
    elif( geom == Geometry.BENT):
        lastbond = attachBent(atom, bond, time, colors)
    elif( geom == Geometry.TETRAHEDRAL):
        lastbond = attachTetrahedron(atom, bond, time, colors)
    elif( geom == Geometry.SQUAREPLANAR):
        lastbond = attachSquarePlanar(atom, bond, time, colors)
    elif( geom == Geometry.SQUAREPYRAMIDAL):
        lastbond = attachSquarePyramidal(atom, bond, time, colors)
    elif( geom == Geometry.SEESAW):
        lastbond = attachSeeSaw(atom, bond, time, colors)
    elif( geom == Geometry.OCTAHEDRAL):
        lastbond = attachOctahedral(atom, bond, time, colors)
    elif( geom == Geometry.PENTAGONAL):
        lastbond = attachPentagonal(atom, bond, time, colors)
    elif( geom == Geometry.TRIGONALPYRAMIDAL):
        lastbond = attachTrigonalPyramidal(atom, bond, time, colors)
    elif( geom == Geometry.TSHAPE):
        lastbond = attachTshaped(atom, bond, time, colors)
    elif( geom == Geometry.LONE):
        lastbond = lone(atom, bond, colors)

    return lastbond

# Decide el modelo 3D que se va a dibujar y llama a defineGeometry para ya graficarlo
def draw3D( type, chain):
    if(  type == "spaceFill"):
        setInitialValues( 30 , 17, 1, ball, ball1, stick )
    elif( type == "stickBall"):
        setInitialValues( 8 , 8, 1,  ball, ball1, stick )
    elif( type == "line"):
        setInitialValues( 12 ,8, 8 , ball, ball1, stick )

    global lastbond
    lastbon = ()
    for mol in chain:                                                 # Recorre la cadena de objetos Molecule para ir graficando cada molécula una por una
        colors = ( mol.central_color, mol.bonded_color , mol.valence) # con su geometría respectiva

        if( chain.index(mol) == 0):
            ball1.color = mol.bonded_color
            if(mol.geometry == Geometry.LONE): ball1.visible = False
            lastbond = defineGeometry(mol.geometry,ball, stick, 1, colors) # se recupera el último enlace y último átomo de la molécula anterior
        else:                                                              # esto para adherir la la nueva geometría a partir de estos elementos
            ball2 = lastbond[0]
            stick2 = lastbond[1]
            lastbond = defineGeometry(mol.geometry,ball2, stick2, 0, colors )


