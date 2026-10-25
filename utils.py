import os

def menu():
    menuUtama = """
    ===================================
    |                                 |
    | Program Permutasi Dan Kombinasi |
    |                                 |
    ===================================
    |                                 |
    | [1] Kombinasi                   |
    | [2] Permutasi                   |
    |                                 |
    ===================================
    """

    print(menuUtama)

def jeda():
    input(f"\n[Tekan Enter Untuk Lanjut...]")

def bersihkanLayar():
    os.system('cls')

def garis():
    print("—"*30)