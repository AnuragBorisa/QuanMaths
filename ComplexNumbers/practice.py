import numpy as np;

z = 3 + 4j

magitude = np.abs(z)
angle = np.angle(z)

print("Rectangular Form",z)
print("Polar Form:magnitude =",magitude,", angle =",angle)

z_from_polar = magitude * np.exp(1j*angle)
print("Rectangular form from ploar (via Euler's Formula ):",z_from_polar)