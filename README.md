# calc-data

Запуск через Docker:
```bash
docker build -t calc_data .
docker run --rm -v /path/to/data:/data:ro calc_data /data/input.bin
```
