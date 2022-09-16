#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 07:39:10 2022

@author: yulizarw
"""



#PETROL CALCULATOR

def pengenalan_function() :
    print ("Selamat datang di SPBU UPNVJ FT")
#mmeanggil fungsi untuk dapat  dijalankan
"Selamat datang di SPBU UPNVJ FT"


#masukkan data nama pembeli yang meliputi (nama,nomerHape, pekerjaan) 
def identitas_pembeli(nama,nomor_hape,pekerjaan):
   return ()

biodata_pembeli = identitas_pembeli()
biodata_pembeli = ("Aura", 089519602527, "Pelajar")
print (biodata_pembeli)

#Diketahui terdapat jenis bahan bakar yang dapat diisi (pertalait, pertameks, dan selar)
def jenis_bbm(bbm):
    for x, in bbm:
        print(x),

#masukkan data bbm
tipe_bbm =["pertalait", "pertameks", "selar"]
print(tipe_bbm)

#harga untuk pertalait = 10000, pertamek = 12000, selar = 5000
pertalait = 10000
pertameks = 12000
selar = 5000

#buatlah sebuah  fungsi yang mengidentifikasi jenis mobil pemberli dan jumlah liter kebutuhan

def jenis_mobil (nama_brand,jumlah_liter):
    return ()

#panggil fyungsi jenis_mobil
identifikasi_kendaraan = jenis_mobil()
mobil1 = "suf" , 20
mobil2= "avansa" , 30

#panggil fyungsi jenis_mobil
identifikasi_kendaraan = jenis_mobil
print(mobil1)

def hitung_biaya_bbm(liter, harga):
    #rumus
   return ()


#panggil fungsi hitung biaya
total_belanja = hitung_biaya_bbm()

print (liter * harga ) 
print (total_belanja / "a") #harga bbm

# print dengan contoh output yudi  telah membeli tipe bbm selar seharga  12000 dengan total belanja 360000 rupiah
harga = 12000
total_belanja = 360000
print (total_belanja / harga)

#lakukan pembelajaan jika pembeli memiliki uang senilai tertentu lalu hitunglah sampai habis uangnya untuk dibelanjakan
#gunakan recursion
def belanja(uang):
  if(uang >= total_belanja): 
    sisa_uang = "total_belanja" - "uang"
    belanja (sisa_uang)
    print(sisa_uang)
  else:
    sisa_uang = 0
  return sisa_uang

uang = 720000
total_belanja = 360000

print(sisa_uang)

#output jika uang 720000 dan total_belanja 360000
#0
#360000