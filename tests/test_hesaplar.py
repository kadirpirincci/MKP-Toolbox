import pytest

from hesaplar import (
    guc_hesabi,
    akim_hesabi,
    gerilim_hesabi,
    direnc_hesabi,
    enerji_hesabi,
    uc_faz_akim_hesabi,
    uc_faz_guc_hesabi,
)


def test_guc_hesabi():
    sonuc = guc_hesabi(220, 5)

    assert sonuc == 1100


def test_akim_hesabi():
    sonuc = akim_hesabi(220, 10)

    assert sonuc == 22


def test_gerilim_hesabi():
    sonuc = gerilim_hesabi(5, 10)

    assert sonuc == 50


def test_direnc_hesabi():
    sonuc = direnc_hesabi(220, 10)

    assert sonuc == 22


def test_enerji_hesabi():
    sonuc = enerji_hesabi(2, 5)

    assert sonuc == 10


def test_akim_hesabi_sifir_direnc():
    with pytest.raises(ValueError):
        akim_hesabi(220, 0)


def test_direnc_hesabi_sifir_akim():
    with pytest.raises(ValueError):
        direnc_hesabi(220, 0)


def test_uc_faz_guc_hesabi():
    sonuc = uc_faz_guc_hesabi(400, 10, 0.8)

    assert sonuc == pytest.approx(5542.56, rel=1e-4)


def test_uc_faz_guc_hesabi_gecersiz_cos_phi():
    with pytest.raises(ValueError):
        uc_faz_guc_hesabi(400, 10, 1.2)


def test_uc_faz_guc_hesabi_negatif_gerilim():
    with pytest.raises(ValueError):
        uc_faz_guc_hesabi(-400, 10, 0.8)


def test_uc_faz_guc_hesabi_negatif_akim():
    with pytest.raises(ValueError):
        uc_faz_guc_hesabi(400, -10, 0.8)


def test_uc_faz_akim_hesabi():
    sonuc = uc_faz_akim_hesabi(400, 15000, 0.85)

    assert sonuc == pytest.approx(25.47, rel=1e-3)


def test_uc_faz_akim_hesabi_sifir_gerilim():
    with pytest.raises(ValueError):
        uc_faz_akim_hesabi(0, 15000, 0.85)


def test_uc_faz_akim_hesabi_negatif_gerilim():
    with pytest.raises(ValueError):
        uc_faz_akim_hesabi(-400, 15000, 0.85)


def test_uc_faz_akim_hesabi_negatif_guc():
    with pytest.raises(ValueError):
        uc_faz_akim_hesabi(400, -15000, 0.85)


def test_uc_faz_akim_hesabi_gecersiz_cos_phi():
    with pytest.raises(ValueError):
        uc_faz_akim_hesabi(400, 15000, 0)