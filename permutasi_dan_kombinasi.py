import math
import itertools

def permutasiDanKombinasi():
    # Data Mahasiswa
    mahasiswa = ['M', 'N', 'O', 'P']
    n = len(mahasiswa)
    r = 2 # Jumlah orang yang dipilih

    print("="*50)
    print("PROGRAM PERMUTASI DAN KOMBINASI")
    print("="*50)
    print(f"Terdapat {n} mahasiswa: {', '.join(mahasiswa)}.\n")

    # ==========================================
    # STUDI KASUS 1: PERMUTASI (Urutan Penting)
    # ==========================================
    print("--- STUDI KASUS 1: PERMUTASI ---")
    print("Kasus: Akan dipilih 2 orang untuk menempati jabatan Ketua dan Wakil Ketua.")
    print("Berapa banyak susunan kepengurusan yang mungkin dibuat?\n")
    
    input("[Tekan Enter Untuk Lanjut...]\n")

    total_permutasi = math.perm(n, r)
    proses_p = " x ".join(str(i) for i in range(n, n - r, -1))
    
    print(f"Permutasi P({n}, {r}) = {n}! / ({n}-{r})! adalah {total_permutasi}")
    print(f"Hasil dari: {proses_p}")
    print("Banyaknya Cara (Ketua, Wakil Ketua):")
    
    susunan_p = list(itertools.permutations(mahasiswa, r))
    for i, susunan in enumerate(susunan_p, start=1):
        print(f"{i}. {susunan[0]} (Ketua), {susunan[1]} (Wakil)")

    print("\n" + "="*50 + "\n")

    # ==========================================
    # STUDI KASUS 2: KOMBINASI (Urutan Tidak Penting)
    # ==========================================
    print("--- STUDI KASUS 2: KOMBINASI ---")
    print("Kasus: Akan dipilih 2 orang untuk menjadi perwakilan tim proyek tanpa jabatan.")
    print("Berapa banyak susunan tim yang mungkin dibuat?\n")
    
    input("[Tekan Enter Untuk Lanjut...]\n")

    total_kombinasi = math.comb(n, r)
    pembilang_c = " x ".join(str(i) for i in range(n, n - r, -1))
    penyebut_c = " x ".join(str(i) for i in range(r, 0, -1))
    
    print(f"Kombinasi C({n}, {r}) = {n}! / ({r}!({n}-{r})!) adalah {total_kombinasi}")
    print(f"Hasil dari: ({pembilang_c}) / ({penyebut_c})")
    print("Banyaknya Cara (Anggota Tim):")
    
    susunan_c = list(itertools.combinations(mahasiswa, r))
    for i, susunan in enumerate(susunan_c, start=1):
        print(f"{i}. {susunan[0]} dan {susunan[1]}")

if __name__ == "__main__":
    pass