import builtins
import pytest
from utils import hesap_calistir, secim_al, sifir_ve_pozitif_sayi_al


def test_pozitif_sayi_al(monkeypatch: pytest.MonkeyPatch):
    def fake_input(_: str) -> str:
        return "25"

    monkeypatch.setattr(builtins, "input", fake_input)

    sonuc = sifir_ve_pozitif_sayi_al("Sayı: ")

    assert sonuc == 25


def test_negatif_sayi_reddedilir(monkeypatch: pytest.MonkeyPatch):
    girisler = iter(["-5", "10"])

    def fake_input(_: str) -> str:
        return next(girisler)

    monkeypatch.setattr(builtins, "input", fake_input)

    sonuc = sifir_ve_pozitif_sayi_al("Sayı: ")

    assert sonuc == 10


def test_gecerli_secim(monkeypatch: pytest.MonkeyPatch):
    def fake_input(_: str) -> str:
        return "2"

    monkeypatch.setattr(
        builtins,
        "input",
        fake_input
    )

    sonuc = secim_al("Seçim: ", [1, 2, 3])

    assert sonuc == 2


def test_hesap_calistir_basari():
    def toplama(a: int, b: int) -> int:
        return a + b

    sonuc = hesap_calistir(toplama, 5, 3)

    assert sonuc == 8


def test_hesap_calistir_hata():
    def hata_fonksiyonu() -> None:
        raise ValueError("Hata")

    sonuc = hesap_calistir(hata_fonksiyonu)

    assert sonuc is None