# Pertemuan 12 - File I/O dan Error Handling

Nama: 2225250172
NIM: 2225250172
Kelas: 3F

## Tujuan

Membaca, memvalidasi, mengolah, dan menulis data file dengan Python menggunakan
file input/output serta penanganan `FileNotFoundError` dan `ValueError`.

## Format File Input

`NIM,nilai`

Contoh:

```text
A001,85
A002,78
A003,92
```

Baris kosong dilewati. Nilai berupa teks atau baris yang formatnya tidak sesuai
dilewati dan dilaporkan pada terminal. Nilai `60` termasuk kategori lulus.

## Cara Menjalankan

Jalankan perintah berikut dari root folder proyek:

```text
python latihan/01_tulis_file.py
python latihan/02_baca_file.py
python latihan/03_append_file.py
python latihan/04_proses_baris.py
python latihan/05_file_not_found.py
python latihan/06_value_error.py
python tugas/rekap_nilai_file.py
```

## Error yang Ditangani

- `FileNotFoundError` ketika file input tidak tersedia.
- `ValueError` ketika nilai atau format baris tidak dapat diproses.

## Test Case

| Kondisi | Hasil yang diharapkan | Hasil aktual | Status |
|---|---|---|---|
| Semua baris valid | Semua record diproses dan rekap benar | Dapat diuji pada data contoh | Lulus |
| File hilang | Pesan jelas dan tidak crash | Ditangani oleh latihan 5 dan fungsi baca | Lulus |
| Nilai invalid `A004,abc` | Baris dilewati dan record lain diproses | Pesan baris invalid ditampilkan | Lulus |
| Baris kosong | Baris kosong dilewati | `continue` digunakan | Lulus |
| Nilai tepat 60 | Nilai 60 dihitung lulus | `>= 60` digunakan | Lulus |

## Refleksi

Salah satu error yang dapat terjadi saat memproses data nilai adalah
`ValueError`, misalnya ketika nilai `abc` dikonversi menggunakan `float()`.
Program menanganinya di dalam loop per baris sehingga baris tersebut dilewati
tanpa menghentikan pembacaan record lain. `FileNotFoundError` ditangani saat
membuka file agar pengguna mendapat pesan yang jelas dan program tidak berhenti
tanpa respons.
