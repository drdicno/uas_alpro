"""
Nama  : Dicky Novanda Syaifulah
NM    : 20083000068  
Kelas : 2C
PERHITUNGAN GAJI KARYAWAN CV. LOGOS
"""

import datetime
x = datetime.datetime.now()

#print("Tanggal = " + x.strftime("%d") , x.strftime("%B") , x.strftime("%Y"))
print("=====================================")
print(" PERHITUNGAN GAJI KARYAWAN CV. LOGOS ")
print("=====================================")

kode_gol=[1,2,3]
gaji_gol=[2500000,4500000,6500000]
kode_jk=["l","p"]
jeniskel=["Laki - laki","Perempuan"]
kode_kwn=["s","b"]
status_kwn=["Sudah menikah","Belum menikah"]

#input nama karyawan
nama=input("Tuliskan Nama Anda      = ")

#input golongan
sts_gol=int(input("Golongan anda           = "))

#ambil kode nama golongan yang dipilih
i=0
while i<len(kode_gol):
    #jika value pada kode golongan[i] == sts_golongan
    if kode_gol[i] == sts_gol:
        data_gol = kode_gol[i]
        data_gaji = gaji_gol[i]
        #print(str(data_gaji))
    #jika tidak cocok, lanjut ke i berikutnya
    i+=1
    

#input jenis kelamin
jkel=str.lower(input("Jenis kelamin (L/P)     = "))
i=0
while i<len(kode_jk):
    #jika value pada kode jk[i] == jenis kel pada inputan
    if kode_jk[i] == jkel:
        data_jk = kode_jk[i]
        #print(data_jk)
    #jika tidak cocok, lanjut ke i berikutnya
    i+=1
    

#input status kawin
sts_kawin=str.lower(input("Status kawin (S/B)      = "))
i=0
while i<len(kode_kwn):
    #jika value pada kode kwn[i] == status kwn pada inputan
    if kode_kwn[i] == sts_kawin:
        data_kwn = kode_kwn[i]
        sts1_kwn = status_kwn[i]
        #print(data_kwn)

    #jika tidak cocok, lanjut ke i berikutnya
    i+=1

#cek data kawin dan punya anak
if data_kwn == "s":
    data_anak=str.lower(input("Apakah Punya Anak (Y/T)= "))
    #jika punya anak
    if data_anak == "y":
        jum_anak=input("Jumlah anak = ")
    else : jum_anak = 0
else : print("Belum kawin")

#Menghitung gaji pokok
#print("Gaji pokok = Rp " + str(data_gaji))

#Menghitung tunjangan istri
if data_jk == "l" and data_kwn == "s":
    if data_gol == 1: tun_istri = 0.01 * data_gaji
    elif data_gol == 2: tun_istri = 0.03 * data_gaji
    elif data_gol == 3: tun_istri = 0.05 * data_gaji
else: tun_istri = 0
#print("Tunjangan istri = " + str(tun_istri))

#Menghitung tunjangan anak
if data_kwn == "s" and data_anak == "y":
    tun_anak = 0.02 * data_gaji
else : tun_anak = 0
#print("tunjangan anak = " + str(tun_anak))

#Menghitung gaji bruto
gaji_bruto = data_gaji + tun_anak + tun_istri
#print("Gaji bruto = " + str(gaji_bruto))

#menghitung biaya jabatan
b_jabatan = 0.05 * gaji_bruto
#print(b_jabatan)

#iuran pensiun
i_pensiun = 15500

#iuran organisasi
i_org = 3500

#gaji netto
gaji_netto = gaji_bruto - b_jabatan - i_pensiun - i_org
#print("gaji netto = " + str(gaji_netto))

print("===================================")
print("Slip Gaji")
print("Tanggal = " + x.strftime("%d") , x.strftime("%B") , x.strftime("%Y"))
print()
print("Nama             = " + nama)
print("Golongan         = " + str(data_gol))
print("Jenis Kelamin    = " + data_jk)
print("Status Menikah   = " + sts1_kwn)
print("Gaji Pokok       = Rp " + str(data_gaji))
print("Tunjangan Istri  = Rp " + str(tun_istri))
print("Tunjangan Anak   = Rp " + str(tun_anak))
print(">> Gaji Bruto    = Rp " + str(gaji_bruto))
print("===================================")
print("Biaya Jabatan    = Rp " + str(b_jabatan))
print("Iuran Pensiun    = Rp " + str(i_pensiun))
print("Iuran Organisasi = Rp " + str(i_org))
print(">> Gaji Netto    = Rp " + str(gaji_netto))
print()