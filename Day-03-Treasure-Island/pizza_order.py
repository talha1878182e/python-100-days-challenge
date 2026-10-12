print("*********************************************")
print("*****Welcome to Python Pizza Deliveries!*****")
print("*********************************************")

price = 0
extras = {
    "Jambon": 15,
    "Pepperoni": 15,
    "Sucuk": 15,
    "Sosis": 15,
    "Köz Biber": 15,
    "Mısır": 10,
    "Mozerella": 25,
    "Pizza Sos": 8,
    "Siyah Zeytin": 10,
    "Yeşil Biber": 20,
    "Soğan": 10,
    "Domates": 10,
    "Mantar": 15,
    "BBQ Sos": 8,
    "Ballı Hardal Sos": 8,
    "Susam": 1.5,
    "Kekik": 1.5,
    "Pastırma": 45,
    "Ton Balığı": 50,
    "Ketçap": 8
}

drinks = {
    "Coca-Cola 330mL" : 90,
    "Coca-Cola 1L" : 130,
    "Coca-Cola Zero 330ml" : 90,
    "Coca-Cola Zero 1L" : 130,
    "Sütaş Ayran 300mL" : 55,
    "Sütaş Ayran 1L" : 130,
    "FuesTea Şeftali 330mL" : 130,
    "FuesTea Şeftali 1L" : 90,
    "RED Bull Energy Drink 250mL" : 125,
    "Damla Su 500mL" : 40,
    "FuesTea Limon 1L": 130,
    "FuesTea Limon 330L" : 90
}

print("\nHangi pizzayı istersiniz?")
print("______MENU______")
print("Süperix","Classical","Sucuklu","Vegetarian",sep="\n")
print("________________")

choose_pizza = input("\nHangisini seçiyorsunuz?: ")


if choose_pizza == "Süperix":
    price = 470
elif choose_pizza == "Classical":
    price = 400
elif choose_pizza == "Sucuklu":
    price = 430
elif choose_pizza == "Vegetarian":
    price = 500
else:
    print("Geçersiz pizza seçimi!")

if price > 0:

    pizza_extra = input("Pizzada herhangi bir değişiklik yapmak ister misiniz? Evet ise Y'ye, Hayır ise N'ye basın: ")
    if pizza_extra == "Y":
        print("-----Extra Menu-----")
        print("Ekstra Jambon = 15 TL ","Ekstra Pepperoni = 15 TL ","Ekstra Sucuk = 15 TL ")
        print("Ekstra Sosis = 15 TL ", "Ekstra Köz Biber = 15 TL ", "Ekstra Mısır = 10 TL ")
        print("Ekstra Mozerella = 25 TL ", "Ekstra Pizza Sos = 8 TL ", "Ekstra Siyah Zeytin  = 10 TL ")
        print("Ekstra Yeşil Biber = 20 TL ", "Ekstra Soğan = 10 TL ", "Ekstra Domates = 10 TL ")
        print("Ekstra Mantar = 15 TL ", "Ekstra Acı Chili Baharatı = 8 TL ", "Ekstra Dominos Sos = 8 TL ")
        print("Ekstra BBQ Sos = 8 TL ", "Ekstra Balllı Haradal Sos = 8 TL ", "Ekstra Susam = 1.5 TL ")
        print("Ekstra Kekik = 1.5 TL ", "Ekstra Pastırma = 45 TL ", "Ekstra Ton Balığı = 50 TL ")
        print("Ekstra Ketcap = 8 TL ")
        print("---------------------")

        choose_extra = input("Choose extra: ")

        if choose_extra in extras:
            price += extras[choose_extra]
            print(f"{choose_extra} eklendi. Yeni Toplam Tutarınız: {price} TL")
        else:
            print("Geçersiz ekstra seçimi!")

    choose_drink_ask = input("İçecek ister misiniz? Evet ise Y'ye, Hayır ise N'ye basın: ")
    if choose_drink_ask == "Y":
        print("-----İçecek Menu-----")
        print("Coca-Cola 330mL = 90 TL ","Coca-Cola 1L = 130 TL","Coca-Cola Zero 330mL = 90 TL")
        print("Coca-Cola Zero 1L = 130TL", "Sütaş Ayran 300mL = 55 TL", "Sütaş Ayran 1L = 130 TL")
        print("FuesTea Şeftali 330mL = 90 TL", "FuesTea Şeftali 1L = 130 TL ", "RED Bull Energy Drink 250mL = 125 TL")
        print("Damla Su 500mL = 40 TL", "FuesTea Limon 1L = 130 TL ", "FuesTea Limon 330mL = 90 TL")
        print("---------------------")

        choose_drink = input("İçeceğinizi yazınız: ")
        if choose_drink in drinks:
            price += drinks[choose_drink]
            print(f"{choose_drink} eklendi. Yeni Toplam Tutarınız: {price} TL")
        else:
            print("Geçersiz içecek seçimi!")

    print(f"\nSiparişiniz tamamlandı! Toplam Ödenecek Tutar: {price} TL")
