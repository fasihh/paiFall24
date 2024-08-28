from math import pi

def area_trapezoid(a, b, h):
    return 0.5*h*(a+b)
def area_parallelogram(a, b):
    return a*b
def surface_area_cylinder(r, h):
    return 2*pi*r*h + 2*pi*r**2
def volume_cylinder(r, h):
    return pi*r**2*h

print(area_trapezoid(1, 3, 2))
print(area_parallelogram(2, 3))
print(surface_area_cylinder(2, 2))
print(volume_cylinder(2, 2))
