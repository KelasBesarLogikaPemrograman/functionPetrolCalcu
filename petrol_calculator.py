
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 07:39:10 2022

@author: yulizarw
"""



#PETROL CALCULATOR

def pengenalan_function() :
    print ("Selamat datang di SPBU UPNVJ FT")
#memanggil fungsi untuk dapat  dijalankan
pengenalan_function()


#masukkan data nama pembeli yang meliputi (nama,nomerhape, pekerjaan) 
def identitas_pembeli(nama,nomor_hape,pekerjaan):
   return (nama, nomor_hape, pekerjaan)

biodata_pembeli = identitas_pembeli("M. Adi Brata", "087878169886", "Mahasiswa")
print(biodata_pembeli)


#Diketahui terdapat jenis bahan bakar yang dapat diisi (pertalait, pertameks, dan selar)
def jenis_bbm(bbm):
    for x, in bbm:
        print(x),

#masukkan data bbm
tipe_bbm =["pertalait", "pertameks", "selar"]
print(tipe_bbm)

#harga untuk pertalait = 10000, pertameks = 12000, selar = 5000
pertalait = 10000
pertameks = 12000 
selar = 5000

#buatlah sebuah  fungsi yang mengidentifikasi jenis mobil pembeli dan jumlah liter kebutuhan

def jenis_mobil (nama_brand,jumlah_liter):
    return (nama_brand, jumlah_liter)

#panggil fungsi jenis_mobil
identifikasi_kendaraan = jenis_mobil("Audi", 21,6)
print(identifikasi_kendaraan)

def hitung_biaya_bbm(liter, harga):
    #rumus
    total_harga = liter*harga
    return (total_harga)

#panggil fungsi hitung biaya
total_belanja = hitung_biaya_bbm(identifikasi_kendaraan[1], pertameks)

print (total_belanja, "a")

# print dengan contoh output yudi  telah membeli tipe bbm selar seharga  12000 dengan total belanja 360000 rupiah
nama = biodata_pembeli[0]
bbm = tipe_bbm[1]

print (nama , "telah membeli tipe bbm" , bbm , "seharga" , pertameks, "dengan total belanja" , total_belanja , "rupiah" )

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

belanja(260000)
print("\n\nRecursion Example Results")
#output jika uang 720000 dan total_belanja 360000
#0
#360000