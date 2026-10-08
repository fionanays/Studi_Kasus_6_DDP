import json

with open("std5.json", "r", encoding = "utf-8") as f:
    data = json.load(f)

def tambah_data(nama, nilai, kelas):
    data.append({
        "nama": nama,
        "nilai": nilai,
        "kelas": kelas
    })

    return "Data berhasil ditambahkan!"

def simpan_file():
    with open("std5.json", "w", encoding = "utf-8") as f:
        json.dump(data, f, indent = 4, )
        return "Tersimpan rekap nilai siswa ke std5.json"

def rekap_nilai():
    while True:
        print("========== REKAP NILAI ==========")
        print("1. Lihat data nilai")
        print("2. Tambah data")
        print("3. Keluar")

        pilihan = input("Masukkan pilihan anda: ")

        if pilihan == "1":
            print(data)
        elif pilihan == "2":
            nama = input("Masukkan nama siswa: ")
            nilai = input("Masukkan nilai siswa: ")
            kelas = input("Masukkan kelas siswa: ")

            print(f"Data dengan nama {nama}, nilai {nilai}, kelas {kelas} berhasil ditambahkan")
            tambah_data(nama, nilai, kelas)

            simpan_file()
        elif pilihan == "3":
            ("Program selesai")
            break

        else:
            print("Ulangi lagi")

rekap_nilai()