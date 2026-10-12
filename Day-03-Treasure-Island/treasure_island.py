import sys
import time

print("""
                    |>>>                        |>>>
                    |                           |
                _  _|_  _                   _  _|_  _
               | |_| |_| |                 | |_| |_| |
                 .      /                   .    .  /
                    ,  /                        .  /
                 | .   |_   _   _   _   _   _| ,   |
                 |    .| |_| |_| |_| |_| |_| |  .  |
                 | ,   | .    .     .      . |    .|
                 |   . |  .     . .   .  ,   |.    |
     ___----_____| .   |.   ,  _______   .   |   , |---~_____
_---~            |     |  .    +++++++    . | .   |         ~---_
                 |.    | .    |+++++++| .    |   . |              ~-_
              __ |   . |   ,  |+++++++|.  . _|__   |                 ~-_
     ____--`~    '--~~__ .    |++++ __|----~    ~`---,              ___^~-__
-~--~                   ~---__|,--~'                  ~~----_____-~'   `~----~
""")

user_me_name = "TalhaCBC"
user_me_password = "123123"

print("Welcome to the Treasure Castle")
user_ask = input("Oyuna kayıtlı mısınız? (evet / hayır): ").strip().lower()

if user_ask == "hayır":
    print("____________Kayıt Ekranı____________")
    user_me_name = input("|   Username: ")
    user_me_password = input("|   Password: ")
    print("____________________________________")
    print("Kayıt başarılı! Giriş yapılıyor...\n")

elif user_ask == "evet":
    print("____________Giriş Ekranı____________")
    user_name_registered = input("Username: ")
    user_password_registered = input("Password: ")

    if user_name_registered == user_me_name and user_password_registered == user_me_password:
        print("Bilgiler kontrol ediliyor...")
        time.sleep(1.5)
        print("Giriş Başarılı!\n")
    else:
        print("Giriş bilgileri hatalı! Oyundan çıkarılıyorsunuz.")
        sys.exit()
time.sleep(1)
print("""
██╗██╗██╗███████╗██╗     ██████╗  ██████╗ ███╗   ███╗███████╗
██║██║██║██╔════╝██║    ██╔════╝ ██╔═══██╗████╗ ████║██╔════╝
██║██║██║█████╗  ██║    ██║      ██║   ██║██╔████╔██║█████╗  
██║██║██║██╔══╝  ██║    ██║      ██║   ██║██║╚██╔╝██║██╔══╝  
╚██████╔╝███████╗███████╗██████╔╝╚██████╔╝██║ ╚═╝ ██║███████╗
 ╚═════╝ ╚══════╝╚══════╝╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚══════╝
""")

time.sleep(1.5)
print("Kalede bir hazine var!!")
print("Kapı kilitli.")
time.sleep(1)

print("Kaleye girişi nasıl yapacaksınız?")
kapi_giris = input("Tırmanarak (T) - Kapıyı zorlayarak (K): ").strip().upper()

if kapi_giris == "T":
    print("Tırmanırken ayağınız kaydı, düştünüz ve öldünüz! 💀")
    sys.exit()
elif kapi_giris == "K":
    print("Kapı açıldı!")
else:
    print("Geçersiz hamle yaptığınız için yakalandınız!")
    sys.exit()

time.sleep(1)
print("Dikkatli olun, içeride muhafızlar var...")
time.sleep(0.5)
print("Önünde iki seçenek var:")

merdiven = input("Sağ Merdiven (Sağ) - Sol Merdiven (Sol): ").strip().capitalize()

if merdiven == "Sağ":
    print("Karşına muhafız çıktı! !!YAKALANDINIZ!!")
    time.sleep(1)
    print("Hücredesin...")
    time.sleep(1)

    hucre_kacis = input("Hücreden çıkmak ister misiniz? (Evet / Hayır): ").strip().capitalize()
    if hucre_kacis == "Evet":
        print("Hücreden kaçtınız, çabuk olun!")
        print("Yukarı kata çıktınız.")
    else:
        print("Hücrede çürüyüp gittiniz... !KAYBETTİNİZ!")
        sys.exit()

elif merdiven == "Sol":
    print("Sessizce yukarı kata çıktınız.")

time.sleep(1)
kapi = input("3 kapı var, birini seçin (A / B / C): ").strip().upper()

if kapi == "A":
    print("Yanlış kapı! Karşınıza çıkan aslan sizi yedi. 🦁 !KAYBETTİNİZ!")
elif kapi == "B":
    print("Doğru kapı! Hazineyi buldunuz! 🎉")
    time.sleep(1)
    print(""" 
██╗    ██╗██╗███╗   ██╗
██║    ██║██║████╗  ██║
██║ █╗ ██║██║██╔██╗ ██║
██║███╗██║██║██║╚██╗██║
╚███╔███╔╝██║██║ ╚████║
 ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝
""")
elif kapi == "C":
    print("Burası boş bir oda! Tuzak kapısı kapandı. !KAYBETTİNİZ!")
else:
    print("Yanlış kapı seçimi yaptınız.")
