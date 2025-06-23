import numpy as np

def toy_cost(params):
     θ, φ = params
     return np.cos(θ)*np.cos(φ)

grid = np.linspace(0,2*np.pi,41)
best = {'params':None,'cost':np.inf}

for θ in grid:
    for φ in grid:
         c = toy_cost((θ, φ))
         if c < best['cost']:
              best = {'params':(θ, φ),'cost':c}

print("Grid-search best params:", best['params'])
print("Cost at best:", best['cost'])