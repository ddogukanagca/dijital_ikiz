# Dijital İkiz: C dilinde koşullar konusunda öğrenmeyi ölçen uygulama
# Yöntem: Bayesçi Bilgi İzleme (Bayesian Knowledge Tracing - BKT)

# Sorular ve tekrar içerikleri ayrı dosyada durur
from sorular import SORULAR, TEKRAR

# Her sorunun altında gösterilen şıklar
SORU_METNI = "A) A yazar  B) B yazar  C) derleme hatası  D) hiçbir şey yazmaz\nCevabın: "

# Cevaba göre kişinin beceriyi bilme olasılığını günceller
def guncelle(bilme, dogru):
    sans = 0.25          # bilmediği halde doğru yapma olasılığı (4 şık)
    dikkatsizlik = 0.10  # bildiği halde yanlış yapma olasılığı
    ogrenme = 0.15       # soruyu çözerken öğrenme olasılığı

    # Bu cevabın iki açıklaması: "biliyordu" ve "bilmiyordu"
    if dogru:
        biliyor = bilme * (1 - dikkatsizlik)
        bilmiyor = (1 - bilme) * sans
    else:
        biliyor = bilme * dikkatsizlik
        bilmiyor = (1 - bilme) * (1 - sans)

    # Bayes kuralı: cevabı gördükten sonra bilme olasılığı
    sonrasi = biliyor / (biliyor + bilmiyor)
    # Henüz bilmeyenlerin bir kısmı bu soruda öğrenmiş olabilir
    return sonrasi + (1 - sonrasi) * ogrenme

# Geçerli bir harf girilene kadar cevap ister
def cevap_al():
    while True:
        cevap = input(SORU_METNI).strip().upper()
        if cevap in ["A", "B", "C", "D"]:
            return cevap
        print("Lütfen A, B, C ya da D yaz.")


# Kişinin dijital ikizi: her becerinin bilme olasılığı
puanlar = {}

# 1. AŞAMA: İlk ölçüm
for soru in SORULAR:
    beceri = soru["beceri"]
    if beceri not in puanlar:
        puanlar[beceri] = 0.30  # başlangıç tahmini

    print()
    print(soru["kod"])
    cevap = cevap_al()

    dogru = cevap.strip().upper() == soru["dogru"]
    puanlar[beceri] = guncelle(puanlar[beceri], dogru)

    if dogru:
        print("Doğru!")
    else:
        print("Yanlış.", soru["aciklama"])

# İlk raporu yaz ve puanların kopyasını sakla
print()
ilk_puanlar = puanlar.copy()
print("--- RAPOR ---")
for beceri, puan in puanlar.items():
    print(f"{beceri}: %{puan * 100:.0f}")
    
# 2. AŞAMA: Zayıf becerileri anlat ve yeniden ölç
for beceri, puan in puanlar.items():
    if puan >= 0.60:  # yeterli beceri atlanır
        continue

    print()
    print("TEKRAR:", beceri)
    print(TEKRAR[beceri]["ders"])
    input("Okuyunca Enter'a bas...")

    # Aynı soru değil, yeni sorular sorulur (ezberi ölçmemek için)
    for soru in TEKRAR[beceri]["sorular"]:
        print()
        print(soru["kod"])
        cevap = cevap_al()
        dogru = cevap.strip().upper() == soru["dogru"]

        eski = puanlar[beceri]
        puanlar[beceri] = guncelle(eski, dogru)
        print(f"{beceri}: %{eski * 100:.0f} -> %{puanlar[beceri] * 100:.0f}")

        if puanlar[beceri] >= 0.60:  # sınır geçildiyse dur
            break


# 3. AŞAMA: Önce ve sonrayı karşılaştıran son rapor
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

# Raporu dosyaya kaydet
with open("rapor.txt", "w", encoding="utf-8") as dosya:
    dosya.write(rapor)