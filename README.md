
# Pertemuan 12 - File I/O dan Error Handling

**Nama:** [Nama lengkap kamu]  
**NIM:** 2225250200  
**Kelas:** [Kelas kamu]

## Tujuan
Membaca, memvalidasi, mengolah, dan menulis data file menggunakan Python.

## Struktur Folder
- `data/`: Menyimpan file input dan output.
- `latihan/`: Menyimpan enam latihan File I/O.
- `tugas/`: Menyimpan program rekap nilai.

## Format File Input
File `data/nilai.txt` menggunakan format NIM,nilai, satu record per baris.

Contoh:
```text
A001,85
A002,78
A003,92
A004,abc
A005,74
A006,88
```

Baris dengan nilai yang tidak valid akan dilaporkan dan dilewati.

## Cara Menjalankan
Jalankan dari terminal pada folder utama proyek:

```bash
python tugas/rekap_nilai_file.py
```

## Error yang Ditangani
- `FileNotFoundError`: File input tidak ditemukan.
- `ValueError`: Format baris atau nilai tidak valid.

## Hasil Pengujian

| Kondisi | Hasil yang diharapkan | Status |
|---|---|---|
| Semua data valid | Semua record diproses | Belum diuji |
| File tidak ditemukan | Pesan kesalahan ditampilkan | Belum diuji |
| Nilai `abc` | Baris dilewati, data lain diproses | Belum diuji |
| Baris kosong | Baris dilewati | Belum diuji |
| Nilai 60 | Dihitung sebagai lulus | Belum diuji |

## Refleksi
Program menggunakan `try-except` untuk menangani kesalahan file dan data. Data tidak valid dilewati agar pemrosesan record lainnya tetap berjalan.
