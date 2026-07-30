from menuler import (
    guc_modulu,
    ohm_modulu,
    enerji_modulu,
    hakkinda_modulu,
    uc_faz_modulu,
    gerilim_dusumu_modulu,
)

from utils import (
    secim_al,
    ana_menu,
)


def main() -> None:
    while True:
        ana_menu()

        secim = secim_al("Seçiminiz: ", [1, 2, 3, 4, 5, 6, 7])

        if secim == 1:
            guc_modulu()

        elif secim == 2:
            ohm_modulu()

        elif secim == 3:
            enerji_modulu()

        elif secim == 4:
            uc_faz_modulu()

        elif secim == 5:
            gerilim_dusumu_modulu()

        elif secim == 6:
            hakkinda_modulu()

        elif secim == 7:
            print()
            print("Program sonlandırılıyor...")
            break


if __name__ == "__main__":
    main()