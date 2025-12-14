class Ayah:
    def __init__(self, nama_ayah):
        self.nama_ayah = nama_ayah
    
    def bekerja(self):
        print(f"{self.nama_ayah} sedang bekerja.")

class Ibu:
    def __init__(self, nama_ibu):
        self.nama_ibu = nama_ibu

    def memasak(self):
        print(f"{self.nama_ibu} sedang memasak.")

class Anak(Ayah, Ibu):
    def __init__(self, nama_anak, nama_ayah, nama_ibu):
        Ayah.__init__(self, nama_ayah)
        Ibu.__init__(self, nama_ibu)
        self.nama_anak = nama_anak

    def bermain(self):
        print(f"{self.nama_anak} sedang bermain.")

budi = Anak("Budi", "Hendra (Ayah)", "Wati (Ibu)")

budi.bekerja()
budi.memasak() 
budi.bermain()