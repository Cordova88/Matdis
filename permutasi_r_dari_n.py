import math
import itertools

def permutasiRN(elemen, r):

    n = len(elemen)
    total = math.perm(n, r)
    batasBawah = n - r
    proses = " x ".join(str(i) for i in range(n, batasBawah, -1))

    susunan = list(itertools.permutations(elemen, r))

    print(f"\nPermutasi P({n}, {r}) = {n}!/({n} - {r})! adalah {total}")
    print(f"Hasil dari: {proses}")

    print("Banyaknya Cara:\n")

    nomor = 1
    for i in susunan:
        print(f"{nomor}. [{', '.join(i)}]")
        nomor += 1