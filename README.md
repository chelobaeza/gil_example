# Python GIL cpu vs io-bound samples
samples and variations for testing purposes.

source: https://tenthousandmeters.com/


## IO bound process
```
docker compose run --rm python311 src/io_bound_gather.py
```

will generate a similar output
```
threads_num=1; n=18
18.020555019378662

threads_num=2; n=9
9.012449502944946

threads_num=4; n=4
4.005394697189331

threads_num=8; n=2
2.002504587173462
```

## CPU Bound process

cpu bound tasks won't see any improvement on performance on multithreading

```
docker compose run --rm python310 src/cpu_bound.py
```
output:
```
threads_num=1; n=100000000
3.3834314346313477
3.3801305294036865
3.3731331825256348

threads_num=2; n=50000000
3.3666114807128906
3.3477697372436523
3.346545696258545

threads_num=4; n=25000000
3.416996479034424
3.422248601913452
3.4063024520874023

threads_num=8; n=12500000
3.4292080402374268
3.4294915199279785
3.435525894165039
```

Python3.11 has an improvement, but still not recommended
```
docker compose run --rm python311 src/cpu_bound.py
```

output:
```
threads_num=1; n=100000000
6.635344505310059
6.573229551315308
6.500473499298096

threads_num=2; n=50000000
5.217439889907837
5.100391149520874
3.706242084503174

threads_num=4; n=25000000
3.056912899017334
3.20098614692688
2.949566602706909

threads_num=8; n=12500000
2.70778751373291
2.720555067062378
2.668062686920166
```