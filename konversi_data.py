import csv
import json

# Nama file yang akan dibaca
file_master_item = 'master-item.csv'

def konversi_csv_ke_javascript():
    """
    Membaca file master-item.csv dengan struktur kolom yang telah disesuaikan
    dan mencetaknya dalam format larik objek JavaScript.
    """
    items_data = []
    
    try:
        with open(file_master_item, mode='r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            
            # Lewati baris header (jika ada)
            try:
                next(reader)
            except StopIteration:
                print("File kosong.")
                return

            for row in reader:
                # Pastikan baris memiliki setidaknya 5 kolom untuk diproses
                if len(row) >= 5:
                    # Sesuaikan dengan struktur kolom Anda yang baru:
                    # row[3] -> Kode Barang
                    # row[2] -> Nama Barang
                    # row[4] -> Satuan
                    kode = row[3].strip()
                    nama = row[2].strip()
                    satuan = row[4].strip()
                    
                    # !! PENTING: Kolom HARGA JUAL tidak ada di contoh Anda.
                    # Untuk sementara, harga diatur ke 0.
                    # Jika harga ada di kolom lain, ganti angka '0' di bawah ini
                    # dengan int(row[indeks_harga])
                    harga = 0
                    
                    # Hanya proses baris yang memiliki kode dan nama
                    if kode and nama:
                        items_data.append({
                            "code": kode,
                            "name": nama,
                            "unit": satuan,
                            "price": harga
                        })

    except FileNotFoundError:
        print(f"--- ERROR ---")
        print(f"File tidak ditemukan: '{file_master_item}'")
        return
    except Exception as e:
        print(f"Terjadi kesalahan saat memproses file: {e}")
        return

    # Cetak hasilnya dalam format yang bisa langsung disalin ke HTML.
    print("[\n    // Data dihasilkan secara otomatis dari master-item.csv.")
    for i, item in enumerate(items_data):
        json_string = json.dumps(item, ensure_ascii=False)
        suffix = "," if i < len(items_data) - 1 else ""
        print(f"    {json_string}{suffix}")
    print("]")


if __name__ == '__main__':
    print(f"--- Memulai Konversi Data dari '{file_master_item}' ---")
    konversi_csv_ke_javascript()
    print("\n--- Konversi Selesai ---")