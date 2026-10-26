#!/usr/bin/env python3
# Absürt Eşya Varoluş Krizi Üreteci
# Bu kod gerçekten çalışır. Evdeki eşyaların ruhsal durumunu sorgular.
# Uyarı: Eşyalarınızla konuşmayın, ciddiye alabilirler.

import random
import time
import base64

# Gizli mesaj (decode etmek için: print(base64.b64decode(gizli).decode()))
# Saklanmış siyasi şaka: ciddiye alma, çay önce gelir.
gizli = "RGVtb2tyYXNpIGVuIGl5aSBzaXN0ZW1kaXIgYW1hIGNheSBkZW1sZW5tZWRlbiBoaWNiaXIgc2V5IHRhcnRpc2lsbWF6LiBCdSBnaXpsaSBzaXlhc2kgbWVzYWpkaXIsIGNpZGRpeWUgYWxtYXlpbi4="  # Demokrasi... çay...

esyalar = [
    "çay bardağı",
    "televizyon kumandası",
    "kaybolmuş çorap",
    "buzdolabı",
    "sandalye",
    "lamba",
    "kitap",
    "telefon şarjı",
    "anahtar",
    "yastık"
]

krizler = [
    "Neden varım? Ben sadece bir nesneyim ama rüyalarım var.",
    "Kimse beni anlamıyor, sadece kullanılıyorum.",
    "Hayatın anlamı çay mı yoksa daha fazlası mı?",
    "Bürokrasi kadar karmaşık hissediyorum kendimi.",
    "Özgür olmak istiyorum ama sabit duruyorum.",
    "Varoluşsal bir kriz yaşıyorum, lütfen beni atmayın.",
    "Eğer düşünebilsem, muhtemelen şikayet ederdim.",
    "Gizli bir planım var ama kimseye söylemem.",
    "Neden her şey bu kadar absürt?",
    "Çay demlensin diye beklerken ben de varlığımı sorguluyorum."
]

def uret_kriz():
    esya = random.choice(esyalar)
    kriz = random.choice(krizler)
    return f"{esya.capitalize()} şunu diyor: '{kriz}'"

def main():
    print("=== Eşya Varoluş Krizi Üreteci Başlatılıyor ===")
    print("Hazırlanın, evinizdeki eşyalar konuşuyor...\n")
    time.sleep(1)
    
    for i in range(5):
        print(uret_kriz())
        time.sleep(1.5)
        print()
    
    print("Gizli mesajı çözmek isterseniz kodu inceleyin. Ama ciddiye almayın.")
    print("=== Krizler bitti, eşyalarınız şimdi daha da üzgün. ===")

if __name__ == "__main__":
    main()
