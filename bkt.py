from sorular import SORULAR, TEKRAR

SORU_METNI = "A) A yazar  B) B yazar  C) derleme hatası  D) hiçbir şey yazmaz\nCevabın: "

def guncelle(bilme, dogru):
    sans = 0.25
    dikkatsizlik = 0.10
    ogrenme = 0.15

    if dogru:
        biliyor = bilme * (1 - dikkatsizlik)
        bilmiyor = (1 - bilme) * sans
    else:
        biliyor = bilme * dikkatsizlik
        bilmiyor = (1 - bilme) * (1 - sans)

    sonrasi = biliyor / (biliyor + bilmiyor)
    return sonrasi + (1 - sonrasi) * ogrenme

def cevap_al():
    while True:
        cevap = input(SORU_METNI).strip().upper()
        if cevap in ["A", "B", "C", "D"]:
            return cevap
        print("Lütfen A, B, C ya da D yaz.")


puanlar = {}

for soru in SORULAR:
    beceri = soru["beceri"]
    if beceri not in puanlar:
        puanlar[beceri] = 0.30

    print()
    print(soru["kod"])
    cevap = cevap_al()

    dogru = cevap.strip().upper() == soru["dogru"]
    puanlar[beceri] = guncelle(puanlar[beceri], dogru)

    if dogru:
        print("Doğru!")
    else:
        print("Yanlış.", soru["aciklama"])

print()
ilk_puanlar = puanlar.copy()
print("--- RAPOR ---")
for beceri, puan in puanlar.items():
    print(f"{beceri}: %{puan * 100:.0f}")
    
for beceri, puan in puanlar.items():
    if puan >= 0.60:
        continue

    print()
    print("TEKRAR:", beceri)
    print(TEKRAR[beceri]["ders"])
    input("Okuyunca Enter'a bas...")

    for soru in TEKRAR[beceri]["sorular"]:
        print()
        print(soru["kod"])
        cevap = cevap_al()
        dogru = cevap.strip().upper() == soru["dogru"]

        eski = puanlar[beceri]
        puanlar[beceri] = guncelle(eski, dogru)
        print(f"{beceri}: %{eski * 100:.0f} -> %{puanlar[beceri] * 100:.0f}")

        if puanlar[beceri] >= 0.60:
            break


satirlar = ["--- SON RAPOR ---"]

for beceri, puan in puanlar.items():
    if puan >= 0.60:
        durum = "yeterli"
    else:
        durum = "tekrar gerekli"

    satirlar.append(f"{beceri}: %{ilk_puanlar[beceri] * 100:.0f} -> %{puan * 100:.0f} ({durum})")

rapor = "\n".join(satirlar)
print()
print(rapor)

with open("rapor.txt", "w", encoding="utf-8") as dosya:
    dosya.write(rapor)