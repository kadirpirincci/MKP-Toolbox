from math import sqrt


def guc_hesabi(gerilim: float, akim: float) -> float:
    """
    Gerilim ve akım değerlerinden elektrik gücünü hesaplar.

    Parametreler:
        gerilim (float): Gerilim değeri (V)
        akim (float): Akım değeri (A)

    Döndürür:
        float: Güç değeri (W)
    """
    return gerilim * akim


def akim_hesabi(gerilim: float, direnc: float) -> float:
    """
    Gerilim ve direnç değerlerinden akımı hesaplar.

    Parametreler:
        gerilim (float): Gerilim değeri (V)
        direnc (float): Direnç değeri (Ω)

    Döndürür:
        float: Akım değeri (A)
    """

    if direnc == 0:
        raise ValueError("Direnç sıfır olamaz.")

    return gerilim / direnc


def gerilim_hesabi(akim: float, direnc: float) -> float:
    """
    Akım ve direnç değerlerinden gerilimi hesaplar.

    Parametreler:
        akim (float): Akım değeri (A)
        direnc (float): Direnç değeri (Ω)

    Döndürür:
        float: Gerilim değeri (V)
    """
    return akim * direnc


def direnc_hesabi(gerilim: float, akim: float) -> float:
    """
    Gerilim ve akım değerlerinden direnci hesaplar.

    Parametreler:
        gerilim (float): Gerilim değeri (V)
        akim (float): Akım değeri (A)

    Döndürür:
        float: Direnç değeri (Ω)
    """

    if akim == 0:
        raise ValueError("Akım sıfır olamaz.")
    return gerilim / akim


def enerji_hesabi(guc: float, zaman: float) -> float:
    """
    Güç ve çalışma süresinden enerji tüketimini hesaplar.

    Parametreler:
        guc (float): Güç değeri (kW)
        zaman (float): Çalışma süresi (saat)

    Döndürür:
        float: Enerji değeri (kWh)
    """
    return guc * zaman


def uc_faz_guc_hesabi(
        gerilim: float,
        akim: float,
        cos_phi: float
) -> float:
    """
    Üç fazlı sistemde gerilim, akım ve güç faktöründen gücü hesaplar.

    Parametreler:
        gerilim (float): Gerilim değeri (V)
        akim (float): Akım değeri (A)
        cos_phi (float): Güç faktörü

    Döndürür:
        float: Aktif güç değeri (W)
    """

    if gerilim < 0:
        raise ValueError("Gerilim negatif olamaz.")

    if akim < 0:
        raise ValueError("Akım negatif olamaz.")

    if not (0 <= cos_phi <= 1):
        raise ValueError("Güç faktörü 0 ile 1 arasında olmalıdır.")

    return sqrt(3) * gerilim * akim * cos_phi


def uc_faz_akim_hesabi(
        gerilim: float,
        guc: float,
        cos_phi: float
) -> float:
    """
    Üç fazlı sistemde gerilim, güç ve güç faktöründen akımı hesaplar.

    Parametreler:
        gerilim (float): Gerilim değeri (V)
        guc (float): Güç değeri (W)
        cos_phi (float): Güç faktörü

    Döndürür:
        float: Akım değeri (A)
    """

    if gerilim <= 0:
        raise ValueError("Gerilim pozitif olmalıdır.")

    if guc <= 0:
        raise ValueError("Güç pozitif olmalıdır.")

    if not (0 < cos_phi <= 1):
        raise ValueError("Güç faktörü 0'dan büyük ve 1'e eşit veya küçük olmalıdır.")

    return guc / (sqrt(3) * gerilim * cos_phi)


def uc_faz_gerilim_hesabi(
        guc: float,
        akim: float,
        cos_phi: float
) -> float:
    """
    Üç fazlı sistemde akım, güç ve güç faktöründen gerilimi hesaplar.

    Parametreler:
        guc (float): Güç değeri (W)
        akim (float): Akım değeri (A)
        cos_phi (float): Güç faktörü

    Döndürür:
        float: Gerilim değeri (V)
    """

    if akim <= 0:
        raise ValueError("Akım pozitif olmalıdır.")

    if guc <= 0:
        raise ValueError("Güç pozitif olmalıdır.")

    if not (0 < cos_phi <= 1):
        raise ValueError("Güç faktörü 0'dan büyük ve 1'e eşit veya küçük olmalıdır.")

    return guc / (sqrt(3) * akim * cos_phi)


def uc_faz_cos_phi_hesabi(
        guc: float,
        gerilim: float,
        akim: float
) -> float:
    """
    Üç fazlı sistemde güç, gerilim ve akımdan güç faktörünü hesaplar.

    Parametreler:
        guc (float): Güç değeri (W)
        gerilim (float): Gerilim değeri (V)
        akim (float): Akım değeri (A)

    Döndürür:
        float: Güç faktörü
    """
    if guc <= 0:
        raise ValueError("Güç pozitif olmalıdır.")

    if gerilim <= 0:
        raise ValueError("Gerilim pozitif olmalıdır.")

    if akim <= 0:
        raise ValueError("Akım pozitif olmalıdır.")

    cos_phi = guc / (sqrt(3) * gerilim * akim)

    if not (0 < cos_phi <= 1):
        raise ValueError(
            "Girilen değerlerle hesaplanan güç faktörü fiziksel olarak geçerli değildir."
        )
    return cos_phi


def tek_faz_gerilim_dusumu_hesabi(
        ozdirenc: float,
        uzunluk: float,
        akim: float,
        kesit: float
) -> float:
    """
    Tek fazlı sistemde iletkenin özdirenci, uzunluğu, akımı ve kesit alanından gerilim düşümünü hesaplar.

    Parametreler:
        ozdirenc (float): İletkenin özdirenci (Ω·mm²/m)
        uzunluk (float): İletkenin uzunluğu (m)
        akim (float): Akım değeri (A)
        kesit (float): İletkenin kesit alanı (mm²)

    Döndürür:
        float: Gerilim düşümü (V)
    """
    if ozdirenc <= 0:
        raise ValueError("Özdirenç pozitif olmalıdır.")

    if uzunluk <= 0:
        raise ValueError("Uzunluk pozitif olmalıdır.")

    if akim <= 0:
        raise ValueError("Akım pozitif olmalıdır.")

    if kesit <= 0:
        raise ValueError("Kesit alanı pozitif olmalıdır.")

    return 2 * ozdirenc * uzunluk * akim / kesit


def uc_faz_gerilim_dusumu_hesabi(
        ozdirenc: float,
        uzunluk: float,
        akim: float,
        kesit: float
) -> float:
    """
    Üç fazlı sistemde iletkenin özdirenci, uzunluğu, akımı ve kesit alanından gerilim düşümünü hesaplar.

    Parametreler:
        ozdirenc (float): İletkenin özdirenci (Ω·mm²/m)
        uzunluk (float): İletkenin uzunluğu (m)
        akim (float): Akım değeri (A)
        kesit (float): İletkenin kesit alanı (mm²)

    Döndürür:
        float: Gerilim düşümü (V)
    """
    if ozdirenc <= 0:
        raise ValueError("Özdirenç pozitif olmalıdır.")

    if uzunluk <= 0:
        raise ValueError("Uzunluk pozitif olmalıdır.")

    if akim <= 0:
        raise ValueError("Akım pozitif olmalıdır.")

    if kesit <= 0:
        raise ValueError("Kesit alanı pozitif olmalıdır.")

    return sqrt(3) * ozdirenc * uzunluk * akim / kesit


def gerilim_dusumu_yuzdesi_hesabi(
        gerilim_dusumu: float,
        sistem_gerilimi: float
) -> float:
    """
    Sistem gerilimi ve gerilim düşümü değerlerinden gerilim düşümü yüzdesini hesaplar.

    Parametreler:
        gerilim_dusumu (float): Gerilim düşümü (V)
        sistem_gerilimi (float): Sistem gerilimi (V)

    Döndürür:
        float: Gerilim düşümü yüzdesi (%)
    """
    if gerilim_dusumu < 0:
        raise ValueError("Gerilim düşümü sıfır veya pozitif olmalıdır.")
    
    if sistem_gerilimi <= 0:
        raise ValueError("Sistem gerilimi pozitif olmalıdır.")

    return (gerilim_dusumu / sistem_gerilimi) * 100