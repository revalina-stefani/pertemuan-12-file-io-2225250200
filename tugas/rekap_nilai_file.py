
def baca_data(nama_file):
    hasil = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                baris = baris.strip()

                if baris == "":
                    continue

                try:
                    nim, teks_nilai = baris.split(",")
                    nilai = float(teks_nilai)
                    hasil.append((nim, nilai))
                except ValueError:
                    print(f"Baris {nomor} tidak valid: {baris}")

    except FileNotFoundError:
        print(f"File tidak ditemukan: {nama_file}")
        return None

    return hasil


def tulis_rekap(nama_file, data):
    jumlah_data = len(data)

    with open(nama_file, "w", encoding="utf-8") as file:
        file.write("REKAP NILAI MAHASISWA\n")
        file.write("=====================\n")
        file.write(f"Jumlah data valid: {jumlah_data}\n")

        if jumlah_data > 0:
            daftar_nilai = [nilai for nim, nilai in data]
            rata_rata = sum(daftar_nilai) / jumlah_data
            nilai_minimum = min(daftar_nilai)
            nilai_maksimum = max(daftar_nilai)
            jumlah_lulus = sum(
                1 for nilai in daftar_nilai if nilai >= 60
            )

            file.write(f"Rata-rata: {rata_rata:.2f}\n")
            file.write(f"Nilai minimum: {nilai_minimum:g}\n")
            file.write(f"Nilai maksimum: {nilai_maksimum:g}\n")
            file.write(f"Jumlah lulus: {jumlah_lulus}\n")
        else:
            file.write("Rata-rata: tidak tersedia\n")
            file.write("Nilai minimum: tidak tersedia\n")
            file.write("Nilai maksimum: tidak tersedia\n")
            file.write("Jumlah lulus: 0\n")


input_file = "data/nilai.txt"
output_file = "data/hasil_rekap.txt"

data = baca_data(input_file)

if data is not None:
    tulis_rekap(output_file, data)

    print("\nProses rekap selesai.")
    print(f"Jumlah data valid: {len(data)}")

    if data:
        daftar_nilai = [nilai for nim, nilai in data]
        print(f"Rata-rata: {sum(daftar_nilai) / len(data):.2f}")
        print(f"Nilai minimum: {min(daftar_nilai):g}")
        print(f"Nilai maksimum: {max(daftar_nilai):g}")
        print(
            "Jumlah lulus:",
            sum(1 for nilai in daftar_nilai if nilai >= 60)
        )

    print(f"Hasil tersimpan di {output_file}")
