# Dijital İkiz: Öğrenme Ölçme Uygulaması

Bir kişinin bir konuyu ne kadar anladığını ölçen, zayıf kaldığı
beceriyi tekrar çalıştırıp yeniden ölçen ve raporlayan Python uygulaması.
İlk konu: C dilinde koşullar. İleride yeni konular eklenecek.

## Nasıl çalışır?
1. Her beceri için soru sorulur.
2. Cevaba göre bilme olasılığı güncellenir (Bayesian Knowledge Tracing).
3. %60'ın altında kalan beceri anlatılır ve yeni sorular sorulur.
4. İlk ve son puanlar raporlanır (`rapor.txt`).

## Çalıştırma
Python 3 gerekir. Ek kütüphane gerekmez.

```
python bkt.py
```

## Dosyalar
| Dosya | Görevi |
|---|---|
| `bkt.py` | Ölçme, tekrar ve rapor |
| `sorular.py` | Sorular ve anlatımlar |

## Beceriler
- `=` ile `==` farkı
- Mantıksal operatörler
- `if / else`

## Sınırlamalar
- Model değerleri (başlangıç, tahmin, dikkatsizlik, öğrenme) elle
  seçildi, gerçek öğrenci verisiyle eğitilmedi.
- Her beceri için az sayıda soru var.
- Puanlar bir tahmindir; kesin bir başarı notu değildir.