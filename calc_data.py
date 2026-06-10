import sys
import os
import numpy as np
from concurrent.futures import ProcessPoolExecutor


def process_chunk(args):
    filepath, start_byte, length_bytes = args

    chunk_sum = 0
    chunk_min = 0xFFFFFFFF
    chunk_max = 0

    with open(filepath, "rb") as f:
        f.seek(start_byte)

        raw_data = f.read(length_bytes)

        arr = np.frombuffer(raw_data, dtype=">u4", count=length_bytes // 4)

        chunk_sum = int(arr.sum(dtype=np.uint64))
        chunk_min = int(arr.min())
        chunk_max = int(arr.max())

    return chunk_sum, chunk_min, chunk_max


def main():

    path = sys.argv[1]

    file_size = os.path.getsize(path)
    file_size = (file_size // 4) * 4

    num_workers = os.cpu_count() or 1

    chunk_size = file_size // num_workers
    chunk_size = (chunk_size // 4) * 4

    tasks = []
    start = 0

    for i in range(num_workers):
        if i == num_workers - 1:
            length = file_size - start
        else:
            length = chunk_size

        if length > 0:
            tasks.append((path, start, length))
            start += length

    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        results = list(executor.map(process_chunk, tasks))

    result_sum = sum(r[0] for r in results)
    result_min = min(r[1] for r in results)
    result_max = max(r[2] for r in results)

    print(f"sum={result_sum}")
    print(f"min={result_min}")
    print(f"max={result_max}")


if __name__ == "__main__":
    main()
