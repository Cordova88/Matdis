from utils import menu, jeda, garis, bersihkanLayar
from permutasi_n import permutasiN

if __name__ == "__main__":

    isRunning = True

    while(isRunning):

        bersihkanLayar()
        menu()
        pilihan = int(input("> "))

        if pilihan == 0:
            isRunning = False
        if pilihan == 1:
            pass
        elif pilihan == 2:
            bersihkanLayar()
            print("Studi Kasus:\n")
            print("Ada 4 mahasiswa: M, N, O, dan P\nyang akan maju presentasi tugas Matematika Diskrit.\nBerapa banyak susunan giliran urutan presentasi yang\nmungkin dibuat dari keempat mahasiswa tersebut?")

            jeda()

            mahasiswa = ["M", "N", "O", "P"]
            permutasiN(mahasiswa)

            jeda()
            
        else:
            print("Pilihan Tidak Valid")