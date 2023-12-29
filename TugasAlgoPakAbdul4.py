import os
import sys

data = []
filename = ''

def filenama():
    global filename, data
    print("[File Recognition]")
    filename = input("Masukan Nama File : ").lower()
    if filename.lower() == "exit":
        sys.exit("Exiting the program.")    
    try:
        with open(f"{filename}.txt", 'r') as file:
            data = file.readlines()
        print(f"File {filename[6:]}.txt Berhasil ditemukan ")
        return main()
    except FileNotFoundError:
        print("File tidak ditemukan")
        print("Membuat File Baru....")
        with open(f"{filename}.txt", "w") as file:
            file.close()
        return main()

def clear():
    os.system('cls')

def lihatnilai():
    global filename, data
    print("[4] Lihat Semua Nilai ")
    print(" NO.  |   NAMA   | PRAK1  | PRAK2  | PRAK3  | RATA RATA ")
    print("========================================================")
    for idx, user in enumerate(data, start=1):
        stripped = user.strip().split(' ')
        nilai1 = stripped[-3]
        nilai2 = stripped[-2]
        nilai3 = stripped[-1]
        rata_rata = (int(nilai1) + int(nilai2) + int(nilai3)) / 3
        nama = ' '.join(stripped[0:stripped.index(nilai1)])
        print(" {} | {} | {} | {} | {} | {} ".format(
            str(idx).ljust(4),
            nama.ljust(8),
            str(nilai1).ljust(6),
            str(nilai2).ljust(6),
            str(nilai3).ljust(6),
            str(int(rata_rata)).ljust(6).rjust(5)
        ))
    return main()

def inputnamalihatnilai():
    print("[1] Lihat Nilai ")
    global filename, data
    name = input("Masukan Nama : ")
    userFound = False
    for user in data:
        stripped = user.strip().split(' ')
        nilai1 = stripped[-3]
        nilai2 = stripped[-2]
        nilai3 = stripped[-1]
        rata_rata = (int(nilai1) + int(nilai2) + int(nilai3)) / 3
        nama = ' '.join(stripped[0:stripped.index(nilai1)])
        if name == nama:
            print(f"{nama} = Nilai1: {nilai1}, Nilai2: {nilai2}, Nilai3: {nilai3}, Rata Rata: {rata_rata}")
            userFound = True
            return main()
    if not userFound:
        print("Nama tidak ditemukan!")
        return main()

def updatenilai():
    print("[2] Update Nilai")
    global filename, data
    name = input("Masukan Nama : ")
    userFound = False
    for user in data:
        stripped = user.strip().split(' ')
        nilai1 = stripped[-3]
        nilai2 = stripped[-2]
        nilai3 = stripped[-1]
        nama = ' '.join(stripped[0:stripped.index(nilai1)])
        if name == nama:
            fulldata = [nama, int(nilai1), int(nilai2), int(nilai3)]
            nilaiberapa = input("Edit Nilai Ke : ")
            try:
                nilaiLama = fulldata[int(nilaiberapa)]
                nilaibaru = input("Masukan Nilai Baru : ")
                fulldata[int(nilaiberapa)] = nilaibaru
                data[data.index(user)] = f"{nama} {fulldata[1]} {fulldata[2]} {fulldata[3]}\n"
                print("Berhasil Diupdate")
                userFound = True
                return main()
            except:
                print("Nilai tidak valid")
                return updatenilai()
    if not userFound:
        print("Nama tidak ditemukan!")
        return main()

def hapusnilai():
    print("[3] Hapus Nilai ")
    global filename, data
    name = input("Masukan Nama : ")
    userFound = False
    for user in data:
        stripped = user.strip().split(' ')
        nilai1 = stripped[-3]
        nilai2 = stripped[-2]
        nilai3 = stripped[-1]
        nama = ' '.join(stripped[0:stripped.index(nilai1)])
        if name == nama:
            data.remove(user)
            userFound = True
            print("berhasil di hapus")
            return main()
    if not userFound:
        print("User tidak ditemukan!")
        return main()

def simpanfile():
    global filename, data
    with open(f"{filename}.txt", 'w') as files:
        files.write(''.join(data))
    print("Perubahan berhasil disimpan.")
    return main()

def inputnilai():
    print("[6] Input Nilai")
    global filename, data
    try:
        baris = int(input("Masukan Baris Line : "))

        nama = input("Masukan Nama : ")
        userFound = False

        for line in data:
            if nama in line:
                userFound = True
                print("User sudah terdaftar")
                return main()

        if not userFound:
            nilai1 = int(input("Masukan Nilai 1 : "))
            nilai2 = int(input("Masukan Nilai 2 : "))
            nilai3 = int(input("Masukan Nilai 3 : "))

            # Extend the data list if needed
            while len(data) < baris:
                data.append('\n')

            data[baris - 1] = f"{nama} {nilai1} {nilai2} {nilai3}\n"
            with open(f"{filename}.txt", "w") as file:
                file.writelines(data)
            print("Data Berhasil Di input.")
            return main()

    except ValueError:
        print("Baris harus angka (int) !")
        return main()
    
def main():
    global filename, data
    
    print("""[MENU]
1.> Lihat Nilai
2.> Update Nilai
3.> Hapus Data
4.> Lihat Semua Nilai
5.> Simpan ke file
6.> Input Data
0.> Keluar""")
    opsi = input(">>> ")
    if opsi == "1":
        clear()
        inputnamalihatnilai()
    elif opsi == "2":
        clear()
        updatenilai()
    elif opsi == "3":
        clear()
        hapusnilai()
    elif opsi == "4":
        clear()
        lihatnilai()
    elif opsi == "5":
        clear()
        simpanfile()
    elif opsi == "0":
        clear()
        sys.exit()
    elif opsi == "6":
        clear()
        inputnilai()

if __name__ == "__main__":
    clear()
    filenama()
    clear()
    while True:
        main()
