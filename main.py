def ektraksi_data():
    """
    Tampilan Data hasil Ekstrak :

    Tanggal     : 21 Juni 2025
    Waktu       : 20:18:50 WIB
    Magnitudo   : 4.0
    Kedalaman   : 40 km
    Lokasi      : LS=1.48 Bt:134.01
    Pusat Gempa : Pusat gempa berada di laut 6 km barat daya Amalatu, Seram Bagian Barat
    Dirasakan   : Dirasakan (Skala MMI): II-III Ambon, II-III Saparua, II-III Amahai
    """
    hasil = dict()
    hasil['tanggal'] = ['21 Juni 2025']
    hasil['waktu']  = ['20:18:50 WIB']
    print(hasil)
    return hasil

def tampilkan_data(result):
    pass

if __name__ == '__main__':
    print("Aplikasi Utama")
    result = ektraksi_data()
    tampilkan_data(result)