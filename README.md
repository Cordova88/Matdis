# Tugas MatDih

## 📚 Tautan Dokumentasi Python

* 📘 [Dokumentasi Resmi Modul `math`](https://docs.python.org/3/library/math.html)
* 📙 [Dokumentasi Resmi Modul `itertools`](https://docs.python.org/3/library/itertools.html)

---

## 📋 To-Do List Pengerjaan Tugas Kombinatorika

*Tandai dengan `[x]` yang mau dikerjakan.

- [ x ] **1. Faktorial**
  * Rumus: $n!$
  * Fungsi terkait: `math.factorial()`

- [ ] **2. Permutasi $n$**
  * Rumus: $P(n) = n!$
  * Fungsi terkait: `math.perm()`, `itertools.permutations()`

- [ ] **3. Permutasi $r$ dari $n$**
  * Rumus: $P(n, r) = \frac{n!}{(n-r)!}$
  * Fungsi terkait: `math.perm()`, `itertools.permutations()`

- [ ] **4. Permutasi dengan Perulangan**
  * Rumus: $P = n^r$
  * Fungsi terkait: `pow()`, `itertools.product()`

- [ ] **5. Permutasi dengan Unsur Identik**
  * Rumus: $P = \frac{n!}{k_1! \cdot k_2! \dots k_m!}$
  * Fungsi terkait: `math.factorial()`, `itertools.permutations()`

- [ ] **6. Permutasi Melingkar (Siklis)**
  * Rumus: $P_{siklis} = (n - 1)!$
  * Fungsi terkait: `math.factorial()`

- [ ] **7. Kombinasi**
  * Rumus: $C(n, r) = \frac{n!}{r!(n-r)!}$
  * Fungsi terkait: `math.comb()`, `itertools.combinations()`

- [ ] **8. Permutasi dan Kombinasi (Studi Kasus Gabungan)**
  * Rumus: Kombinasi $P(n, r)$ dan $C(n, r)$
  * Fungsi terkait: `math.perm()`, `math.comb()`

- [ ] **9. Kombinasi dengan Batasan**
  * Rumus: Variasi $C(n, r)$ dengan syarat khusus
  * Fungsi terkait: `itertools.combinations()` dengan *filtering*

- [ ] **10. Kombinasi dengan Perulangan**
  * Rumus: $C'(n, r) = \frac{(n + r - 1)!}{r!(n - 1)!}$
  * Fungsi terkait: `math.comb()`, `itertools.combinations_with_replacement()`
