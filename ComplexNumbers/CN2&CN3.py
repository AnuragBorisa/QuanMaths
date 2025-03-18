import numpy as np;


def evaluate_complex(z,operation="root",n=None):
    if operation == "root":
        if n is None:
            raise ValueError("For the 'root' operation, please specify n (the degree of the root).")
        r = np.abs(z)
        theta = np.angle(z)
        roots = [r**(1/n) * np.exp(1j * (theta + 2*np.pi*k)/n) for k in range(n)]
        return roots
    elif operation == "exp":
         return np.exp(z)
    elif operation == "rect_polar":
        r = np.abs(z);
        theta = np.angle(z)
        return {"rectangular":z,"polar":(r,theta)}
    else:
        raise ValueError("Unknown operation. Supported operations are 'root', 'exp', and 'rect_polar'.")
    
def main():
     print("=== Part (a): 4th roots of i ===")
     roots_i = evaluate_complex(1j,operation="root",n=4)
     for idx,root in enumerate(roots_i):
         print(f"  4th root #{idx}: {root}")
    
     print("\n=== Part (b): Square roots of (1 + i√3) ===")
     z = 1 + np.sqrt(3)*1j
     roots_z = evaluate_complex(z, operation="root", n=2)
     for idx, root in enumerate(roots_z):
        print(f"  Square root #{idx}: {root}")
     
     print("\n=== Part (c): exp(2 i^3) ===")
     exp_val = evaluate_complex(2*(1j**3), operation="exp")
     print(f"  exp(2 i^3) = {exp_val}")

     print("\n===QUESTION 3 (a):3rd Root of 1 ===")
     roots_one = evaluate_complex(1,operation="root",n=3)
     for idx,root in enumerate(roots_one):
         print(f" 3rd root  #{idx}: {root}")

     print("\n===QUESTION 3 (b):3rd Root of i ===")
     roots_i = evaluate_complex(1j,operation="root",n=3)
     for idx,root in enumerate(roots_i):
         print(f" 3rd root #{idx}:{root}")

if __name__ == "__main__":
    main()


    
   