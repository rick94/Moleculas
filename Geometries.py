# -*- coding: utf-8 -*-

from visual import *
# Variables globales usadas para las dimensiones de los gráficos, posterior

rad = 8

radb = 8

cyl = 1

global stickColor

stickColor = (0.827, 0.827, 0.827)


#ball  = sphere(pos = scene.center, radius = 8, color =  (0.60, 0, 0.18))
#stick = cylinder(pos = ball.pos, axis=(20,20,0), radius = 1, color = color.white)
#ball2  = sphere(pos = scene.center, radius = 8, color =  (0.60, 0, 0.18))

def setInitialValues(vrad, vradb, vstick, ball, ball2,  stick):
    global rad
    rad = vrad
    global radb
    radb = vradb
    global cyl
    cyl = vstick
    ball.radius = vrad
    ball2.radius = vradb
    stick.radius = vstick

# Método para obtener un vector aleatorio, ortogonal al v dado
def perpendicular_vector(v):
    if (v.x == 0) and (v.y == 0):
        if (v.z == 0):

            raise ValueError('zero vector')

        # v is Vector(0, 0, v.z)
        return vector(0, 1, 0)

    return vector(-v.y, v.x, 0)

# Métodos de Reajuste de ángulos debido a la distorsión causada por el cambio de eje
# Sirven para los ejes "rectos" puede haber fallo al darse alguna inclinación
# No se hará esfuerzo por arreglar dichos fallos pues se requiere de más conocimiento
# en álgebra vectorial y que no es parte del curso, sin embargo se espera una visualización
# correcta en la mayoría de casos.

# Reajustar ángulos de geometría trigonal
def adjustAnglesTrig( tup ):

    bond1 = tup[0]
    bond2 = tup[1]

    bond1.axis = rotate( bond1.axis, radians(180))
    bond2.axis = rotate( bond2.axis, radians(180))

    if ( degrees (diff_angle(bond1.axis,bond2.axis)) < 120 ):
        v = perpendicular_vector(bond1.axis)
        bond1.axis = bond2.axis
        bond1.axis = rotate( bond1.axis, radians(180), v)
        bond2.axis = bond1.axis
        bond2.axis = rotate( bond2.axis, radians(60))
        bond1.axis = bond2.axis
        bond1.axis = rotate( bond2.axis, radians(260))

# Reajustar ángulos de geometría en T
def adjustAnglesTshaped( tup ):
    bond1 = tup[0]
    bond2 = tup[1]

    bond1.axis = rotate( bond1.axis, radians(180))
    bond2.axis = rotate( bond2.axis, radians(180))

    if ( degrees (diff_angle(bond2.axis,bond1.axis)) < 90):

         v = perpendicular_vector( bond2.axis )
         bond2.axis = rotate( bond2.axis, radians(90), v)

def adjustAnglesTrigPyd( tup ):

    bond1 = tup[0]
    bond2 = tup[1]

    bond1.axis = rotate( bond1.axis, radians(180))
    bond2.axis = rotate( bond2.axis, radians(180))




# Reajustar ángulos de geometría tetraédrica
rotc = 0
def adjustAnglesTetra( tup ):

    bond1 = tup[0]
    bond2 = tup[1]
    bond3 = tup[2]
    bond  = tup[3]

    v = perpendicular_vector( bond1.axis)
    bond1.axis = rotate( bond1.axis, radians(180))
    bond2.axis = rotate( bond2.axis, radians(180))
    bond3.axis = rotate( bond3.axis, radians(180))
    # aún con reajuste hay ocasiones o ángulo en los que se deba de reajustar la geometría nuevamente
    # esto se hace en todos los métodos de reajuste
    if ( degrees (diff_angle(bond2.axis,bond1.axis)) > 102):
         bond1.axis = rotate( bond1.axis, radians(70.5),v)
         bond2.axis = bond1.axis
         bond2.axis = rotate( bond2.axis, radians(109.5))
         bond3.axis = bond2.axis
         bond3.axis = rotate( bond3.axis, radians(109.5))
    global rotc
    if rotc % 2 == 0:
        bond1.axis = rotate( bond1.axis, radians(141))
        bond2.axis = rotate( bond2.axis, radians(-109.5))
        bond3.axis = rotate( bond3.axis, radians(-109.5))
    rotc += 1

# Reajustar ángulos de geometría lineal
def adjustAnglesLinear( tup ):
    bond1 = tup

    bond1.axis = rotate( bond1.axis, radians(180))

# Reajustar ángulos de geometría doblada
def adjustAnglesBent( tup ):
    bond1 = tup[0]
    bond  = tup[1]

    bond1.axis = rotate( bond1.axis, radians(180))
    if( degrees (diff_angle(bond1.axis,bond.axis)) < 10):
        v = perpendicular_vector( bond1.axis)
        bond1.axis = rotate( bond1.axis, radians(60), v)

# Reajustar ángulos de geometría de balancín
def adjustAnglesSeeSaw( tup ):
    bond1 = tup[0]
    bond2 = tup[1]
    bond3 = tup[2]

    v = perpendicular_vector( bond1.axis)
    bond1.axis = rotate( bond1.axis, radians(180))
    bond2.axis = rotate( bond2.axis, radians(90))
    bond3.axis = rotate( bond3.axis, radians(90),v)
    if( degrees (diff_angle(bond2.axis,bond3.axis)) < 30):
        bond3.axis = rotate( bond3.axis, radians(90))

# Reajuste geometría pirámide cuadrangular
def adjustAnglesSquarePyramidal( tup ):
    bond1 = tup[0]
    bond2 = tup[1]
    bond3 = tup[2]
    bond4 = tup[3]

    bond1.axis = rotate( bond1.axis, radians(180))
    bond2.axis = rotate( bond2.axis, radians(180))
    bond3.axis = rotate( bond3.axis, radians(180))
    bond4.axis = rotate( bond4.axis, radians(180))

# Reajuste geometría cuadrada plana
def adjustAnglesSquarePlanar ( tup ):
    bond1 = tup[0]
    bond2 = tup[1]
    bond3 = tup[2]

    bond1.axis = rotate( bond1.axis, radians(180))
    bond2.axis = rotate( bond2.axis, radians(180))
    bond3.axis = rotate( bond3.axis, radians(180))

# Reajuste geometría octahédrica
def adjustAnglesOctahedral( tup ):
    bond1 = tup[0]
    bond2 = tup[1]
    bond3 = tup[2]
    bond4 = tup[3]
    bond5 = tup[4]

    bond1.axis = rotate( bond1.axis, radians(180))
    bond2.axis = rotate( bond2.axis, radians(180))
    bond3.axis = rotate( bond3.axis, radians(180))
    bond4.axis = rotate( bond4.axis, radians(180))
    bond5.axis = rotate( bond3.axis, radians(180))

    if ( degrees (diff_angle(bond3.axis,bond5.axis)) < 180):
        v = perpendicular_vector( bond1.axis)
        bond3.axis = rotate( bond3.axis, radians(270), v)
        bond5.axis = rotate( bond5.axis, radians(90), v)

# Reajuste geometría bipirámide pentagonal
def adjustAnglesPentagonal ( tup):
    bond1 = tup[0]
    bond2 = tup[1]
    bond3 = tup[2]
    bond4 = tup[3]
    bond5 = tup[4]
    bond6 = tup[5]

    bond1.axis = rotate( bond1.axis, radians(180))
    v = perpendicular_vector( bond1.axis)
    v = perpendicular_vector( v )
    bond2.axis = bond1.axis
    bond2.axis = rotate( bond2.axis, radians(90))
    bond3.axis = bond2.axis
    bond3.axis = rotate( bond3.axis, radians(72),v)
    bond4.axis = bond3.axis
    bond4.axis = rotate( bond4.axis, radians(72),v)
    bond5.axis = bond4.axis
    bond5.axis = rotate( bond5.axis, radians(72),v)


# Método clave: Se encarga de "enlazar" las dos esferas proporcionadas con el cilindro dado
# simulando la unión de dos átomos mediante un enlace. No se distingue si es un enlace simple
# doble o triple
def attach(sphere1, sphere2, cilinder):
    sX = sphere1.pos.x;
    aX = cilinder.axis.x;
    sY = sphere1.pos.y;
    aY = cilinder.axis.y;
    sZ = sphere1.pos.z;
    aZ = cilinder.axis.z;
    sPos = vector(sX + aX, sY + aY, sZ + aZ)
    sphere2.pos = sPos

# Métodos de formación de geometrías: Todos reciben de parámetro una esfera (átomo) y un cilindro
# (enlace). A partir de estos dos elementos se crean los átomos y enlaces necesarios para formar
# la geometría alrededor de la esfera dada que actúa como átomo central de la molécula en específico.


def lone(sphere1, bond, colors):
    sphere1.color = colors[0]
    sphere1.radius = 30
    bond.visible = False

    val = colors[2]


    r = vector (25, 25, 25)
    text(text='Elemento', align='center', depth=-0.3, color=color.blue, pos = (30, 0, 0))
    v = perpendicular_vector( r )
    for i in range( val ):
        electron = sphere (display = scene, pos = r ,radius = 2, material = materials.chrome, color = color.white )
        r = rotate(r, radians(360 / val), v)




    return (sphere1, bond)


# Geometría lineal, ejemplo: CO2
def attachLinear(sphere1, bond, first, colors):

    sphere1.color = colors[0]
    sphere1.radius = rad
    sphere2 = sphere (radius = radb, color = colors[1])

    bond1 = cylinder (pos = sphere1.pos, axis = bond.axis, radius = cyl, color = stickColor)

    v = perpendicular_vector(bond.axis)
    bond1.axis = rotate(bond.axis, radians(180))

    if ( first == False ):
        tup = ( bond1 )
        adjustAnglesLinear(tup)

    attach(sphere1, sphere2, bond1)

    return (sphere2, bond1)

# Geometría angular doblada, ejemplo: SO2
def attachBent( sphere1, bond, first, colors):
    sphere1.color = colors[0]
    sphere1.radius = rad

    sphere2 = sphere (radius = radb, color = colors[1])

    bond1 = cylinder (pos = sphere1.pos, axis = bond.axis, radius = cyl, color = stickColor)

    v = perpendicular_vector(bond.axis)

    bond1.axis = rotate(bond.axis, radians(120))

    if (first == False):
        tup = ( bond1 , bond)
        adjustAnglesBent (tup)

    attach(sphere1, sphere2, bond1)

    return (sphere2, bond1)

# Geometría tetrahédrica, ejemplo: CH4
def attachTetrahedron( sphere1, bond, first, colors):
    sphere1.color = colors[0]
    sphere1.radius = rad

    sphere2 = sphere (radius = radb, color = colors[1])
    sphere3 = sphere (radius = radb, color = colors[1])
    sphere4 = sphere (radius = radb, color = colors[1])

    bond1 = cylinder (pos = sphere1.pos, axis = bond.axis, radius = cyl, color = stickColor)
    bond2 = cylinder (pos = sphere1.pos, axis = bond.axis, radius = cyl, color = stickColor)
    bond3 = cylinder (pos = sphere1.pos, axis = bond.axis, radius = cyl, color = stickColor)

    v = perpendicular_vector(bond.axis)
    bond1.axis = rotate(bond.axis, radians(109.5))
    bond2.axis = rotate(bond2.axis, radians(54.75))
    v = perpendicular_vector(bond2.axis)
    bond2.axis = rotate(bond2.axis, radians(109.5), v)
    bond3.axis = bond2.axis
    bond3.axis = rotate(bond3.axis, radians(109.5), v )

    if (first == False):
        tup = (bond1, bond2, bond3, bond)
        adjustAnglesTetra( tup )

    attach(sphere1, sphere2, bond1)
    attach(sphere1, sphere3, bond2)
    attach(sphere1, sphere4, bond3)


    return (sphere2, bond1)

# Geometría Tetraedro piramidal, ejemplo: PCl3
def attachTrigonalPyramidal( sphere1, bond, first, colors):
    sphere1.color = colors[0]
    sphere1.radius = rad

    sphere2 = sphere (radius = radb, color = colors[1])
    sphere3 = sphere (radius = radb, color = colors[1])

    bond1 = cylinder (pos = sphere1.pos, axis = bond.axis, radius = cyl, color = stickColor)
    bond2 = cylinder (pos = sphere1.pos, axis = bond.axis, radius = cyl, color = stickColor)

    v = perpendicular_vector(bond.axis)
    bond1.axis = rotate(bond.axis, radians(109.5))
    bond2.axis = rotate(bond2.axis, radians(54.75))
    v = perpendicular_vector(bond2.axis)
    bond2.axis = rotate(bond2.axis, radians(109.5), v)


    if (first == False):
        tup = (bond1, bond2)
        adjustAnglesTrigPyd( tup )

    attach(sphere1, sphere2, bond1)
    attach(sphere1, sphere3, bond2)

    return (sphere2, bond1)

# Geometría trigonal plana, ejemplo: SO3
def attachTrigonal( sphere1, bond, first, colors):
    sphere1.color = colors[0]
    sphere1.radius = rad

    sphere2 = sphere (radius = radb, color = colors[1])
    sphere3 = sphere (radius = radb, color = colors[1])

    bond1 = cylinder (pos = sphere1.pos, axis = bond.axis, radius = cyl, color = stickColor)
    bond2 = cylinder (pos = sphere1.pos, axis = bond.axis, radius = cyl, color = stickColor)

    bond1.axis =  rotate(bond1.axis, radians(120) )
    bond2.axis = bond1.axis
    bond2.axis = rotate(bond2.axis, radians(120))

    if (first == False):
        tup = ( bond1, bond2 )
        adjustAnglesTrig (tup)

    attach(sphere1, sphere2, bond1)
    attach(sphere1, sphere3, bond2)

    return (sphere2, bond1)
# Geometría en T, ejemplo: ClF3
def attachTshaped( sphere1, bond, first, colors):
    sphere1.color = colors[0]
    sphere1.radius = rad

    sphere2 = sphere (radius = radb, color = colors[1])
    sphere3 = sphere (radius = radb, color = colors[1])

    bond1 = cylinder (pos = sphere1.pos, axis = bond.axis, radius = cyl, color = stickColor)
    bond2 = cylinder (pos = sphere1.pos, axis = bond.axis, radius = cyl, color = stickColor)

    v = perpendicular_vector(bond.axis)
    bond1.axis = rotate(bond.axis, radians(180))
    bond2.axis = bond1.axis
    bond2.axis = rotate(bond2.axis, radians(90))

    if (first == False):
        tup = ( bond1, bond2 )
        adjustAnglesTshaped (tup)

    attach(sphere1, sphere2, bond1)
    attach(sphere1, sphere3, bond2)

    return (sphere2, bond1)

# Geometría de balancín, ejemplo: SF4
def attachSeeSaw( sphere1, bond, first , colors):
    sphere1.color = colors[0]
    sphere1.radius = rad

    sphere2 = sphere (radius = radb, color = colors[1])
    sphere3 = sphere (radius = radb, color = colors[1])
    sphere4 = sphere (radius = radb, color = colors[1])

    bond1 = cylinder (pos = sphere1.pos, axis = bond.axis, radius = cyl, color = stickColor)
    bond2 = cylinder (pos = sphere1.pos, axis = bond.axis, radius = cyl, color = stickColor)
    bond3 = cylinder (pos = sphere1.pos, axis = bond.axis, radius = cyl, color = stickColor)

    v = perpendicular_vector(bond.axis)
    bond1.axis = rotate(bond.axis, radians(180))
    bond2.axis = bond1.axis
    bond2.axis = rotate(bond2.axis, radians(90))
    v = perpendicular_vector(bond2.axis)
    bond2.axis = rotate(bond2.axis, radians(90), v)
    bond3.axis = bond2.axis
    bond3.axis = rotate(bond3.axis, radians(90), v)

    if (first == False):
        tup = (bond1, bond2, bond3)
        adjustAnglesSeeSaw( tup )

    attach(sphere1, sphere2, bond1)
    attach(sphere1, sphere3, bond2)
    attach(sphere1, sphere4, bond3)

    return (sphere2, bond1)

# Geometría octahédrica, ejemplo: SF6
def attachOctahedral( sphere1, bond, first, colors ):
    sphere1.color = colors[0]
    sphere1.radius = rad

    sphere2 = sphere (radius = radb, color = colors[1])
    sphere3 = sphere (radius = radb, color = colors[1])
    sphere4 = sphere (radius = radb, color = colors[1])
    sphere5 = sphere (radius = radb, color = colors[1])
    sphere6 = sphere (radius = radb, color = colors[1])

    bond1 = cylinder (pos = sphere1.pos, axis = bond.axis, radius = cyl, color = stickColor)
    bond2 = cylinder (pos = sphere1.pos, axis = bond.axis, radius = cyl, color = stickColor)
    bond3 = cylinder (pos = sphere1.pos, axis = bond.axis, radius = cyl, color = stickColor)
    bond4 = cylinder (pos = sphere1.pos, axis = bond.axis, radius = cyl, color = stickColor)
    bond5 = cylinder (pos = sphere1.pos, axis = bond.axis, radius = cyl, color = stickColor)

    v = perpendicular_vector(bond.axis)
    bond1.axis = rotate(bond.axis, radians(180))
    bond2.axis = bond1.axis
    bond2.axis = rotate(bond2.axis, radians(90))
    v = perpendicular_vector(bond2.axis)
    bond2.axis = rotate(bond2.axis, radians(90), v)
    bond3.axis = bond2.axis
    bond3.axis = rotate(bond3.axis, radians(90), v)
    bond4.axis = bond3.axis
    bond4.axis = rotate(bond4.axis, radians(90), v)
    bond5.axis = bond4.axis
    bond5.axis = rotate(bond5.axis, radians(90), v)

    if (first == False):
        tup = (bond1, bond2, bond3, bond4, bond5)
        adjustAnglesOctahedral( tup )

    attach(sphere1, sphere2, bond1)
    attach(sphere1, sphere3, bond2)
    attach(sphere1, sphere4, bond3)
    attach(sphere1, sphere5, bond4)
    attach(sphere1, sphere6, bond5)

    return (sphere2, bond1)

# Geometría cuadrada planar, ejemplo:
def attachSquarePlanar( sphere1, bond, first , colors):
    sphere1.color = colors[0]
    sphere1.radius = rad
    sphere2 = sphere (radius = radb, color = colors[1] )
    sphere3 = sphere (radius = radb, color = colors[1] )
    sphere4 = sphere (radius = radb, color = colors[1] )

    bond1 = cylinder (pos = sphere1.pos, axis = bond.axis, radius = cyl, color = stickColor)
    bond2 = cylinder (pos = sphere1.pos, axis = bond.axis, radius = cyl, color = stickColor)
    bond3 = cylinder (pos = sphere1.pos, axis = bond.axis, radius = cyl, color = stickColor)

    v = perpendicular_vector(bond.axis)
    bond1.axis = rotate(bond.axis, radians(180))
    bond2.axis = bond1.axis
    bond2.axis = rotate(bond2.axis, radians(90))
    v = perpendicular_vector(bond2.axis)
    bond2.axis = rotate(bond2.axis, radians(90), v)
    bond3.axis = bond2.axis
    bond3.axis = rotate(bond3.axis, radians(180), v)

    if (first == False):
        tup = (bond1, bond2, bond3)
        adjustAnglesSquarePlanar( tup )

    attach(sphere1, sphere2, bond1)
    attach(sphere1, sphere3, bond2)
    attach(sphere1, sphere4, bond3)

    return (sphere2, bond1)

# Geometría pirámide cuadrada, ejemplo: BrF5
def attachSquarePyramidal( sphere1, bond, first, colors ):
    sphere1.color = colors[0]
    sphere1.radius = rad

    sphere2 = sphere (radius = radb, color = colors[1])
    sphere3 = sphere (radius = radb, color = colors[1])
    sphere4 = sphere (radius = radb, color = colors[1])
    sphere5 = sphere (radius = radb, color = colors[1])

    bond1 = cylinder (pos = sphere1.pos, axis = bond.axis, radius = cyl, color = stickColor)
    bond2 = cylinder (pos = sphere1.pos, axis = bond.axis, radius = cyl, color = stickColor)
    bond3 = cylinder (pos = sphere1.pos, axis = bond.axis, radius = cyl, color = stickColor)
    bond4 = cylinder (pos = sphere1.pos, axis = bond.axis, radius = cyl, color = stickColor)

    v = perpendicular_vector(bond.axis)
    bond1.axis = rotate(bond.axis, radians(180))
    bond2.axis = bond1.axis
    bond2.axis = rotate(bond2.axis, radians(90))
    v = perpendicular_vector(bond2.axis)
    bond2.axis = rotate(bond2.axis, radians(90), v)
    bond3.axis = bond2.axis
    bond3.axis = rotate(bond3.axis, radians(90), v)
    bond4.axis = bond3.axis
    bond4.axis = rotate(bond4.axis, radians(90), v)

    if (first == False):
        tup = (bond1, bond2, bond3, bond4)
        adjustAnglesSquarePyramidal( tup )

    attach(sphere1, sphere2, bond1)
    attach(sphere1, sphere3, bond2)
    attach(sphere1, sphere4, bond3)
    attach(sphere1, sphere5, bond4)

    return (sphere2, bond1)

# Geometría bipirámide pentagonal, ejemplo: IF7
def attachPentagonal( sphere1, bond, first, colors ):
    sphere1.color = colors[0]
    sphere1.radius = rad

    sphere2 = sphere (radius = radb, color = colors[1])
    sphere3 = sphere (radius = radb, color = colors[1])
    sphere4 = sphere (radius = radb, color = colors[1])
    sphere5 = sphere (radius = radb, color = colors[1])
    sphere6 = sphere (radius = radb, color = colors[1])
    sphere7 = sphere (radius = radb, color = colors[1])

    bond1 = cylinder (pos = sphere1.pos, axis = bond.axis, radius = cyl, color = stickColor)
    bond2 = cylinder (pos = sphere1.pos, axis = bond.axis, radius = cyl, color = stickColor)
    bond3 = cylinder (pos = sphere1.pos, axis = bond.axis, radius = cyl, color = stickColor)
    bond4 = cylinder (pos = sphere1.pos, axis = bond.axis, radius = cyl, color = stickColor)
    bond5 = cylinder (pos = sphere1.pos, axis = bond.axis, radius = cyl, color = stickColor)
    bond6 = cylinder (pos = sphere1.pos, axis = bond.axis, radius = cyl, color = stickColor)

    v = perpendicular_vector(bond.axis)
    bond1.axis = rotate(bond.axis, radians(180))
    bond2.axis = bond1.axis
    bond2.axis = rotate(bond2.axis, radians(90), v)
    v = perpendicular_vector(bond2.axis)
    bond2.axis = rotate(bond2.axis, radians(72), v)
    bond3.axis = bond2.axis
    bond3.axis = rotate(bond3.axis, radians(72), v)
    bond4.axis = bond3.axis
    bond4.axis = rotate(bond4.axis, radians(72), v)
    bond5.axis = bond4.axis
    bond5.axis = rotate(bond5.axis, radians(72), v)
    bond6.axis = bond5.axis
    bond6.axis = rotate(bond6.axis, radians(72), v)

    if (first == False):
        tup = (bond1, bond2, bond3, bond4, bond5, bond6)
        adjustAnglesPentagonal( tup )

    attach(sphere1, sphere2, bond1)
    attach(sphere1, sphere3, bond2)
    attach(sphere1, sphere4, bond3)
    attach(sphere1, sphere5, bond4)
    attach(sphere1, sphere6, bond5)
    attach(sphere1, sphere7, bond6)

    return (sphere2, bond1)

s = sphere(color=color.cyan)




