from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_ROOT / "data" / "nilai.txt"
OUTPUT_FILE = PROJECT_ROOT / "data" / "hasil_rekap.txt"


def baca_data(nama_file):
    data = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                baris = baris.strip()
                if not baris:
                    continue

                try:
                    nim, teks_nilai = baris.split(",")
                    nim = nim.strip()
                    if not nim:
                        raise ValueError("NIM kosong")

                    nilai = float(teks_nilai.strip())
                    data.append((nim, nilai))
                except ValueError:
                    print(f"Baris {nomor} dilewati karena tidak valid: {baris}")
    except FileNotFoundError:
        print(f"File tidak ditemukan: {nama_file}")

    return data


def tulis_rekap(nama_file, data):
    if not data:
        print("Tidak ada data valid untuk direkap.")
        return False

    nilai = [item[1] for item in data]
    jumlah_lulus = sum(1 for angka in nilai if angka >= 60)

    with open(nama_file, "w", encoding="utf-8") as file:
        file.write(f"Jumlah data valid: {len(nilai)}\n")
        file.write(f"Rata-rata: {sum(nilai) / len(nilai):.2f}\n")
        file.write(f"Minimum: {min(nilai):.2f}\n")
        file.write(f"Maksimum: {max(nilai):.2f}\n")
        file.write(f"Jumlah lulus: {jumlah_lulus}\n")

    return True


if __name__ == "__main__":
    data_valid = baca_data(INPUT_FILE)

    if data_valid and tulis_rekap(OUTPUT_FILE, data_valid):
        print(f"Rekap ditulis ke {OUTPUT_FILE}")
        print(f"Jumlah data valid: {len(data_valid)}")
