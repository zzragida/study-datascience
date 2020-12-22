import numpy as np

def main():
    f = np.array([1, 2, 4, 7, 11, 16], dtype=float)
    print(np.gradient(f))
    print(np.gradient(f, 2))

if __name__ == "__main__":
    main()