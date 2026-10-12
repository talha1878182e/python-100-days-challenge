from datetime import date

class kisi:
    zam_orani = 1.1
    kisi_sayisi= 0
    def __init__(self, isim,yas):
        self.isim = isim
        self.yas = yas
        kisi.kisi_sayisi += 1
    def bilgileri_soyle(self):
        return f"ad: {self.isim} yaş:{self.yas}"

    @classmethod
    def kisi_sayisi_soyle(cls):
        return cls.kisi_sayisi
    @classmethod
    def string_ile_olustur(cls,str_):
        isim,yas = str_.split("-")
        return cls(isim,yas)
    @classmethod
    def dogum_yili_ile_olustur(cls,isim,dogum_yili):
        return cls(isim,date.today().year-dogum_yili)
    @staticmethod
    def dogum_yili_hesapla(kisi):
        return date.today().year-kisi.yas

kisi1 = kisi("Ali",20)
kisi2 = kisi("Veli",30)
kisi3=kisi.string_ile_olustur("Ahmet-40")
kisi4 = kisi.dogum_yili_ile_olustur("Talha",2007)
print(kisi4.isim,kisi4.yas)
print(kisi.dogum_yili_hesapla(kisi2))
