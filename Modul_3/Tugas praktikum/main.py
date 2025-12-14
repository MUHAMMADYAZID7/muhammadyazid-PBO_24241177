# Kelas dasar Pegawai (superclass)
# Menyimpan data umum pegawai: nama, NIP, gaji pokok
class Pegawai:
    # Konstruktor: mengisi data pegawai saat objek dibuat
    def __init__(self, nama: str, nip: str, gaji_pokok: int):
        self.nama = nama                 # Menyimpan nama pegawai
        self.nip = nip                   # Menyimpan NIP pegawai
        self.__gaji_pokok = int(gaji_pokok)  # Gaji pokok (PRIVATE, tidak bisa diakses langsung)

    # Mengambil nilai gaji pokok (karena variabelnya private)
    def get_gaji_pokok(self) -> int:
        return self.__gaji_pokok

    # Bonus default untuk pegawai biasa (nol)
    def hitung_bonus(self) -> int:
        return 0

    # Menghitung gaji total = gaji pokok + bonus
    def get_gaji_total(self) -> int:
        return self.__gaji_pokok + self.hitung_bonus()

    # Menampilkan informasi pegawai
    def tampilkan_info(self) -> str:
        return f"Nama: {self.nama}, NIP: {self.nip}\nGaji Pokok: {format_rp(self.__gaji_pokok)}"


# Kelas Manager adalah turunan dari Pegawai
# Memiliki fitur tambahan: tunjangan jabatan dan bonus 15%
class Manager(Pegawai):
    # Konstruktor Manager (menambah tunjangan jabatan)
    def __init__(self, nama: str, nip: str, gaji_pokok: int, tunjangan_jabatan: int):
        super().__init__(nama, nip, gaji_pokok)  # Memanggil konstruktor Pegawai
        self.tunjangan_jabatan = int(tunjangan_jabatan)

    # Manager mendapat bonus 15% dari gaji pokok
    def hitung_bonus(self) -> int:
        return int(self.get_gaji_pokok() * 0.15)

    # Menampilkan info tambahan untuk Manager
    def tampilkan_info(self) -> str:
        base = super().tampilkan_info()  # Info dasar dari Pegawai
        return base + f"\nTunjangan: {format_rp(self.tunjangan_jabatan)}"


# Kelas StaffTeknis, turunan Pegawai
# Mendapat bonus berdasarkan jumlah proyek
class StaffTeknis(Pegawai):
    # Konstruktor Staff Teknis (menambah jumlah proyek)
    def __init__(self, nama: str, nip: str, gaji_pokok: int, jumlah_proyek: int):
        super().__init__(nama, nip, gaji_pokok)
        self.jumlah_proyek = int(jumlah_proyek)

    # Bonus diperoleh dari 500 ribu x jumlah proyek
    def hitung_bonus(self) -> int:
        return 500_000 * self.jumlah_proyek

    # Menampilkan tambahan info jumlah proyek
    def tampilkan_info(self) -> str:
        base = super().tampilkan_info()
        return base + f"\nJumlah Proyek: {self.jumlah_proyek}"


# Fungsi untuk memformat angka menjadi format rupiah
def format_rp(amount: int) -> str:
    return "Rp " + format(int(amount), ",d")


# Bagian utama program
if __name__ == '__main__':

    # Membuat objek Manager dan StaffTeknis
    manager = Manager("Budi Hartono", "M-001", 10_000_000, tunjangan_jabatan=5_000_000)
    staff = StaffTeknis("Susi Susanti", "S-001", 6_000_000, jumlah_proyek=3)

    # Output info Manager
    print("--- Info Manager ---")
    print(manager.tampilkan_info())
    print(f"Gaji Total Manager: {format_rp(manager.get_gaji_total())}\n")

    print("==============================\n")

    # Output info Staff Teknis
    print("--- Info Staff Teknis ---")
    print(staff.tampilkan_info())
    print(f"Gaji Total Staff: {format_rp(staff.get_gaji_total())}\n")

    print("==============================\n")

    # Tes Encapsulation (keamanan data)
    print("--- Tes Keamanan (Encapsulasi) ---")
    try:
        # Percobaan mengakses gaji pokok secara langsung (akan error)
        print(staff.__gaji_pokok)
    except AttributeError as e:
        print(f"ERROR: {e}")
        print("-> TIDAK BISA diakses langsung dari luar!")

    # Gaji tetap benar dihitung melalui method resmi
    print(f"Gaji Total Susi (tetap): {format_rp(staff.get_gaji_total())}")
