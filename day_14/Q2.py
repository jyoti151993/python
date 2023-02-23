# 2) Create a class that captures planets. 
# 	Each planet has a name, a distance from the sun, 
#     and its gravity relative to Earth’s gravity. For distance and gravity,
#      use the type double which captures real numbers. Make objects for Earth and your favorite non-earth planet.


class Planets:
    def __init__(self, name, distance, relative_gravity):
        self.name = name
        self.distance = distance
        self.relative_gravity = relative_gravity

p1 = Planets("Earth", 147.67, 9.81 )
p2 = Planets("Mars", 228.38,3.72)
