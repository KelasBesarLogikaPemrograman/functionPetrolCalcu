def identitas_pembeli(nama, nomor_hape, pekerjaan):
   return (nama, nomor_hape, pekerjaan)

biodata_pembeli = identitas_pembeli("Fauzan Hafiz", "082122318129", "Mahasiswa")

#Diketahui terdapat jenis bahan bakar yang dapat diisi (pertalait, pertameks, dan selar)
def jenis_bbm(bbm):
    for x in bbm:
        print(x)
#masukkan data bbm
tipe_bbm = jenis_bbm(("pertalait", "pertameks", "selar"))
#harga untuk pertalait = 10000, pertamek = 12000, selar = 5000
pertalait = 10000
pertameks = 12000
selar = 5000
#buatlah sebuah  fungsi yang mengidentifikasi jenis mobil pemberli dan jumlah liter kebutuhan
def jenis_mobil(nama_brand, jumlah_liter):
    return (nama_brand, jumlah_liter)
#panggil fungsi jenis_mobil
identifikasi_kendaraan = jenis_mobil("Daihatsu Sigra", 34)
def hitung_biaya_bbm(liter, harga):
    total = liter * harga
    return total
#panggil fungsi hitung biaya
total_belanja = hitung_biaya_bbm(identifikasi_kendaraan[1], pertameks)
print(total_belanja, "a")
# print dengan contoh output yudi telah membeli tipe bbm selar seharga 12000 dengan total belanja 360000 rupiah
nama = biodata_pembeli[0]
bbm = "pertameks"
print("Fauzan Hafiz telah membeli tipe bbm", bbm, "seharga", pertameks, "dengan total", total_belanja )
#lakukan pembelajaan jika pembeli memiliki uang senilai tertentu lalu hitunglah sampai habis uangnya untuk dibelanjakan
#gunakan recursion
def belanja(uang):
  if(uang >= total_belanja):
    sisa_uang = uang - total_belanja
    belanja(sisa_uang)
    print(sisa_uang)
  else:
    sisa_uang = 0
  return sisa_uang
print("\n\nRecursion Example Results")
belanja(502000)
#output jika uang 1000000 dan total_belanja 408000