import math
import itertools

def kombinasiPerulangan(elemen, r):

    n = len(elemen)

    # Menghitung total cara menggunakan rumus C(n+r-1, r)
    n_rumus = n + r - 1
    total_cara = math.comb(n_rumus, r)
    
    print("\nPerhitungan Matematis:")
    print(f"Rumus    : C(n + r - 1, r)")
    print(f"Hitungan : C({n} + {r} - 1, {r}) = C({n_rumus}, {r})")
    print(f"Total    : {total_cara} cara\n")
    
    print("Daftar Kemungkinan Susunan Donat:")

    # Menghasilkan daftar kombinasi dengan pengulangan menggunakan itertools
    kombinasi_donat = list(itertools.combinations_with_replacement(elemen, r))
    
    for i, susunan in enumerate(kombinasi_donat, start=1):
        # Menggabungkan elemen tuple menjadi string agar rapi
        format_susunan = ", ".join(susunan)
        print(f"{i}. {format_susunan}")

if __name__ == "__main__":
    pass