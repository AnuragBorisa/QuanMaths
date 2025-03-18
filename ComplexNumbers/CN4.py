import numpy as np

def findRealAndImag(z1,z2):
    ans = z1/z2;
    return {"Rz":ans.real,"Im":ans.imag}

def evaluateMods(z1,z2):
    modz1 = np.abs(z1)
    modz2 = np.abs(z2)
    return modz1/modz2

def main():
    print(f"{findRealAndImag(1+1j,2+3j)}")
    print(f"Evaluate for real a and b {evaluateMods(1+2j,1-2j)}")

if __name__ == "__main__":
    main()