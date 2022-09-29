printf ("selamat datang di spbu upnvj")

identitas_pembeli {
    printf"\nNama   : %s"%nama
    printf"nomor hp   : %s"%nomorhp
    printf"pekerjaan   : %d"%pekerjaan
}

biodata_pembeli=identitas_pembeli

jenis_bbm {
    printf"pertalite"%pertalite
    printf"pertamax"%pertamax
    printf"solar"%solar
}

tipebbm=jenis_bbm
printf"\ntipe bbm   : %s"%tipebbm

harga_bbm {
    pertalite=10000;
    pertamax=120000;
    solar=5000;
}

jenis_mobil {
    printf"\nmerk   : %s"%merk_mobil
    printf"jumlah liter   : %s"%jml_liter
}

identifikasi_kendaraan=jenis_mobil

total_bbm {
    tipebbm=jml_liter*harga_bbm
}

total_belanja=total_bbm

print("tuan/nyonya".format(nama) "telah membeli{}".format(jenis_bbm) "dengan jumlah liter{}".format(jml_liter) "serta total harga{}".format(total_belanja))

def belanja(uang):
  if(uang >= total_belanja):
    sisa_uang = 
    belanja (sisa_uang)
    print(sisa_uang)
  else:
    sisa_uang = 0
  return sisa_uang

print("tuan/nyonya kembalian anda adalah senilai".format(sisa_uang))
