# ============================================
#        APLIKASI KASIR RESTORAN (Python)
# ============================================

# 1. Mulai Program
print("=" * 40)
print("     MEIMEI RESTORAN - KASIR")
print("=" * 40)

total = 0  # variabel untuk menyimpan total belanja

# Daftar menu
menu = {
    1: ("Dimsum Hakau", 25000),
    2: ("Bakmi Pangsit", 22000),
    3: ("Nasi Hainan", 28000),
    4: ("Bebek Peking", 85000),
    5: ("Capcay Kuah", 30000),
}

# 2. Tampilkan menu & proses pemesanan (perulangan)
while True:
    print("\n--- DAFTAR MENU ---")
    for nomor, (nama, harga) in menu.items():
        print(f"{nomor}. {nama:<15} - Rp{harga:,}".replace(",", "."))
    print("0. Selesai Memilih")

    pilihan = input("\nPilih menu (0-5): ")

    # Validasi input harus angka
    if not pilihan.isdigit():
        print("Input tidak valid! Masukkan angka.")
        continue

    pilihan = int(pilihan)

    # 4. Apakah pilihan 0? Jika ya, keluar dari perulangan
    if pilihan == 0:
        break

    # Pilihan di luar menu
    if pilihan not in menu:
        print("Menu tidak tersedia! Silakan pilih lagi.")
        continue

    # 3. Input jumlah pesanan
    jumlah = input("Masukkan jumlah pesanan: ")
    if not jumlah.isdigit() or int(jumlah) <= 0:
        print("Jumlah tidak valid! Silakan ulangi.")
        continue

    jumlah = int(jumlah)

    # Hitung subtotal lalu tambahkan ke total
    nama, harga = menu[pilihan]
    subtotal = harga * jumlah
    total += subtotal

    print(f"Ditambahkan: {nama} x{jumlah} = Rp{subtotal:,}".replace(",", "."))
    print(f"Total sementara: Rp{total:,}".replace(",", "."))

# 5. Hitung Diskon
if total > 200000:
    persen_diskon = 20
else:
    persen_diskon = 0

potongan = total * persen_diskon // 100
total_bayar = total - potongan

# 6. Tampilkan Struk Pembayaran
print("\n" + "=" * 40)
print("          MEIMEI RESTORAN")
print("         STRUK PEMBAYARAN")
print("=" * 40)
print(f"Total Belanja : Rp{total:,}".replace(",", "."))
print(f"Diskon        : {persen_diskon}%")
print(f"Potongan      : Rp{potongan:,}".replace(",", "."))
print("-" * 40)
print(f"Total Bayar   : Rp{total_bayar:,}".replace(",", "."))
print("=" * 40)
print("            Terima Kasih")
print("=" * 40)