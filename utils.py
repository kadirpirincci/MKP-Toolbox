from typing import Sequence, Callable, Any, Optional


def sayi_al(mesaj: str) -> float:
    while True:
        try:
            return float(input(mesaj))
        except ValueError:
            print("Hatalı giriş! Lütfen sayısal bir değer giriniz.")


def pozitif_sayi_al(mesaj: str) -> float:
    while True:
        sayi = sayi_al(mesaj)

        if sayi > 0:
            return sayi

        print("Lütfen pozitif bir değer giriniz.")


def sifir_ve_pozitif_sayi_al(mesaj: str) -> float:
    while True:
        sayi = sayi_al(mesaj)

        if sayi >= 0:
            return sayi

        print("Lütfen sıfır veya pozitif bir değer giriniz.")


def sifirdan_buyuk_bire_esit_sayi_al(mesaj: str) -> float:
    while True:
        sayi = sayi_al(mesaj)

        if 0 < sayi <= 1:
            return sayi

        print("Lütfen 0'dan büyük ve 1'e eşit veya küçük bir değer giriniz.")


def sifir_bir_arasi_sayi_al(mesaj: str) -> float:
    while True:
        sayi = sayi_al(mesaj)

        if 0 <= sayi <= 1:
            return sayi

        print("Lütfen 0 ile 1 arasında bir değer giriniz.")


def secim_al(mesaj: str, secenekler: Sequence[int]) -> int:
    while True:
        try:
            secim = int(input(mesaj))

            if secim in secenekler:
                return secim

            print("Geçersiz seçim!")

        except ValueError:
            print("Hatalı giriş!")


def ana_menu() -> None:
    print()
    print("=========================")
    print("      MKP Toolbox")
    print("=========================")
    print()
    print("1 - Güç Hesabı")
    print("2 - Ohm Kanunu")
    print("3 - Enerji Tüketimi")
    print("4 - Hakkında")
    print("5 - Çıkış")


def bekle() -> None:
    print()
    input("Ana menüye dönmek için Enter'a basınız...")


def baslik(isim: str) -> None:
    print()
    print("=================================")
    print(f"{isim:^33}")
    print("=================================")
    print()


def sonuc_yazdir(satirlar: Sequence[str]) -> None:
    print()
    print("---------------------------------")
    for satir in satirlar:
        print(satir)
    print("---------------------------------")


def hesap_calistir(fonksiyon: Callable[..., Any], *parametreler: Any) -> Optional[Any]:
    try:
        return fonksiyon(*parametreler)

    except ValueError:
        return None