class Kendaraan:
    def __init__(self, nama):
        print("-> (Parent __init__ dipanggil)")
        self.nama = nama

class Mobil(Kendaraan):
    def __init__(self, nama, jumlah_pintu):
        print("-> (Child __init__ dipanggil)")
        
        super().__init__(nama) 
        
        self.jumlah_pintu = jumlah_pintu
        print(f"   -> Mobil {self.nama} dengan {self.jumlah_pintu} pintu dibuat.")

xenia = Mobil("Xenia Hitam", 4)
print(f"Nama object: {xenia.nama}")