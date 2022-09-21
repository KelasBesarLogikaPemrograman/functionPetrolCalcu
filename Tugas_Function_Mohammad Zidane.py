
def pengenalan_function() :
    print ("Selamat datang di SPBU UPNVJ FT")
#mmeanggil fungsi untuk dapat  dijalankan
pengenalan_function()


#masukkan data nama pembeli yang meliputi (nama,nomerHape, pekerjaan) 
def identitas_pembeli(nama, nomerHP,pekerjaan):
   return (nama, nomerHP,pekerjaan)

biodata_pembeli = identitas_pembeli("M Zidane","081223344556","HRD")
print (biodata_pembeli)
#Diketahui terdapat jenis bahan bakar yang dapat diisi (pertalait, pertameks, dan selar)
def jenis_bbm(bbm):
    for x, in bbm:
        print(x),

#masukkan data bbm
tipe_bbm =["Pertalait", "Pertameks", "Selar"]
print (tipe_bbm)

#harga untuk pertalait = 10000, pertamek = 12000, selar = 5000
pertalait = 10000
pertameks =  12000
selar = 5000

#buatlah sebuah  fungsi yang mengidentifikasi jenis mobil pemberli dan jumlah liter kebutuhan

def jenis_mobil (nama_brand,jumlah_liter):
    return (nama_brand,jumlah_liter)

#panggil fyungsi jenis_mobil
identifikasi_kendaraan = jenis_mobil("Alphard", 12.1004)
print (identifikasi_kendaraan)

def hitung_biaya_bbm(liter, harga):
    #rumus
    total_biaya = liter*harga
    return total_biaya

#panggil fungsi hitung biaya
total_belanja = hitung_biaya_bbm(identifikasi_kendaraan[(1)], pertameks)

print (total_belanja, "a")

# print dengan contoh output yudi  telah membeli tipe bbm selar seharga  12000 dengan total belanja 360000 rupiah
nama_orang = biodata_pembeli[0]
bbm = tipe_bbm[1]
print (nama_orang, "telah membeli tipe bbm" ,bbm, "seharga", pertameks, "dengan total belanja", total_belanja, "rupiah")

#lakukan pembelajaan jika pembeli memiliki uang senilai tertentu lalu hitunglah sampai habis uangnya untuk dibelanjakan
#gunakan recursion
def belanja(uang):
  if(uang >= total_belanja):
    sisa_uang = uang - total_belanja
    belanja (sisa_uang)
    print(sisa_uang)
  else:
    sisa_uang = 0
  return sisa_uang

print("\n\nRecursion Example Results")
belanja(200000)
#output jika uang 720000 dan total_belanja 360000
#0
#360000