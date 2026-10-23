import math

# Koding di sini

def faktorial(n):
    
    hasil = math.factorial(n)
    proses = " x ".join(str(i) for i in range(n, 0, -1)) # => Untuk Iterasi dari n sampai 1

    print(f"\nFaktorial {n} adalah {hasil}\nHasil dari {proses}\n")