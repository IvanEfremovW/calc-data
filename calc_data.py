import sys
import numpy as np

def main(path: str):
    arr = np.memmap(path, dtype=">u4", mode="r")

    s = np.sum(arr, dtype=np.uint64)
    mn = np.min(arr)
    mx = np.max(arr)

    print(f"sum={int(s)}")
    print(f"min={int(mn)}")
    print(f"max={int(mx)}")


if __name__ == "__main__":
    main(sys.argv[1])
