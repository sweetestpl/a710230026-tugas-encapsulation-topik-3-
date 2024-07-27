class Musisi:
    def _init_(self, genre, jenis_vokal):
        self.__genre = genre
        self.__jenis_vokal = jenis_vokal

    def bernyanyi(self, lagu):
        print(f"Musisi {self._genre} dengan vokal {self._jenis_vokal} sedang bernyanyi lagu {lagu}")

    def menari(self, gaya_tari):
        print(f"Musisi {self._genre} dengan vokal {self._jenis_vokal} sedang menari dengan gaya {gaya_tari}")

    # Getter untuk genre
    def get_genre(self):
        return self.__genre

    # Setter untuk genre
    def set_genre(self, genre):
        self.__genre = genre

    # Getter untuk jenis_vokal
    def get_jenis_vokal(self):
        return self.__jenis_vokal

    # Setter untuk jenis_vokal
    def set_jenis_vokal(self, jenis_vokal):
        self.__jenis_vokal = jenis_vokal

# Contoh penggunaan class Musisi
musisi1 = Musisi("Pop", "Soprano")
musisi1.bernyanyi("Anugerah Terindah yang Pernah Kumiliki")
musisi1.menari("Hip-hop")

musisi2 = Musisi("Rock", "Tenor")
musisi2.bernyanyi("Bohemian Rhapsody")
musisi2.menari("Breakdance")

# Membuat objek baru dan mengakses variabel private menggunakan getter dan setter
musisi3 = Musisi("Jazz", "Alto")
print(f"Genre musisi3: {musisi3.get_genre()}")
print(f"Jenis vokal musisi3: {musisi3.get_jenis_vokal()}")

musisi3.set_genre("Blues")
musisi3.set_jenis_vokal("Baritone")
print(f"Genre baru musisi3: {musisi3.get_genre()}")
print(f"Jenis vokal baru musisi3: {musisi3.get_jenis_vokal()}")