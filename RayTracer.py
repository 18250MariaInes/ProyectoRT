"""
Maria Ines Vasquez Figueroa
18250
Gráficas
DR3 Planes & Cubes
Main
"""

from gl import Raytracer, color
from obj import Obj, Texture, Envmap
from sphere import *


brick = Material(diffuse = color(0.8, 0.25, 0.25 ), spec = 16)
stone = Material(diffuse = color(0.4, 0.4, 0.4 ), spec = 32)
grass = Material(diffuse = color(0.5, 1, 0), spec = 32)
glass = Material(diffuse = color(0.25, 1, 1), spec = 64)
coal = Material(diffuse = color(0.15,0.15,0.15), spec = 32)
snow = Material(diffuse = color(1, 1, 1), spec = 64)
carrot=Material(diffuse = color(1, 0.54, 0), spec = 64)
eyes=Material(diffuse = color(0.90, 0.90, 0.90),spec = 64)

pink_center=Material(diffuse = color(0.976, 0.38, 1),spec = 64)
pink_bow=Material(diffuse = color(0.984, 0.6, 1), spec = 64)
christmas_green=Material(diffuse= color(0, 0.82, 0.01),spec = 64)
christmas_base=Material(diffuse= color(0.53, 0.29, 0),spec = 64)
mirror = Material( spec = 64, matType = REFLECTIVE)

red_bow=Material(diffuse = color(1, 0, 0.01),spec = 64)



width = 512
height = 256
r = Raytracer(width,height)
r.glClearColor(0.2, 0.6, 0.8)
r.glClear()
r.envmap = Envmap('snowp.bmp')
r.pointLight = PointLight(position = (0,0,0), intensity = 1)
r.ambientLight = AmbientLight(strength = 0.1)

"""r.scene.append( Sphere(( 1, 1, -8), 1.5, brick) )
r.scene.append( Sphere(( 0, 0, -5), 0.5, stone) )
r.scene.append( Sphere((-3, 3, -10),  2, mirror) )
r.scene.append( Sphere((-3, -1.5, -10), 1.5, mirror) )"""
#cuarto
"""r.scene.append( Plane((0, -3, 0), (0,1,0), stone) )
r.scene.append( Plane((0, 3, 0), (0,1,0), stone) )
r.scene.append( Plane((0, 0, -10), (0,0,1), stone) )
r.scene.append( Plane(( -3,0, 0), (1,0,0), stone) )
r.scene.append( Plane(( 3, 0,0), (1,0,0), stone) )"""
#cubos
"""r.scene.append( AABB((1.5, -1, -5), 0.8, carrot ) )
r.scene.append( AABB((-1.5, -1, -5), 0.8, pink_center ) )"""
"""r.scene.append( AABB(V3(1.5, -1.5, -5), 1.5, mirror ) )
r.scene.append( AABB(V3(-1.5, -1.5, -5), 1.5, glass ) )"""
r.scene.append(Pyramid([(-6, -2, -10), (-4, 1.8, -5), (-10, -2, -10), (-4, -1, -7.5)], christmas_green))
r.scene.append( AABB((-3.8, -1.5, -5), (0.5,1.07,0.5), christmas_base ) )
#gift1
r.scene.append( AABB((-2, -1.5, -5), (1,1,1), christmas_green ) )
r.scene.append( Sphere((-1.90, -0.805,  -4.6), 0.16, red_bow) )
r.scene.append( Sphere((-2, -0.8,  -4.5), 0.13, red_bow) )
r.scene.append( Sphere((-2.10, -0.805,  -4.6), 0.16, red_bow) )
#gift2
r.scene.append( AABB((0, -1.5, -5), (1,1,1), carrot ) )
r.scene.append( Sphere((-0.10, -0.805,  -4.6), 0.16, red_bow) )
r.scene.append( Sphere((0, -0.8,  -4.5), 0.13, red_bow) )
r.scene.append( Sphere((0.10, -0.805,  -4.6), 0.16, red_bow) )
#gift3
r.scene.append( AABB((2, -1.5, -5), (1,1,1), pink_center ) )
r.scene.append( Sphere((1.90, -0.805,  -4.6), 0.16, red_bow) )
r.scene.append( Sphere((2, -0.8,  -4.5), 0.13, red_bow) )
r.scene.append( Sphere((2.10, -0.805,  -4.6), 0.16,red_bow) )
#globo de nieve
r.scene.append( Sphere(( -1, -1.5, -5), 0.4, mirror) )
r.scene.append( AABB((-1, -1.8, -5), (0.5,0.5,0.5), christmas_base ) )
#guirnalda
r.scene.append( Sphere((-5, 2.4,  -5), 0.3, red_bow) )
r.scene.append( Sphere((-4, 2.2,  -5), 0.3, christmas_green) )
r.scene.append( Sphere((-3, 1.9,  -5), 0.3, mirror) )
r.scene.append( Sphere((-2, 1.7,  -5), 0.3, red_bow) )
r.scene.append( Sphere((-1, 1.5,  -5), 0.3, christmas_green) )
r.scene.append( Sphere((0, 1.5,  -5), 0.3, mirror) )
r.scene.append( Sphere((5, 2.4,  -5), 0.3, christmas_green) )
r.scene.append( Sphere((4, 2.2,  -5), 0.3, red_bow) )
r.scene.append( Sphere((3, 1.9,  -5), 0.3, mirror) )
r.scene.append( Sphere((2, 1.7,  -5), 0.3, christmas_green) )
r.scene.append( Sphere((1, 1.5,  -5), 0.3, red_bow) )

#hombre de nieve
#cuerpo
r.scene.append( Sphere((3.5, 0.7,  -5), 0.5, snow) )
r.scene.append( Sphere((3.5, 0, -5), 0.6, snow) )
r.scene.append( Sphere((3.5, -1, -5), 0.9, snow) )

#botones
r.scene.append( Sphere((3, 0,  -4.4), 0.1, coal) )
r.scene.append( Sphere((2.9, -0.4, -4.2), 0.1, coal) )
r.scene.append( Sphere((2.8, -0.8, -4), 0.1, coal) )

#nariz
r.scene.append( Sphere((3, 0.7,  -4.5), 0.1, carrot) )

#sonrisa
r.scene.append( Sphere((2.92, 0.5,  -4.55), 0.05, coal) )
r.scene.append( Sphere((3.08, 0.5,  -4.55), 0.05, coal) )
r.scene.append( Sphere((2.80, 0.57,  -4.55), 0.05, coal) )
r.scene.append( Sphere((3.20, 0.57,  -4.55), 0.05, coal) )

#ojos
r.scene.append( Sphere((2.93, 0.9,  -4.5), 0.08, coal) )
r.scene.append( Sphere((3.11, 0.9,  -4.5), 0.08, coal) )


r.rtRender()

r.glFinish('output.bmp')





