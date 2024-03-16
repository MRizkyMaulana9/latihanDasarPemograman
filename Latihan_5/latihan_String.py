nama = "M. Rizky Maulana"
alamat = "Kp. Batununggal No. 24, cibadak, Sukabumi"

print("nama saya :", nama)
print("alamat saya :", alamat)
print("\n")

#ambil string berdasarkan index
print("Huruf pertama nama saya :", nama[0])
#untuk mendapat huruf terakhir bisa menggunakan (-) yang akan dimulai dari belakang
print("Huruf terakhir nama saya :", nama[-1])
#kita dapat memanipulasi berapa string yang akan di ambil titik dua menjadi kunci diambil dari belakang atau depan coba di run
print("nama depan nama saya :", nama[:-8])
print("nama terakhir nama saya :", nama[-7:])


print("\n") 

#split string (mengubah string menjadi array berdasarkan spasi)
alamat_array = alamat.split()
print("alamat saya array", alamat_array)

#split string (mengubah string menjadi array berdasarkan koma)
alamat_array = alamat.split(", ")
print("alamat saya array :", alamat_array)
print("alamat jalan array :", alamat_array[0])
print("alamat kecamatan array :", alamat_array[1])
print("alamat kabupaten array :", alamat_array[2])
#print("alamat saya", alamat_array[0],"Kecamatan", alamat_array[1], "Kabupaten", alamat_array[2])
#atau bisa juga

jalan = alamat_array[0]
kecamatan = alamat_array[1]
kabupaten = alamat_array[2]
print(f"alamat saya {alamat_array[0]} Kecamatan {alamat_array[1]} Kabupaten {alamat_array[2]}")


print("\n")
#join string(memasukan variabel lain ke array yang sudah ada)
pemisah ="@"
print("alamat join saya :", pemisah.join(alamat_array))
