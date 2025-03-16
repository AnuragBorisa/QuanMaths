import numpy as np
import matplotlib.pyplot as plt
import random

a = 1+2j
b = -3+4j

sum_ab = a+b
mul_ab = a*b
ratio_ba = b/a


print("a + b       =", sum_ab)
print("a * b       =", mul_ab)
print("b / a       =", ratio_ba)

points = {
    "a" : a,
    "b" : b,
    "a+b" : sum_ab,
    "a*b" : mul_ab,
    "b/a" : ratio_ba
}

plt.figure(figsize=(6,6))
ax = plt.gca()

colors = ['red', 'blue', 'green', 'purple', 'orange']

for (label, z), color in zip(points.items(), colors):
    plt.scatter(z.real, z.imag, color=color)
    dx = random.randint(-10, 10)
    dy = random.randint(-10, 10)
    ax.annotate(
        label,
        (z.real, z.imag),
        textcoords="offset points",
        xytext=(dx, dy),
    )

ax.axhline(y=0, color='black', linewidth=0.5)
ax.axvline(x=0, color='black', linewidth=0.5)
ax.set_xlabel('Real axis')
ax.set_ylabel('Imag axis')
ax.set_aspect('equal', 'box')
ax.set_title("Complex Numbers in the Plane")

plt.show()


