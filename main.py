harcamalar = []


def dosyadan_oku():
    try:
        with open("harcamalar.txt", "r", encoding="utf-8") as dosya:
            for satir in dosya:
                temiz = satir.strip()
                if temiz != "":
                    harcamalar.append(temiz)
    except FileNotFoundError:
        pass


def dosyaya_kaydet():
    try:
        with open("harcamalar.txt", "w", encoding="utf-8") as dosya:
            for h in harcamalar:
                dosya.write(h + "\n")
    except:
        print("Dosyaya yazma hatasi!")


def harcama_ekle():
    aciklama = input("Harcama aciklamasi: ").strip()
    kategori = input("Kategori (Yemek / Ulasim / Fatura): ").strip()

    if aciklama == "" or kategori == "":
        print("Alanlar bos birakilamaz!")
        return

    try:
        tutar = float(input("Tutar: "))
        if tutar <= 0:
            print("Tutar sifirdan buyuk olmali!")
            return
    except ValueError:
        print("Gecerli bir tutar giriniz!")
        return

    kayit = f"{aciklama},{kategori},{tutar}"
    harcamalar.append(kayit)
    dosyaya_kaydet()
    print("Harcama basariyla eklendi!")


def harcamalari_goster():
    if not harcamalar:
        print("Harcama bulunmuyor.")
    else:
        print("\n--- Harcamalar ---")
        for i in range(len(harcamalar)):
            parca = harcamalar[i].split(",")
            print(f"{i+1}. {parca[0]} | {parca[1]} | {parca[2]} TL")


def toplam_harcama():
    toplam = 0
    for h in harcamalar:
        parca = h.split(",")
        toplam += float(parca[2])
    print(f"Toplam Harcama: {toplam} TL")


def harcama_sil():
    harcamalari_goster()
    if not harcamalar:
        return

    try:
        secim = int(input("Silinecek harcama numarasi: "))
        if 1 <= secim <= len(harcamalar):
            silinen = harcamalar.pop(secim - 1)
            dosyaya_kaydet()
            print(f"{silinen} silindi.")
        else:
            print("Gecersiz numara!")
    except ValueError:
        print("Lutfen sayi giriniz!")


def menu():
    while True:
        print("\n--- Harcama Takip Uygulamasi ---")
        print("1 - Harcama Ekle")
        print("2 - Harcamalari Listele")
        print("3 - Harcama Sil")
        print("4 - Toplam Harcamayi Goster")
        print("5 - Cikis")

        try:
            secim = int(input("Seciminiz: "))
            if secim == 1:
                harcama_ekle()
            elif secim == 2:
                harcamalari_goster()
            elif secim == 3:
                harcama_sil()
            elif secim == 4:
                toplam_harcama()
            elif secim == 5:
                print("Cikis yapiliyor...")
                break
            else:
                print("Gecersiz secim!")
        except ValueError:
            print("Lutfen sadece sayi giriniz!")


dosyadan_oku()
menu()
