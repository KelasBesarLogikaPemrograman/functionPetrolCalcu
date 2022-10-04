#PETROL CALCULATOR

def pengenalan_function():
    print ("Selamat datang di SPBU UPNVJ FT")
#memanggil fungsi untuk dapat  dijalankan
pengenalan_function()


#masukkan data nama pembeli yang meliputi (nama,nomerHape, pekerjaan) 
def identitas_pembeli(nama,nomor_hape,pekerjaan):
   return (nama,nomor_hape,pekerjaan)

biodata_pembeli = identitas_pembeli("joko", "081237482736", "beauty vlogger")
print(biodata_pembeli)


#Diketahui terdapat jenis bahan bakar yang dapat diisi (pertalite, pertamax, dan solar)
def jenis_bbm(bbm):
    for x, in bbm:
        print(x)

#masukkan data bbm
tipe_bbm =["pertalite", "pertamax", "solar"]

#harga untuk pertalite = 10000, pertamax = 12000, solar = 5000
pertalite = 10000
pertamax = 12000
solar = 5000

#buatlah sebuah  fungsi yang mengidentifikasi jenis mobil pembeli dan jumlah liter kebutuhan

def jenis_mobil (nama_brand,jumlah_liter):
    return (nama_brand,jumlah_liter)
konsumsi_bbm = jenis_mobil("mazda", "12km/liter")
print(konsumsi_bbm)

#panggil fungsi jenis_mobil
identifikasi_kendaraan = jenis_mobil("mazda", 12)
print(identifikasi_kendaraan)


def hitung_biaya_bbm(liter, harga):
    #rumus
    biaya_bbm = liter * harga
    return (biaya_bbm)

#panggil fungsi hitung biaya
total_belanja = hitung_biaya_bbm(identifikasi_kendaraan[1], pertamax)

print (total_belanja, "a")

# print dengan contoh output yudi  telah membeli tipe bbm selar seharga  12000 dengan total belanja 360000 rupiah
nama = biodata_pembeli[0]
bbm = tipe_bbm[1]
print(nama, "telah membeli tipe bbm", bbm, "seharga", pertamax, "dengan total belanja", total_belanja, "rupiah")

#lakukan pembelajaan jika pembeli memiliki uang senilai tertentu lalu hitunglah sampai habis uangnya untuk dibelanjakan
#gunakan recursion
def belanja(uang):
  if(uang >= total_belanja):
    sisa_uang = uang - total_belanja
    belanja (sisa_uang)
    print(sisa_uang)
  else:
    sisa_uang = 0
  return(sisa_uang)

print("\n\nRecursion Example Results")
belanja(33000000)
#output jika uang 720000 dan total_belanja 360000
#0
#360000