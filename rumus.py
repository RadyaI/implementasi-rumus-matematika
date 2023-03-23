print("Hehehe")

def hitung_kecepatan():
    print("Hitung kecepatan sukses")
    jarak = float(input("Masukkan jarak: "))
    waktu = float(input("Masukkan waktu: "))
    kecepatan = jarak * waktu
    print("Kecepatan: ", kecepatan ,"\n")

def luas_segitiga():
    print("Hitung luas segitiga")    
    setengah = 1/2
    alas = float(input("Masukkan Alas: "))
    tinggi = float(input("Masukkan Tinggi: "))
    luas = setengah * (alas * tinggi)
    print("Luas segitiga :", luas, "\n")

def luas_balok():
    print("Hitung luas balok \n")

    print("Hitung panjang x Lebar")
    pl_p = float(input("Masukkan panjang: "))    
    pl_l = float(input("Masukkan lebar: "))
    pl = 2 * pl_p * pl_l
    print("Panjang x lebar : ", pl, "\n")

    print("Hitung panjang x tinggi")
    pt_p = float(input("Masukkan panjang: "))
    pt_t = float(input("Masukkan tinggi: "))
    pt = 2 * pt_p * pt_t
    print("Panjang x Tinggi : ", pt ,"\n")

    print("Hitung lebar x tinggi")
    lt_l = float(input("Masukkan lebar: "))
    lt_t = float(input("Masukkan tinggi: "))
    lt = 2 * lt_l * lt_t
    print("Lebar x tinggi : ", lt , "\n")

    hasil = pl + pt + lt
    print("Jadi hasil luas balok nya adalah: " , hasil, "\n")
    # PENGEN NYOBA YANG RIBET AJA INI 😏

def luas_lingkaran():
        print("Hitung luas bola \n")
        userInput1 = int(input("Pilih yang di ketahui: \n 1.Diameter \n 2.Jari-jari \n Input: "))
        if(userInput1 == 1):
                Diameter = float(input("Masukkan diameter: "))
                userInput2 = int(input("Pilih yang ingin di gunakan: \n 1. 22/7 \n 2. 3,14 \n Input: "))
                if(userInput2 == 1):
                    hasil = 22/7 * (Diameter / 2) * (Diameter / 2)
                    print("\n Diameter: ", Diameter ,"\n","Phi: 22/7","\n","Luas Lingkaran: ", hasil)
                    
                elif(userInput2 == 2):   
                    hasil = 3.14 * (Diameter / 2) * (Diameter / 2)
                    print("\n Diameter: " , Diameter , "\n" , "Phi: 3,14 \n" , "Luas Lingkaran: ", hasil)
                      
                else:
                    print("Gagal!")
                       

        elif(userInput1 == 2):
                jarijari = float(input("Masukkan jari-jari: "))
                userInput3 = int(input("Pilih yang ingin di gunakan: \n 1. 22/7 \n 2. 3,14 \n Input: " ))
                if(userInput3 == 1):
                    hasil = 22/7 * jarijari * jarijari
                    print("\n jari-jari: " , jarijari , "\n" , "Phi: 22/7 \n" ,"Luas Lingkaran: ",hasil)
                    
                elif(userInput3 == 2):              
                    hasil = 3.14 * jarijari * jarijari
                    print("\n jari-jari: " , jarijari , "\n" , "Phi: 3,14 \n" ,"Luas Lingkaran: ",hasil)
                    
                else:
                    print('Gagal!')
                        
        else:
            print("Mohon ulangi!")
                

while True:
    userInput = input("Pilih rumus: \n 1.Hitung kecepatan \n 2.Luas segitiga \n 3.Luas balok \n 4.Luas Lingkaran \n\n ketik x untuk batal \n\n\n Pilih rumus nomor: ")
    if(userInput == '1'):
        hitung_kecepatan()
        break
    elif(userInput =='2'):
        luas_segitiga()
        break
    elif(userInput == '3'):
        luas_balok()
        break
    elif(userInput == '4'):
        luas_lingkaran()  
        break  
    else:   
        print("salah kocak!")
        print("Harap input yang sesuai!!")
        break    
