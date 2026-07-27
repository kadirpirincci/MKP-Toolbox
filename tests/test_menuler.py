import builtins
import pytest

from menuler import (
    guc_modulu,
    uc_faz_modulu,
    uc_faz_aktif_guc_modulu,
    uc_faz_akim_modulu,
    uc_faz_gerilim_modulu,
    uc_faz_cos_phi_modulu,
)


def test_guc_modulu(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    girisler = iter([
        "220",
        "5",
        ""
    ])

    def fake_input(_: str) -> str:
        return next(girisler)

    monkeypatch.setattr(builtins, "input", fake_input)

    guc_modulu()

    cikti = capsys.readouterr()

    assert "1100" in cikti.out


def test_uc_faz_aktif_guc_modulu(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    girisler = iter([
        "400",
        "10",
        "0.8",
        ""
    ])

    def fake_input(_: str) -> str:
        return next(girisler)

    monkeypatch.setattr(builtins, "input", fake_input)

    uc_faz_aktif_guc_modulu()

    cikti = capsys.readouterr()

    assert "5542.56" in cikti.out
    assert "Aktif güç" in cikti.out

def test_uc_faz_akim_modulu(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    girisler = iter([
        "400",
        "5542.56",
        "0.8",
        ""
    ])

    def fake_input(_: str) -> str:
        return next(girisler)

    monkeypatch.setattr(builtins, "input", fake_input)

    uc_faz_akim_modulu()

    cikti = capsys.readouterr()

    assert "10" in cikti.out
    assert "Akım" in cikti.out

def test_uc_faz_gerilim_modulu(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    girisler = iter([
        "5542.56",
        "10",
        "0.8",
        ""
    ])

    def fake_input(_: str) -> str:
        return next(girisler)

    monkeypatch.setattr(builtins, "input", fake_input)

    uc_faz_gerilim_modulu()

    cikti = capsys.readouterr()

    assert "400" in cikti.out
    assert "Gerilim" in cikti.out

def test_uc_faz_cos_phi_modulu(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    girisler = iter([
        "5542.56",
        "400",
        "10",
        ""
    ])

    def fake_input(_: str) -> str:
        return next(girisler)

    monkeypatch.setattr(builtins, "input", fake_input)

    uc_faz_cos_phi_modulu()

    cikti = capsys.readouterr()

    assert "0.80" in cikti.out
    assert "Güç faktörü" in cikti.out

def test_uc_faz_modulu_akim(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    girisler = iter([
        "2",
        "400",
        "5542.56",
        "0.8",
        "",
        "5"
    ])

    def fake_input(_: str) -> str:
        return next(girisler)

    monkeypatch.setattr(builtins, "input", fake_input)

    uc_faz_modulu()

    cikti = capsys.readouterr()

    assert "10.00 A" in cikti.out
    assert "Akım" in cikti.out


def test_uc_faz_modulu_gerilim(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    girisler = iter([
        "3",
        "5542.56",
        "10",
        "0.8",
        "",
        "5"
    ])

    def fake_input(_: str) -> str:
        return next(girisler)

    monkeypatch.setattr(builtins, "input", fake_input)

    uc_faz_modulu()

    cikti = capsys.readouterr()

    assert "400" in cikti.out
    assert "Gerilim" in cikti.out


def test_uc_faz_modulu_cos_phi(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    girisler = iter([
        "4",
        "5542.56",
        "400",
        "10",
        "",
        "5"
    ])

    def fake_input(_: str) -> str:
        return next(girisler)

    monkeypatch.setattr(builtins, "input", fake_input)

    uc_faz_modulu()

    cikti = capsys.readouterr()

    assert "0.8" in cikti.out
    assert "Güç faktörü" in cikti.out