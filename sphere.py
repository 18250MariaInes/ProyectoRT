"""
Maria Ines Vasquez Figueroa
18250
Gráficas
DR3 Planes & Cubes
Sphere, Planes and AABB
"""

import numpy as np
from gl import *
from mathLib import *

OPAQUE = 0
REFLECTIVE = 1
TRANSPARENT = 2
WHITE = color(1,1,1)

class Material(object):
    # Un material como visto en Unity que rige como se comportara con la luz. Como los materiales de roca, ladrillo, entre otros
    def __init__(self, diffuse = WHITE, spec = 0, matType = OPAQUE):
        # color pero se esparce cuando tiene luz
        self.diffuse = diffuse
        self.spec = spec
        self.matType = matType


class Intersect(object): #función que devuelve la distancia de la intersección
    def __init__(self, distance, point, normal, sceneObject):
        self.distance = distance
        self.point = point
        self.normal = normal
        self.sceneObject = sceneObject

class AmbientLight(object):
    def __init__(self, strength = 0, _color = WHITE):
        self.strength = strength
        self.color = _color

class PointLight(object):
    def __init__(self, position = (0,0,0), _color = WHITE, intensity = 1):
        self.position = position
        self.intensity = intensity
        self.color = _color


class Sphere(object):
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def ray_intersect(self, orig, dir):
        
        # Regresa falso o verdadero si hace interseccion con una esfera

        # Formula para un punto en un rayo
        # t es igual a la distancia en el rayo
        # P = O + tD
        # P0 = O + t0 * D
        # P1 = O + t1 * D
        #d va a ser la magnitud de un vector que es
        #perpendicular entre el rayo y el centro de la esfera
        # d > radio, el rayo no intersecta
        #tca es el vector que va del orign al punto perpendicular al centro
        #L = np.subtract(self.center, orig)
        Lp=subtract(self.center[0],orig[0],self.center[1],orig[1],self.center[2],orig[2])#funciona
        
       
        tcap=dot(Lp,dir[0], dir[1], dir[2])#funciona
        
        lp=frobenius(Lp) #funciona magnitud de L
        
        d = (lp**2 - tcap**2) ** 0.5
        if d > self.radius:
            return None

        # thc es la distancia de P1 al punto perpendicular al centro
        thc = (self.radius ** 2 - d**2) ** 0.5
        t0 = tcap - thc
        t1 = tcap + thc
        if t0 < 0:
            t0 = t1

        if t0 < 0: # t0 tiene el valor de t1
            return None
        #hit = np.add(orig, t0 * np.array(dir))
        """print(orig)
        print(t0 * np.array(dir))
        print(hit)
        print(add(orig, multiN(t0,dir)))"""
        hitp=add(orig, multiN(t0,dir))
        #print("-------------------------------------------------------")

        #norm = np.subtract( hit, self.center )
        norm2=subtract(hitp[0], self.center[0],hitp[1],self.center[1],hitp[2],self.center[2])#funciona
        #norm = norm / np.linalg.norm(norm)
        norm2=division(norm2, frobenius(norm2))
        """print(norm)
        print(norm2)"""

        return Intersect(distance = t0,
                         point = hitp,
                         normal = norm2,
                         sceneObject = self)
#clase para plano infinitos
class Plane(object):
    def __init__(self, position, normal, material):
        self.position = position
        #self.normal = normal / np.linalg.norm(normal)
        self.normal = division(normal, frobenius(normal))
        self.material = material

    def ray_intersect(self, orig, dir):
        # t = (( position - origRayo) dot normal) / (dirRayo dot normal)

        denom = dot(dir, self.normal[0], self.normal[1], self.normal[2])
        """print("-----------------------")
        print(denom)
        print(dot(dir, self.normal[0], self.normal[1], self.normal[2]))"""

        if abs(denom) > 0.0001:
            val2=subtract(self.position[0], orig[0], self.position[1], orig[1], self.position[2], orig[2])
            t = dot(self.normal, val2[0],val2[1],val2[2])/denom
            """print("-----------------------")
            print(np.dot(self.normal, np.subtract(self.position, orig))/ denom)
            
            print(dot(self.normal, val2[0],val2[1],val2[2])/denom)"""
            if t > 0:
                # P = O + tD
                hit = add(orig, multiN(t, dir))
                """print("-----------------------")
                print(np.add(orig, t * np.array(dir)))"""
                """print(orig)
                print(t)
                print(t * np.array(dir))"""
                return Intersect(distance = t,
                                 point = hit,
                                 normal = self.normal,
                                 sceneObject = self)

        return None
#clase para cubos, bounding box
class AABB(object):
    def __init__(self, position, size, material):
        self.position = position
        self.size = size
        self.material = material
        self.planes = []

        halfSize = size / 2

        self.planes.append( Plane( add(position, (halfSize,0,0)), (1,0,0), material))
        self.planes.append( Plane( add(position, (-halfSize,0,0)), (-1,0,0), material))

        self.planes.append( Plane( add(position, (0,halfSize,0)), (0,1,0), material))
        self.planes.append( Plane( add(position, (0,-halfSize,0)), (0,-1,0), material))

        self.planes.append( Plane( add(position, (0,0,halfSize)), (0,0,1), material))
        self.planes.append( Plane( add(position, (0,0,-halfSize)), (0,0,-1), material))


    def ray_intersect(self, orig, dir):

        epsilon = 0.001

        boundsMin = [0,0,0]
        boundsMax = [0,0,0]

        for i in range(3):
            boundsMin[i] = self.position[i] - (epsilon + self.size / 2)
            boundsMax[i] = self.position[i] + (epsilon + self.size / 2)

        t = float('inf')
        intersect = None

        for plane in self.planes:
            planeInter = plane.ray_intersect(orig, dir)

            if planeInter is not None:

                # Si estoy dentro del bounding box
                if planeInter.point[0] >= boundsMin[0] and planeInter.point[0] <= boundsMax[0]:
                    if planeInter.point[1] >= boundsMin[1] and planeInter.point[1] <= boundsMax[1]:
                        if planeInter.point[2] >= boundsMin[2] and planeInter.point[2] <= boundsMax[2]:
                            if planeInter.distance < t:
                                t = planeInter.distance
                                intersect = planeInter

        if intersect is None:
            return None

        return Intersect(distance = intersect.distance,
                         point = intersect.point,
                         normal = intersect.normal,
                         sceneObject = self)

