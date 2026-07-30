import pytest

from hesaplar import (
    guc_hesabi,
    akim_hesabi,
    gerilim_hesabi,
    direnc_hesabi,
    enerji_hesabi,
    uc_faz_guc_hesabi,
    uc_faz_akim_hesabi,
    uc_faz_gerilim_hesabi,
    uc_faz_cos_phi_hesabi,
    tek_faz_gerilim_dusumu_hesabi,
    uc_faz_gerilim_dusumu_hesabi,
    gerilim_dusumu_yuzdesi_hesabi,
)


# ==================================================
# TEMEL HESAPLAR
# ==================================================

def test_guc_hesabi():
    sonuc = guc_hesabi(
        220,
        5,
    )

    assert sonuc == 1100


def test_akim_hesabi():
    sonuc = akim_hesabi(
        220,
        10,
    )

    assert sonuc == 22


def test_akim_hesabi_sifir_direnc():
    with pytest.raises(ValueError):
        akim_hesabi(
            220,
            0,
        )


def test_gerilim_hesabi():
    sonuc = gerilim_hesabi(
        5,
        10,
    )

    assert sonuc == 50


def test_direnc_hesabi():
    sonuc = direnc_hesabi(
        220,
        10,
    )

    assert sonuc == 22


def test_direnc_hesabi_sifir_akim():
    with pytest.raises(ValueError):
        direnc_hesabi(
            220,
            0,
        )


def test_enerji_hesabi():
    sonuc = enerji_hesabi(
        2,
        5,
    )

    assert sonuc == 10


# ==================================================
# ÜÇ FAZ GÜÇ HESABI
# ==================================================

def test_uc_faz_guc_hesabi():
    sonuc = uc_faz_guc_hesabi(
        400,
        10,
        0.8,
    )

    assert sonuc == pytest.approx(5542.56, rel=1e-4)


def test_uc_faz_guc_hesabi_sifir_gerilim():
    sonuc = uc_faz_guc_hesabi(
        0,
        10,
        0.8,
    )

    assert sonuc == 0


def test_uc_faz_guc_hesabi_sifir_akim():
    sonuc = uc_faz_guc_hesabi(
        400,
        0,
        0.8,
    )

    assert sonuc == 0


def test_uc_faz_guc_hesabi_sifir_cos_phi():
    sonuc = uc_faz_guc_hesabi(
        400,
        10,
        0,
    )

    assert sonuc == 0


def test_uc_faz_guc_hesabi_birim_cos_phi():
    sonuc = uc_faz_guc_hesabi(
        400,
        10,
        1,
    )

    assert sonuc == pytest.approx(4000 * 3 ** 0.5)


def test_uc_faz_guc_hesabi_negatif_gerilim():
    with pytest.raises(ValueError):
        uc_faz_guc_hesabi(
            -400,
            10,
            0.8,
        )


def test_uc_faz_guc_hesabi_negatif_akim():
    with pytest.raises(ValueError):
        uc_faz_guc_hesabi(
            400,
            -10,
            0.8,
        )


def test_uc_faz_guc_hesabi_gecersiz_cos_phi():
    with pytest.raises(ValueError):
        uc_faz_guc_hesabi(
            400,
            10,
            1.2,
        )


# ==================================================
# ÜÇ FAZ AKIM HESABI
# ==================================================

def test_uc_faz_akim_hesabi():
    sonuc = uc_faz_akim_hesabi(
        400,
        15000,
        0.85,
    )

    assert sonuc == pytest.approx(25.47, rel=1e-3)


def test_uc_faz_akim_hesabi_sifir_gerilim():
    with pytest.raises(ValueError):
        uc_faz_akim_hesabi(
            0,
            15000,
            0.85,
        )


def test_uc_faz_akim_hesabi_negatif_gerilim():
    with pytest.raises(ValueError):
        uc_faz_akim_hesabi(
            -400,
            15000,
            0.85,
        )


def test_uc_faz_akim_hesabi_sifir_guc():
    with pytest.raises(ValueError):
        uc_faz_akim_hesabi(
            400,
            0,
            0.85,
        )


def test_uc_faz_akim_hesabi_gecersiz_cos_phi():
    with pytest.raises(ValueError):
        uc_faz_akim_hesabi(
            400,
            15000,
            0,
        )


# ==================================================
# ÜÇ FAZ GERİLİM HESABI
# ==================================================

def test_uc_faz_gerilim_hesabi():
    sonuc = uc_faz_gerilim_hesabi(
        5542.56,
        10,
        0.8,
    )

    assert sonuc == pytest.approx(400, rel=1e-4)


def test_uc_faz_gerilim_hesabi_sifir_akim():
    with pytest.raises(ValueError):
        uc_faz_gerilim_hesabi(
            5542.56,
            0,
            0.8,
        )


def test_uc_faz_gerilim_hesabi_sifir_guc():
    with pytest.raises(ValueError):
        uc_faz_gerilim_hesabi(
            0,
            10,
            0.8,
        )


def test_uc_faz_gerilim_hesabi_gecersiz_cos_phi():
    with pytest.raises(ValueError):
        uc_faz_gerilim_hesabi(
            5542.56,
            10,
            0,
        )


# ==================================================
# ÜÇ FAZ GÜÇ FAKTÖRÜ HESABI
# ==================================================

def test_uc_faz_cos_phi_hesabi():
    sonuc = uc_faz_cos_phi_hesabi(
        5542.56,
        400,
        10,
    )

    assert sonuc == pytest.approx(0.8, rel=1e-4)


def test_uc_faz_cos_phi_hesabi_sifir_guc():
    with pytest.raises(ValueError):
        uc_faz_cos_phi_hesabi(
            0,
            400,
            10,
        )


def test_uc_faz_cos_phi_hesabi_sifir_gerilim():
    with pytest.raises(ValueError):
        uc_faz_cos_phi_hesabi(
            5542.56,
            0,
            10,
        )


def test_uc_faz_cos_phi_hesabi_sifir_akim():
    with pytest.raises(ValueError):
        uc_faz_cos_phi_hesabi(
            5542.56,
            400,
            0,
        )


def test_uc_faz_cos_phi_hesabi_fiziksel_olarak_gecersiz():
    with pytest.raises(ValueError):
        uc_faz_cos_phi_hesabi(
            10000,
            400,
            10,
        )


# ==================================================
# TEK FAZ GERİLİM DÜŞÜMÜ
# ==================================================

def test_tek_faz_gerilim_dusumu_hesabi():
    sonuc = tek_faz_gerilim_dusumu_hesabi(
        0.0175,
        10,
        5,
        2.5,
    )

    assert sonuc == pytest.approx(0.7)


def test_tek_faz_gerilim_dusumu_hesabi_sifir_ozdirenc():
    with pytest.raises(ValueError):
        tek_faz_gerilim_dusumu_hesabi(
            0,
            10,
            5,
            2.5,
        )


def test_tek_faz_gerilim_dusumu_hesabi_sifir_uzunluk():
    with pytest.raises(ValueError):
        tek_faz_gerilim_dusumu_hesabi(
            0.0175,
            0,
            5,
            2.5,
        )


def test_tek_faz_gerilim_dusumu_hesabi_sifir_akim():
    with pytest.raises(ValueError):
        tek_faz_gerilim_dusumu_hesabi(
            0.0175,
            10,
            0,
            2.5,
        )


def test_tek_faz_gerilim_dusumu_hesabi_sifir_kesit():
    with pytest.raises(ValueError):
        tek_faz_gerilim_dusumu_hesabi(
            0.0175,
            10,
            5,
            0,
        )


# ==================================================
# ÜÇ FAZ GERİLİM DÜŞÜMÜ
# ==================================================

def test_uc_faz_gerilim_dusumu_hesabi():
    sonuc = uc_faz_gerilim_dusumu_hesabi(
        0.0175,
        10,
        5,
        2.5,
    )

    assert sonuc == pytest.approx(0.6062, rel=1e-4)


def test_uc_faz_gerilim_dusumu_hesabi_sifir_ozdirenc():
    with pytest.raises(ValueError):
        uc_faz_gerilim_dusumu_hesabi(
            0,
            10,
            5,
            2.5,
        )


def test_uc_faz_gerilim_dusumu_hesabi_sifir_uzunluk():
    with pytest.raises(ValueError):
        uc_faz_gerilim_dusumu_hesabi(
            0.0175,
            0,
            5,
            2.5,
        )


def test_uc_faz_gerilim_dusumu_hesabi_sifir_akim():
    with pytest.raises(ValueError):
        uc_faz_gerilim_dusumu_hesabi(
            0.0175,
            10,
            0,
            2.5,
        )


def test_uc_faz_gerilim_dusumu_hesabi_sifir_kesit():
    with pytest.raises(ValueError):
        uc_faz_gerilim_dusumu_hesabi(
            0.0175,
            10,
            5,
            0,
        )


# ==================================================
# GERİLİM DÜŞÜMÜ YÜZDESİ
# ==================================================

def test_gerilim_dusumu_yuzdesi_hesabi():
    sonuc = gerilim_dusumu_yuzdesi_hesabi(
        10,
        220,
    )

    assert sonuc == pytest.approx(4.54545, rel=1e-3)


def test_gerilim_dusumu_yuzdesi_hesabi_sifir_dusum():
    sonuc = gerilim_dusumu_yuzdesi_hesabi(
        0,
        220,
    )

    assert sonuc == 0


def test_gerilim_dusumu_yuzdesi_hesabi_negatif_gerilim_dusumu():
    with pytest.raises(ValueError):
        gerilim_dusumu_yuzdesi_hesabi(
            -1,
            220,
        )


def test_gerilim_dusumu_yuzdesi_hesabi_sifir_sistem_gerilimi():
    with pytest.raises(ValueError):
        gerilim_dusumu_yuzdesi_hesabi(
            10,
            0,
        )