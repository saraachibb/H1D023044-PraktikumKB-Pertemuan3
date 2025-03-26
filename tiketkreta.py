import random
import datetime

# Struktur Data: Menyimpan daftar rute
trains = {
    "1": {"route": "Purwokerto - Semarang", "available_seats": ["A1", "A2", "B1", "B2"]},
    "2": {"route": "Jakarta - Yogyakarta", "available_seats": ["C1", "C2", "D1", "D2"]},
    "3": {"route": "Pekalongan - Malang", "available_seats": ["E1", "E2", "F1", "F2"]}
}

def display_trains():
    print("Daftar Rute Kereta:")
    for key, train in trains.items():
        print(f"{key}. {train['route']}")

def book_ticket():
    display_trains()
    pilihan = input("Pilih nomor rute yang ingin dipesan: ")
    if pilihan not in trains:
        print("Pilihan tidak valid!")
        return
    
    train = trains[pilihan]
    print(f"Anda memilih rute: {train['route']}")
    print("Kursi tersedia: ", ', '.join(train['available_seats']))
    kursi = input("Pilih kursi: ")
    
    if kursi not in train['available_seats']:
        print("Kursi tidak tersedia!")
        return
    
    # Memasukkan jadwal keberangkatan
    try:
        tanggal_keberangkatan = input("Masukkan tanggal keberangkatan (YYYY-MM-DD HH:MM): ")
        jadwal_keberangkatan = datetime.datetime.strptime(tanggal_keberangkatan, "%Y-%m-%d %H:%M")
    except ValueError:
        print("Format tanggal tidak valid! Gunakan format YYYY-MM-DD HH:MM")
        return
    
    # Struktur kontrol: Menghapus kursi yang sudah dipesan
    train['available_seats'].remove(kursi)
    kode_booking = random.randint(1000, 9999)
    waktu_pemesanan = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    
    print(f"Tiket berhasil dipesan! Kode Booking: {kode_booking}")
    print(f"Rute: {train['route']}, Kursi: {kursi}")
    print(f"Waktu Pemesanan: {waktu_pemesanan}")
    print(f"Jadwal Keberangkatan: {jadwal_keberangkatan.strftime('%Y-%m-%d %H:%M')}")

def main():
    while True:
        print("\nSistem Pemesanan Tiket Kereta")
        print("1. Lihat daftar rute")
        print("2. Pesan tiket")
        print("3. Keluar")
        pilihan = input("Masukkan pilihan: ")
        
        if pilihan == "1":
            display_trains()
        elif pilihan == "2":
            book_ticket()
        elif pilihan == "3":
            print("Terima kasih telah menggunakan layanan kami!")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
