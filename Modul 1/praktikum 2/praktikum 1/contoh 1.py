class Mahasiswa:
    def __init__(self, nama, jurusan):
        self.nama = nama
        self.jurusan = jurusan

mhs = Mahasiswa("lilla", "PTI")

print(mhs.__dict__)