print("===== Program Grade Nilai =====")
def cek_nilai(nilai):
    try:
        nilai = float(nilai)
        if nilai >= 90 and nilai <= 100:
            print("Nilai huruf = A dengan Predikat = Dengan Pujian")
        if nilai >= 80 and nilai <= 89:
            print("Nilai huruf = B dengan Predikat = Sangat Memuaskan")
        if nilai >= 70 and nilai <= 79:
            print("Nilai huruf = C dengan Predikat = Memuaskan")
        if nilai >= 60 and nilai <= 69:
            print("Nilai huruf = D dengan Predikat = Tidak Memuaskan")
        if nilai >= 0 and nilai <= 59:
            print("Nilai huruf = E dengan Predikat = Tidak LULUS")
    except ValueError:
        print("Nilai inputan yang dimasukkan salah.")


nilai_input = input("Masukkan nilai Anda: ")
cek_nilai(nilai_input)