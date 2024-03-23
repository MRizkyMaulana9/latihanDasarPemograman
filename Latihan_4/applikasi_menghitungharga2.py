Modal_dikeluarkan = int(input("Silahkan Masukan Harga Dari Supplier : "))
persen = int(input("Silahkan Masukan Persen Laba :"))
Laba = Modal_dikeluarkan * (persen / 100)
harga_jual= Modal_dikeluarkan + Laba
print("\n")
print("Harga Modal dari Supplier : Rp. {}".format(Modal_dikeluarkan))
print("Persentase Keuntungan :", persen, "%" )
print("Laba dari Supplier : Rp. {}".format(Laba))
print("Harga Jual Ke Customer : Rp. {}".format(harga_jual))