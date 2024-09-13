def shifr():
    for n in range(3, 21):
        for j in range(1, 10):

            for k in range(1,10):
                g = k + j
                if n == j + k or n % g == 0:
                    if j == k or j > k:
                        continue
                    print(f"{n}-{j}{k}")

print(shifr())