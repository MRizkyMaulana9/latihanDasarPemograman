hargasupplier = int(input("Silahkan Masukan Harga Dari Supplier : "))
persen = int(input("Silahkan Masukan Persen Keuntungan :"))
keuntungan = hargasupplier * (persen / 100)
harga_jual= hargasupplier + keuntungan

print("Harga dari Supplier :", hargasupplier)
print("Persentase Keuntungan :", persen, "%" )
print("Keuntungan dari Persen :", keuntungan)
print("Harga Jual :", harga_jual)
