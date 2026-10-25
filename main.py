from utils import menu, jeda, garis, bersihkanLayar
from permutasi_n import permutasiN
from permutasi_r_dari_n import permutasiRN

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
            print("Ada 4 mahasiswa: M, N, O, dan P yan\nakan maju presentasi tugas Matematika Diskrit.\nBerapa banyak susunan giliran urutan presentasi yang\nmungkin dibuat dari keempat mahasiswa tersebut?")

            jeda()

            mahasiswa = ["M", "N", "O", "P"]
            permutasiN(mahasiswa)

            jeda()
        elif pilihan == 3:
            bersihkanLayar()
            print("Studi Kasus:\n")
            print("Sebuah gembok loker membutuhkan kode pengaman yang terdiri\ndari 3 angka berbeda. Angka-angka tersebut hanya boleh dipilih\ndari kumpulan 5 angka yang tersedia, yaitu: 1, 2, 3, 4,\n5. \n\nBerapa banyak kemungkinan kode pengaman yang dapat dibuat?")

            jeda()

            jumlahObjek = ['1', '2', '3', '4', '5']
            jumlahDipilih = 3
            permutasiRN(jumlahObjek, jumlahDipilih)

            jeda()
        else:
            print("Pilihan Tidak Valid")