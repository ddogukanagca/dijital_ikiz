# Dijital İkiz · Digital Twin

![Python](https://img.shields.io/badge/Python-3-3776AB?style=flat&logo=python&logoColor=white)

[Türkçe](#türkçe) · [English](#english)

---

## Türkçe

Bir kişinin bir konuyu ne kadar anladığını ölçen, zayıf kaldığı beceriyi tekrar çalıştırıp yeniden ölçen ve raporlayan Python uygulaması.
İlk konu: **C dilinde koşullar**. İleride yeni konular eklenecek.

### Nasıl çalışır?

1. Her beceri için soru sorulur.
2. Cevaba göre bilme olasılığı güncellenir (Bayesian Knowledge Tracing).
3. %60'ın altında kalan beceri anlatılır ve yeni sorular sorulur.
4. İlk ve son puanlar raporlanır (`rapor.txt`).

### Çalıştırma

Python 3 gerekir. Ek kütüphane gerekmez.

```
python bkt.py
```

### Örnek rapor

```
--- SON RAPOR ---
= ile ==: %67 -> %67 (yeterli)
mantıksal operatörler: %20 -> %84 (yeterli)
if / else: %67 -> %67 (yeterli)
```

### Dosyalar

| Dosya | Görevi |
|---|---|
| `bkt.py` | Ölçme, tekrar ve rapor |
| `sorular.py` | Sorular ve anlatımlar |

### Beceriler

- `=` ile `==` farkı
- Mantıksal operatörler
- `if / else`

### Sınırlamalar

- Model değerleri (başlangıç, tahmin, dikkatsizlik, öğrenme) elle seçildi, gerçek öğrenci verisiyle eğitilmedi.
- Her beceri için az sayıda soru var.
- Puanlar bir tahmindir; kesin bir başarı notu değildir.

---

## English

A Python app that measures how well a person understands a topic, re-teaches the weak skill, measures again and reports the result.
First topic: **conditionals in C**. More topics are planned. The app's interface is in Turkish.

### How it works

1. A question is asked for each skill.
2. The probability that the person knows the skill is updated after each answer (Bayesian Knowledge Tracing).
3. Skills below 60% are explained and tested with new questions.
4. The first and final scores are reported (`rapor.txt`).

### Run

Requires Python 3. No extra libraries.

```
python bkt.py
```

### Files

| File | Purpose |
|---|---|
| `bkt.py` | Measurement, review and report |
| `sorular.py` | Questions and explanations |

### Skills

- The difference between `=` and `==`
- Logical operators
- `if / else`

### Limitations

- Model parameters (initial, guess, slip, learning) were chosen by hand, not trained on real student data.
- There are only a few questions per skill.
- Scores are estimates, not a definitive grade.
