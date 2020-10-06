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
mirror = Material( spec = 64, matType = REFLECTIVE)



width = 512
height = 512
r = Raytracer(width,height)
r.glClearColor(0.2, 0.6, 0.8)
r.glClear()
r.envmap = Envmap('envmap.bmp')
r.pointLight = PointLight(position = (0,0,0), intensity = 1)
r.ambientLight = AmbientLight(strength = 0.1)

"""r.scene.append( Sphere(( 1, 1, -8), 1.5, brick) )
r.scene.append( Sphere(( 0, 0, -5), 0.5, stone) )
r.scene.append( Sphere((-3, 3, -10),  2, mirror) )
r.scene.append( Sphere((-3, -1.5, -10), 1.5, mirror) )"""
#cuarto
r.scene.append( Plane((0, -3, 0), (0,1,0), stone) )
r.scene.append( Plane((0, 3, 0), (0,1,0), stone) )
r.scene.append( Plane((0, 0, -10), (0,0,1), stone) )
r.scene.append( Plane(( -3,0, 0), (1,0,0), stone) )
r.scene.append( Plane(( 3, 0,0), (1,0,0), stone) )
#cubos
r.scene.append( AABB((1.5, -1, -5), 1.5, carrot ) )
r.scene.append( AABB((-1.5, -1, -5), 1.5, pink_center ) )
"""r.scene.append( AABB(V3(1.5, -1.5, -5), 1.5, mirror ) )
r.scene.append( AABB(V3(-1.5, -1.5, -5), 1.5, glass ) )"""


r.rtRender()

r.glFinish('output.bmp')





