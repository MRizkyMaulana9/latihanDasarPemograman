modal_dikeluarkan = int(input("Silahkan Masukan Harga Dari Supplier : "))
persen = int(input("Silahkan Masukan Persen Keuntungan :"))
print('\n')
laba = modal_dikeluarkan * (persen / 100)
harga_jual= modal_dikeluarkan + laba

print("Harga Dari Supplier : Rp. {}".format(modal_dikeluarkan))
print("Persentase Keuntungan :", persen, "%" )
print("Keuntungan Dari Persen : Rp. {}".format(laba))
print("Harga Jual : Rp. {}".format(harga_jual))
