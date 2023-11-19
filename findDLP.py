def dlp(p, X, n):
    for i in range(n):
        y = 2**i % p
        print(f"index ke {i} = ", y)
        if y == X:
            return print(f"jawaban ketemu yaitu : {i}")


dlp(7, 4, 10)
