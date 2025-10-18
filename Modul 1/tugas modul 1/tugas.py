class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        return self.panjang * self.lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)


# Program utama
def main():
    print("=== Program Luas & Keliling Persegi Panjang ===")
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))

    persegi_panjang = PersegiPanjang(panjang, lebar)

    print(f"\nLuas Persegi Panjang     : {persegi_panjang.hitung_luas()}")
    print(f"Keliling Persegi Panjang : {persegi_panjang.hitung_keliling()}")


if __name__ == "__main__":
    main()
