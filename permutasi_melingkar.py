import math
import itertools
 
def permutasiMelingkar(elemen):
 
    elemen = ["A", "B", "C", "D", "E"]
    n = len(elemen)
 
    hasilRumus = math.factorial(n - 1)
    print("Jumlah orang (n)  :", n)
    print("Rumus (n - 1)!    : (5 - 1)! = 4! =", hasilRumus)
 
    semuaSusunan = []
    for urutan in itertools.permutations(elemen[1:]):
        susunan = [elemen[0]] + list(urutan)
        semuaSusunan.append(susunan)
 
    print("Hasil hitung satu-satu :", len(semuaSusunan))
    print()
    print("Semua susunan duduk:")
    nomor = 1
    for susunan in semuaSusunan:
        print(nomor, ".", " - ".join(susunan))
        nomor = nomor + 1
 
if __name__ == "__main__":
    pass