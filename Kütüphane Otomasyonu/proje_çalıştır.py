
from kütüphane import *

print("""***********************************

Kütüphane Programına Hoşgeldiniz.

İşlemler;

1. Kitapları Göster

2. Kitap Sorgulama

3. Kitap Ekle

4. Kitap Sil 

5. Baskı Yükselt

Çıkmak için 'q' ya basın.
***********************************""")

kutuphane = Kutuphane()

while True:
    islem = input("Yapacağınız İşlem:")

    if (islem == "q"):
        print("Program Sonlandırılıyor.....")
        time.sleep(2)
        print("Yine bekleriz....")
        break
    elif (islem == "1"):
        kutuphane.kitaplari_goster()

    elif (islem == "2"):
        isim = input("Hangi kitabı istiyorsunuz ? ")
        print("Kitap Sorgulanıyor...")
        time.sleep(2)

        kutuphane.kitap_sorgula(isim)

    elif (islem == "3"):
        isim = input("İsim:")
        yazar = input("Yazar:")
        yayinevi = input("Yayınevi:")
        tur = input("Tür:")
        baski = int(input("Baskı:"))

        yeni_kitap = Kitap(isim,yazar,yayinevi,tur,baski)
        if kutuphane.kayit_kontrol(isim):
            print("Kitap ekleniyor....")
            time.sleep(2)
            kutuphane.kitap_ekle(yeni_kitap)
            print("Kitap Eklendi....")
        else:
            print("Bu kitap zaten mevcut, tekrar ekleyemezsiniz!!")

    elif (islem == "4"):
        isim = input("Hangi kitabı silmek istiyorsunuz ?")
        cevap = input("Emin misiniz ? (E/H)").upper()
        if (cevap == "E"):
            kutuphane.kitap_sil(isim)
        elif(cevap=="H"):
            print("İşlem iptal edildi")
        else:
            print("Geçersiz bir harf girdiniz!!!")
            time.sleep(2)
            print("Ana menüye yönlendiriliyorsunuz!")
            time.sleep(2)

    elif (islem == "5"):
        isim = input("Hangi kitabın baskısını yükseltmek istiyorsunuz ?")
        kutuphane.baski_yukselt(isim)
    else:
        print("Geçersiz İşlem...")
