import math
import itertools

def permutasiN(elemen):

    n = len(elemen)
    total = math.perm(n)
    proses = " x ".join(str(i) for i in range(n, 0, -1))

    susunan = list(itertools.permutations(elemen))

    print(f"\nPermutasi P({n}) = {n}! adalah {total}")
    print(f"Hasil dari: {proses}")

    print("Banyaknya Cara:\n")

    nomor = 1
    for i in susunan:
        print(f"{nomor}. {', '.join(i)}")
        nomor += 1