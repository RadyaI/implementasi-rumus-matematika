print("\n\n ===== KALKULATOR ====")


def penjumlahan():
    print("\n Penjumlahan \n")
    angka1 = int(input("Masukkan angka: "))
    angka2 = int(input("Masukkan angka: "))
    hasil_jumlah = angka1 + angka2
    print("Hasil jumlah: ", hasil_jumlah, "\n")


def pengurangan():
    print("\n Pengurangan \n")
    angka1 = int(input("Masukkan angka: "))
    angka2 = int(input("Masukkan angka: "))
    hasil = angka1 - angka2
    print("Hasil pengurangan: ", hasil, "\n")


def perkalian():
    print("\n Perkalian \n")
    angka1 = int(input("Masukkan angka: "))
    angka2 = int(input("Masukkan angka: "))
    hasil = angka1 * angka2
    print("Hasil perkalian: ", hasil, "\n")


def pembagian():
    print("\n Pembagian \n")
    angka1 = int(input("Masukkan angka: "))
    angka2 = int(input("Masukkan angka: "))
    hasil = angka1 / angka2
    print("Hasil pembagian: ", hasil, "\n")


num1 = 0
operator = '+'


while True:
    userInput = int(input(
        "Pilih salah satu: \n 1. Kalkulator sederhana \n 2. Kalkulator normal \n Pilih nomor: "))
    if (userInput == 1):
        userInput_ks = int(input(
            "\n Pilih operator aritmatika: \n 1. Penjumlahan \n 2. Pengurangan \n 3. Perkalian \n 4. Pembagian \n Pilih Nomor: "))
        if (userInput_ks == 1):
            penjumlahan()
            break
        elif (userInput_ks == 2):
            pengurangan()
            break
        elif (userInput_ks == 3):
            perkalian()
            break
        elif (userInput_ks == 4):
            pembagian()
            break
        else:
            break
    elif (userInput == 2):
        print("\nBelum jadi hehe")
        break
    elif (userInput == 0):
        print("\nBatal")
        break
    else:
        print("Salah Input!")
        break
