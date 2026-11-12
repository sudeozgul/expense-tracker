harcamalar = []


def dosyadan_oku():
    try:
        with open("harcamalar.txt", "r", encoding="utf-8") as dosya:
            for satir in dosya:
                temiz = satir.strip()

                if temiz:
                    harcamalar.append(temiz)

    except FileNotFoundError:
        pass

    except OSError as hata:
        print(f"Dosya okuma hatasi: {hata}")


def dosyaya_kaydet():
    try:
        with open("harcamalar.txt", "w", encoding="utf-8") as dosya:
            for h in harcamalar:
                dosya.write(h + "\n")

    except OSError as hata:
        print(f"Dosyaya yazma hatasi: {hata}")


def harcama_ekle():
    aciklama = input("Harcama aciklamasi: ").strip()
    kategori = input("Kategori (Yemek / Ulasim / Fatura): ").strip()

    if aciklama == "" or kategori == "":
        print("Alanlar bos birakilamaz!")
        return

    try:
        tutar_girdisi = input("Tutar: ").replace(",", ".")
        tutar = float(tutar_girdisi)

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
        return

    print("\n--- Harcamalar ---")

    for i, h in enumerate(harcamalar, start=1):
        parca = h.split(",")

        if len(parca) == 3:
            print(f"{i}. {parca[0]} | {parca[1]} | {parca[2]} TL")
        else:
            print(f"{i}. Gecersiz harcama kaydi")


def toplam_harcama():
    toplam = 0

    for h in harcamalar:
        parca = h.split(",")

        if len(parca) == 3:
            try:
                toplam += float(parca[2])
            except ValueError:
                print("Gecersiz harcama kaydi atlandi.")

    print(f"Toplam Harcama: {toplam:.2f} TL")


def harcama_sil():
    harcamalari_goster()

    if not harcamalar:
        return

    secim = input("Silinecek harcama numarasi: ").strip()

    if not secim.isdigit():
        print("Lutfen gecerli bir numara giriniz!")
        return

    secim = int(secim)

    if 1 <= secim <= len(harcamalar):
        silinen = harcamalar.pop(secim - 1)
        dosyaya_kaydet()
        print(f"{silinen} silindi.")
    else:
        print("Gecersiz numara!")


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
