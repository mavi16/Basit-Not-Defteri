# Developer Mavi16

def not_defteri():
    def not_ekle():
        baslik = input("Not başlığını girin: ")
        not_icerik = input("Not içeriğini girin: ")
        notlar[baslik] = not_icerik

    def not_goruntule():
        baslik = input("Görüntülemek istediğiniz notun başlığını girin: ")
        if baslik in notlar:
            print(f"{baslik}: {notlar[baslik]}")
        else:
            print("Belirtilen başlıkta bir not bulunamadı.")

    def not_sil():
        baslik = input("Silmek istediğiniz notun başlığını girin: ")
        if baslik in notlar:
            del notlar[baslik]
            print("Not başarıyla silindi.")
        else:
            print("Belirtilen başlıkta bir not bulunamadı.")
    
    # Seçenekleri düzenliyoruz
    notlar = {}
    secenekler = {
        "1": not_ekle,
        "2": not_goruntule,
        "3": not_sil
    }

    # Döngüyü ayarlıyoruz
    while True:
        print("Not Defteri")
        print("1. Not Ekle")
        print("2. Not Görüntüle")
        print("3. Not Sil")
        print("Q. Çıkış")

        secim = input("Bir seçenek girin: ")

        if secim == "Q":
            break
        elif secim in secenekler:
            secenekler[secim]()
        else:
            print("Geçersiz seçenek.")

not_defteri()
