# -*- coding: utf-8 -*-

from visual import *

# Diccionario que simula la tabla periódica con los elementos elegidos (solo se usaron elementos con valencias definidas)
# Recupera elementos claves como el número de valencia, el color para el dibujo
# y el número de electrones requeridos para alcanzar la estabilidad para cada elemento
elements = {
    "H" :
    {
        "Name" : "Hidrogeno",
        "Atomic Number" : 1,
        "Valence" : 1,
        "Stability" : [2],
        "Color" : color.white
    },

    "Li" :
    {
        "Name" : "Litio",
        "Atomic Number" : 3,
        "Valence" : 1,
        "Stability" : [8],
        "Color" : (0.15, 1.0, 0.65)
    },

    "Be" :
    {
        "Name" : "Berilio",
        "Atomic Number" : 4,
        "Valence" : 2,
        "Stability" : [4,8],
        "Color"     : (0.34, 0.34, 1.0)
    },

    "B" :
    {
        "Name" : "Boro",
        "Atomic Number" : 5,
        "Valence" : 3,
        "Stability" : [6,8] ,
        "Color"     : (0.03, 0.03, 0.15)
    },

    "C" :
    {
        "Name" : "Carbono",
        "Atomic Number" : 6,
        "Valence" : 4,
        "Stability" : [8]  ,
        "Color" : (1.0, 0.2549, 0.2549 )
    },

    "N" :
    {
        "Name" : "Nitrogeno",
        "Atomic Number" : 7,
        "Valence" : 5,
        "Stability" : [8],
        "Color" : color.orange
    },

    "O" :
    {
        "Name" : "Oxigeno",
        "Atomic Number" : 8,
        "Valence" : 6,
        "Stability" : [8]  ,
        "Color": (0.156,0.517,0.723)
    },

    "F" :
    {
        "Name" : "Fluor",
        "Atomic Number" : 9,
        "Valence" : 7,
        "Stability" : [8],
        "Color" : (0.862, 0.078, 0.235)
    },

    "Na" :
    {
        "Name" : "Sodio",
        "Atomic Number" : 11,
        "Valence" : 1,
        "Stability" : [8],
        "Color" : (0.823, 0.411, 0.117)
    },

    "Mg" :
    {
        "Name" : "Magnesio",
        "Atomic Number" : 12,
        "Valence" : 2,
        "Stability" : [8],
        "Color" : (1, 0.549, 0)
    },

    "Al" :
    {
        "Name" : "Aluminio",
        "Atomic Number" : 13,
        "Valence" : 3,
        "Stability" : [8],
        "Color": (0.117, 0.564, 1)
    },

    "Si" :
    {
        "Name" : "Silicio",
        "Atomic Number" : 14,
        "Valence" : 4,
        "Stability" : [8]   ,
        "Color" : (0.368,0.526,1.000)
    },

    "P" :
    {
        "Name" : "Fosforo",
        "Atomic Number" : 15,
        "Valence" : 5,
        "Stability" : [8, 10, 12]    ,
        "Color" : (0, 0.392, 0)

    },

    "S" :
    {
        "Name" : "Sulfuro",
        "Atomic Number" : 16,
        "Valence" : 6,
        "Stability" : [8, 10, 12],
        "Color": (0.803, 0.360, 0.360)
    },

    "Cl" :
    {
        "Name" : "Cloro",
        "Atomic Number" : 17,
        "Valence" : 7,
        "Stability" : [8, 10] ,
        "Color" : (0, 0.545, 0.545)
    },

    "K" :
    {
        "Name" : "Potasio",
        "Atomic Number" : 19,
        "Valence" : 1,
        "Stability" : [8]   ,
        "Color" : (0.8, 0.8, 0)
    },

    "Ca" :
    {
        "Name" : "Calcio",
        "Atomic Number" : 20,
        "Valence" : 2,
        "Stability" : [8],
        "Color" : (0, 0.807, 0.858)
    },

    "Ga" :
    {
        "Name" : "Galio",
        "Atomic Number" : 31,
        "Valence" : 3,
        "Stability" : [8],
        "Color" : color.green
    },

    "Ge" :
    {
        "Name" : "Germanio",
        "Atomic Number" : 32,
        "Valence" : 4,
        "Stability" : [8],
        "Color" : (0.332, 0.646, 0.546)
    },

    "As" :
    {
        "Name" : "Arsenico",
        "Atomic Number" : 33,
        "Valence" : 5,
        "Stability" : [8, 10],
        "Color" : (0.552, 0.743, 0.123)
    },

    "Se" :
    {
        "Name" : "Selenium",
        "Atomic Number" : 34,
        "Valence" : 6,
        "Stability" : [8, 10],
        "Color" : (0.452, 0.123, 0.478)
    },

    "Br" :
    {
        "Name" : "Bromo",
        "Atomic Number" : 35,
        "Valence" : 7,
        "Stability" : [8, 10, 12],
        "Color" : (0.556, 0.231, 0.223)
    },

    "Rb" :
    {
        "Name" : "Rubidio",
        "Atomic Number" : 37,
        "Valence" : 1,
        "Stability" : [8],
        "Color" : (0.142, 0.828, 0.653)
    },

    "Sr" :
    {
        "Name" : "Estroncio",
        "Atomic Number" : 38,
        "Valence" : 2,
        "Stability" : [8],
        "Color" : (0.223, 0.666, 0.222)
    },

    "In" :
    {
        "Name" : "Indio",
        "Atomic Number" : 49,
        "Valence" : 3,
        "Stability" : [8],
        "Color" : (0.533, 0.232, 0.222)
    },

    "Sn" :
    {
        "Name" : "Estano",
        "Atomic Number" : 50,
        "Valence" : 4,
        "Stability" : [8],
        "Color" : (0.523, 0.111, 0.876)
    },

    "Sb" :
    {
        "Name" : "Antimonio",
        "Atomic Number" : 51,
        "Valence" : 5,
        "Stability" : [8, 10],
        "Color" : (0.823, 0.621, 0.422)
    },

    "Te" :
    {
        "Name" : "Telurio",
        "Atomic Number" : 52,
        "Valence" : 6,
        "Stability" : [8, 10, 12],
        "Color" : (0.333, 0.555, 0.111)
    },

    "I" :
    {
        "Name" : "Yodo",
        "Atomic Number" : 53,
        "Valence" : 7,
        "Stability" : [8, 10, 14],
        "Color" : (0.196, 0.803, 0.196)
    },

    "Cs" :
    {
        "Name" : "Cesio",
        "Atomic Number" : 55,
        "Valence" : 1,
        "Stability" : [8],
        "Color" : (0.885, 0.234, 0.543)
    },

    "Ba" :
    {
        "Name" : "Bario",
        "Atomic Number" : 56,
        "Valence" : 2,
        "Stability" : [8],
        "Color" : (0.433, 0.776, 0.222)
    },

    "Tl" :
    {
        "Name" : "Talio",
        "Atomic Number" : 81,
        "Valence" : 3,
        "Stability" : [8],
        "Color" : (0.665, 0.122, 0.655)
    },

    "Pb" :
    {
        "Name" : "Plomo",
        "Atomic Number" : 82,
        "Valence" : 4,
        "Stability" : [8],
        "Color" : (0.43, 0.55, 0.1234)
    },

    "Bi" :
    {
        "Name" : "Bismuto",
        "Atomic Number" : 83,
        "Valence" : 5,
        "Stability" : [8, 10],
        "Color" : (0.234, 0.123, 0.858)
    },

    "Po" :
    {
        "Name" : "Polonio",
        "Atomic Number" : 84,
        "Valence" : 6,
        "Stability" : [8, 10, 12],
        "Color" : (0.576, 0.439, 0.858)
    },

    "At" :
    {
        "Name" : "Astato",
        "Atomic Number" : 85,
        "Valence" : 7,
        "Stability" : [8],
        "Color" : (0.780, 0.082, 0.521)
    },

    "Fr" :
    {
        "Name" : "Francio",
        "Atomic Number" : 87,
        "Valence" : 1,
        "Stability" : [8],
        "Color" : (0, 0, 0.545)
    },

    "Ra" :
    {
        "Name" : "Radio",
        "Atomic Number" : 88,
        "Valence" : 2,
        "Stability" : [8]      ,
        "Color" : (0.478, 0.086, 0.243)
    }

}

