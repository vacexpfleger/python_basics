import physics
"""
Modul physics se skládá ze čtyř jednoduchých funkcí, které počítají specifické fyzikální veličiny
"""

print(physics.earth_gravity_force.__doc__)
weight = int(input("Enter your weight (kg): "))
print("The gravity power on Earth is:", physics.earth_gravity_force(weight), "N")
print("The gravity power on Moon is:", physics.moon_gravity_force(weight), "N")

print(physics.object_time.__doc__)
distance = int(input("Enter the distance between you and the sound source (m): "))
print("The time is:", "%.2f" % physics.object_time(distance), "sec")

print(physics.object_lightspeed.__doc__)
index = float(input("Enter the refraction index of an object: "))
print("The speed of light is:", "%.2f" % physics.object_lightspeed(index), "m/s")