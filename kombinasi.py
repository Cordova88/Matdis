import math
import itertools

def kombinasi(elemen, r):
    # Data mahasiswa
    n = len(elemen)

    # Menghitung total kombinasi menggunakan math.comb
    total_kombinasi = math.comb(n, r)
    # Pembilang: deret n turun sebanyak r angka (contoh: 4 x 3)
    pembilang = " x ".join(str(i) for i in range(n, n - r, -1))
    # Penyebut: faktorial dari r (contoh: 2 x 1)
    penyebut = " x ".join(str(i) for i in range(r, 0, -1))
    proses = f"{pembilang} / {penyebut}"
    # Menampilkan hasil perhitungan
    print(f"\nKombinasi C({n}, {r}) = {n}! / ({r}!({n}-{r})!) adalah {total_kombinasi}")
    print(f"Hasil dari: {proses}")
    print("Banyaknya Cara:\n")

    # Menghasilkan dan menampilkan daftar kombinasi menggunakan itertools
    susunan_tim = list(itertools.combinations(elemen, r))
    
    for i, susunan in enumerate(susunan_tim, start=1):
        # Format output agar dipisahkan dengan koma seperti contoh
        format_susunan = ", ".join(susunan)
        print(f"{i}. {format_susunan}")

if __name__ == "__main__":
    pass