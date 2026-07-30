from utils import (
    hesap_calistir,
    pozitif_sayi_al,
    sifir_bir_arasi_sayi_al,
    sifir_ve_pozitif_sayi_al,
    secim_al,
    bekle,
    baslik,
    sifirdan_buyuk_bire_esit_sayi_al,
    sonuc_yazdir,
)

from hesaplar import (
    guc_hesabi,
    gerilim_hesabi,
    akim_hesabi,
    direnc_hesabi,
    enerji_hesabi,
    uc_faz_akim_hesabi,
    uc_faz_cos_phi_hesabi,
    uc_faz_gerilim_hesabi,
    uc_faz_guc_hesabi,
    tek_faz_gerilim_dusumu_hesabi,
    uc_faz_gerilim_dusumu_hesabi,
    gerilim_dusumu_yuzdesi_hesabi,
)


def guc_modulu() -> None:
    baslik("GÜÇ HESABI")

    gerilim = sifir_ve_pozitif_sayi_al("Gerilim (V): ")
    akim = sifir_ve_pozitif_sayi_al("Akım (A): ")

    guc = hesap_calistir(guc_hesabi, gerilim, akim)

    if guc is not None:
        sonuc_yazdir([
            f"{'Gerilim':15}: {gerilim:.2f} V",
            f"{'Akım':15}: {akim:.2f} A",
            f"{'Güç':15}: {guc:.2f} W"
        ])

    bekle()


def ohm_modulu() -> None:
    baslik("OHM KANUNU")

    print("1 - Gerilim Hesabı")
    print("2 - Akım Hesabı")
    print("3 - Direnç Hesabı")

    ohm_secim = secim_al("Seçiminiz: ", [1, 2, 3])

    if ohm_secim == 1:
        akim = sifir_ve_pozitif_sayi_al("Akım (A): ")
        direnc = sifir_ve_pozitif_sayi_al("Direnç (Ω): ")

        gerilim = hesap_calistir(
            gerilim_hesabi,
            akim,
            direnc,
        )

        if gerilim is not None:
            sonuc_yazdir([
                f"{'Akım':15}: {akim:.2f} A",
                f"{'Direnç':15}: {direnc:.2f} Ω",
                f"{'Sonuç':15}: {gerilim:.2f} V"
            ])

    elif ohm_secim == 2:
        gerilim = sifir_ve_pozitif_sayi_al("Gerilim (V): ")
        direnc = sifir_ve_pozitif_sayi_al("Direnç (Ω): ")

        akim = hesap_calistir(
            akim_hesabi,
            gerilim,
            direnc
        )

        if akim is not None:
            sonuc_yazdir([
                f"{'Gerilim':15}: {gerilim:.2f} V",
                f"{'Direnç':15}: {direnc:.2f} Ω",
                f"{'Sonuç':15}: {akim:.2f} A"
            ])

    elif ohm_secim == 3:
        gerilim = sifir_ve_pozitif_sayi_al("Gerilim (V): ")
        akim = sifir_ve_pozitif_sayi_al("Akım (A): ")

        direnc = hesap_calistir(
            direnc_hesabi,
            gerilim,
            akim
        )

        if direnc is not None:
            sonuc_yazdir([
                f"{'Gerilim':15}: {gerilim:.2f} V",
                f"{'Akım':15}: {akim:.2f} A",
                f"{'Sonuç':15}: {direnc:.2f} Ω"
            ])

    bekle()


def enerji_modulu() -> None:
    baslik("ENERJİ TÜKETİMİ")

    print("1 - Watt")
    print("2 - Kilowatt")

    birim = secim_al("Seçiminiz: ", [1, 2])

    if birim == 1:
        girilen_guc = sifir_ve_pozitif_sayi_al("Güç (W): ")
        guc_kw = girilen_guc / 1000
    else:
        girilen_guc = sifir_ve_pozitif_sayi_al("Güç (kW): ")
        guc_kw = girilen_guc

    zaman = sifir_ve_pozitif_sayi_al("Çalışma süresi (saat): ")

    enerji = hesap_calistir(
        enerji_hesabi,
        guc_kw,
        zaman
    )

    if enerji is not None:
        sonuc_yazdir([
            f"{'Güç':15}: {guc_kw:.2f} kW",
            f"{'Çalışma süresi':15}: {zaman:.2f} saat",
            f"{'Enerji tüketimi':15}: {enerji:.2f} kWh"
    ])

    bekle()


def hakkinda_modulu() -> None:
    baslik("HAKKINDA")

    print("MKP Toolbox")
    print("Elektrik ve elektronik mühendisliği hesaplama aracı.")
    print("Geliştirici: Kadir Pirinççi")
    print("Sürüm: 0.1")

    bekle()


def uc_faz_modulu() -> None:
    while True:
        baslik("ÜÇ FAZ HESAPLARI")

        print("1 - Aktif Güç Hesabı")
        print("2 - Akım Hesabı")
        print("3 - Gerilim Hesabı")
        print("4 - Güç Faktörü Hesabı")
        print("5 - Geri")

        secim = secim_al("Seçiminiz: ", [1, 2, 3, 4, 5])

        if secim == 1:
            uc_faz_aktif_guc_modulu()

        elif secim == 2:
            uc_faz_akim_modulu()

        elif secim == 3:
            uc_faz_gerilim_modulu()

        elif secim == 4:
            uc_faz_cos_phi_modulu()

        elif secim == 5:
            break


def uc_faz_aktif_guc_modulu() -> None:
    baslik("ÜÇ FAZ AKTİF GÜÇ HESABI")

    gerilim = sifir_ve_pozitif_sayi_al("Gerilim (V): ")
    akim = sifir_ve_pozitif_sayi_al("Akım (A): ")
    cos_phi = sifir_bir_arasi_sayi_al("Güç faktörü (cosφ): ")

    guc = hesap_calistir(
        uc_faz_guc_hesabi,
        gerilim,
        akim,
        cos_phi
    )

    if guc is not None:
        sonuc_yazdir([
            f"{'Gerilim':15}: {gerilim:.2f} V",
            f"{'Akım':15}: {akim:.2f} A",
            f"{'Güç faktörü':15}: {cos_phi:.2f}",
            f"{'Aktif güç':15}: {guc:.2f} W"
        ])

    bekle()


def uc_faz_akim_modulu() -> None:
    baslik("ÜÇ FAZ AKIM HESABI")

    gerilim = pozitif_sayi_al("Gerilim (V): ")
    aktif_guc = sifir_ve_pozitif_sayi_al("Aktif Güç (W): ")
    cos_phi = sifirdan_buyuk_bire_esit_sayi_al("Güç faktörü (cosφ): ")

    akim = hesap_calistir(
        uc_faz_akim_hesabi,
        gerilim,
        aktif_guc,
        cos_phi
    )

    if akim is not None:
        sonuc_yazdir([
            f"{'Gerilim':15}: {gerilim:.2f} V",
            f"{'Aktif Güç':15}: {aktif_guc:.2f} W",
            f"{'Güç faktörü':15}: {cos_phi:.2f}",
            f"{'Akım':15}: {akim:.2f} A"
        ])

    bekle()


def uc_faz_gerilim_modulu() -> None:
    baslik("ÜÇ FAZ GERİLİM HESABI")

    aktif_guc = sifir_ve_pozitif_sayi_al("Aktif Güç (W): ")
    akim = pozitif_sayi_al("Akım (A): ")
    cos_phi = sifirdan_buyuk_bire_esit_sayi_al("Güç faktörü (cosφ): ")

    gerilim = hesap_calistir(
        uc_faz_gerilim_hesabi,
        aktif_guc,
        akim,
        cos_phi
    )

    if gerilim is not None:
        sonuc_yazdir([
            f"{'Aktif Güç':15}: {aktif_guc:.2f} W",
            f"{'Akım':15}: {akim:.2f} A",
            f"{'Güç faktörü':15}: {cos_phi:.2f}",
            f"{'Gerilim':15}: {gerilim:.2f} V"
        ])

    bekle()


def uc_faz_cos_phi_modulu() -> None:
    baslik("ÜÇ FAZ GÜÇ FAKTÖRÜ HESABI")

    aktif_guc = sifir_ve_pozitif_sayi_al("Aktif Güç (W): ")
    gerilim = pozitif_sayi_al("Gerilim (V): ")
    akim = pozitif_sayi_al("Akım (A): ")

    cos_phi = hesap_calistir(
        uc_faz_cos_phi_hesabi,
        aktif_guc,
        gerilim,
        akim
    )

    if cos_phi is not None:
        sonuc_yazdir([
            f"{'Aktif Güç':15}: {aktif_guc:.2f} W",
            f"{'Gerilim':15}: {gerilim:.2f} V",
            f"{'Akım':15}: {akim:.2f} A",
            f"{'Güç faktörü':15}: {cos_phi:.2f}"
        ])

    bekle()


def gerilim_dusumu_modulu() -> None:
    while True:
        baslik("GERİLİM DÜŞÜMÜ HESABI")

        print("1 - Tek Faz")
        print("2 - Üç Faz")
        print("3 - Gerilim Düşümü %")
        print("4 - Geri")

        secim = secim_al("Seçiminiz: ", [1, 2, 3, 4])
        if secim == 1:
            tek_faz_gerilim_dusumu_modulu()
        elif secim == 2:
            uc_faz_gerilim_dusumu_modulu()
        elif secim == 3:
            gerilim_dusumu_yuzdesi_modulu()
        elif secim == 4:
            break


def tek_faz_gerilim_dusumu_modulu() -> None:
    baslik("TEK FAZ GERİLİM DÜŞÜMÜ HESABI")

    ozdirenc = pozitif_sayi_al("Özdirenç (Ω.mm²/m): ")
    uzunluk = pozitif_sayi_al("Hat uzunluğu (m): ")
    akim = pozitif_sayi_al("Akım (A): ")
    kesit = pozitif_sayi_al("İletken kesiti (mm²): ")

    gerilim_dusumu = hesap_calistir(
        tek_faz_gerilim_dusumu_hesabi,
        ozdirenc,
        uzunluk,
        akim,
        kesit,
    )

    if gerilim_dusumu is not None:
        sonuc_yazdir([
            f"{'Akım':15}: {akim:.2f} A",
            f"{'Özdirenç':15}: {ozdirenc:.2f} Ω.mm²/m",
            f"{'Hat uzunluğu':15}: {uzunluk:.2f} m",
            f"{'İletken kesiti':15}: {kesit:.2f} mm²",
            f"{'Gerilim düşümü':15}: {gerilim_dusumu:.2f} V"
        ])

    bekle()


def uc_faz_gerilim_dusumu_modulu() -> None:
    baslik("ÜÇ FAZ GERİLİM DÜŞÜMÜ HESABI")

    ozdirenc = pozitif_sayi_al("Özdirenç (Ω.mm²/m): ")
    uzunluk = pozitif_sayi_al("Hat uzunluğu (m): ")
    akim = pozitif_sayi_al("Akım (A): ")
    kesit = pozitif_sayi_al("İletken kesiti (mm²): ")

    gerilim_dusumu = hesap_calistir(
        uc_faz_gerilim_dusumu_hesabi,
        ozdirenc,
        uzunluk,
        akim,
        kesit,
    )

    if gerilim_dusumu is not None:
        sonuc_yazdir([
            f"{'Akım':15}: {akim:.2f} A",
            f"{'Özdirenç':15}: {ozdirenc:.2f} Ω.mm²/m",
            f"{'Hat uzunluğu':15}: {uzunluk:.2f} m",
            f"{'İletken kesiti':15}: {kesit:.2f} mm²",
            f"{'Gerilim düşümü':15}: {gerilim_dusumu:.2f} V"
        ])

    bekle()


def gerilim_dusumu_yuzdesi_modulu() -> None:
    baslik("GERİLİM DÜŞÜMÜ YÜZDESİ HESABI")

    gerilim_dusumu = sifir_ve_pozitif_sayi_al(
        "Gerilim düşümü (V): "
        )
    sistem_gerilimi = pozitif_sayi_al(
        "Sistem gerilimi (V): "
    )

    yuzde = hesap_calistir(
        gerilim_dusumu_yuzdesi_hesabi,
        gerilim_dusumu,
        sistem_gerilimi
    )

    if yuzde is not None:
        sonuc_yazdir([
            f"{'Gerilim düşümü':20}: {gerilim_dusumu:.2f} V",
            f"{'Sistem gerilimi':20}: {sistem_gerilimi:.2f} V",
            f"{'Düşüm yüzdesi':20}: {yuzde:.2f} %"
        ])

    bekle()