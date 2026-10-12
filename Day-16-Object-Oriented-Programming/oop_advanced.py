class Calisan:
    zam_orani = 1.1

    def __init__(self,isim,soyisim,maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim.lower() + soyisim.lower() + "@gmail.com"

    def biligleri_goset(self):
        return f"Ad: {self.isim} Soyad: {self.soyisim} maas: {self.maas} email: {self.email}"

calisan1 =  Calisan("Ali", "Çalışkan",5000)
#print(calisan1.biligleri_goset())
print("-------------------------")
calisan2 = Calisan("Veli", "Uzun",6000)
#print(calisan2.biligleri_goset())
print("--------------------------")

class Yazilimci(Calisan):
    zam_orani = 1.2

    def __init__(self,isim,soyisim,maas,bildigi_dil):
        super().__init__(isim,soyisim,maas)
        self.bildigi_dil = bildigi_dil

    def biligleri_goset(self):
        return f"Ad: {self.isim} Soyad: {self.soyisim} maas: {self.maas} email: {self.email} Dil: {self.bildigi_dil}"

    def dilini_soyle(self):
        return f"Bildiği dil: {self.bildigi_dil}"

yazilimci1 = Yazilimci("Ayşe","Yıldız",7000,"Python")
#print(yazilimci1.biligleri_goset())
print("---------------------------")
yazilimci2 = Yazilimci("Fatma","Ay",8000,"Java")
#print(yazilimci2.biligleri_goset())
print("---------------------------")

class Yonetici(Calisan):

    def __init__(self,isim,soyisim,maas,calisanlar = None):
        super().__init__(isim,soyisim,maas)
        if calisanlar == None:
            self.calisanlar = []
        else:
            self.calisanlar = calisanlar
    def calisan_ekle(self,calisan):
        if calisan not in self.calisanlar:
            self.calisanlar.append(calisan)
    def calisan_silme(self,calisan):
        if calisan in self.calisanlar:
            self.calisanlar.remove(calisan)
    def calisanlari_goster(self):
        for calisan in self.calisanlar:
            print(calisan.biligleri_goset())

yonetici1 = Yonetici("Metin","Ali", 10000)
yonetici1.calisan_ekle(yazilimci1)
yonetici1.calisan_ekle(yazilimci2)
yonetici1.calisanlari_goster()
