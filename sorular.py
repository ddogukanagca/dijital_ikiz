SORULAR = [
    {
        "beceri": "= ile ==",
        "kod": 'int x = 3;\nif (x = 5) printf("A"); else printf("B");',
        "dogru": "A",
        "aciklama": "x = 5 atamadır. 5 sıfır olmadığı için koşul doğrudur.",
    },
    {
        "beceri": "mantıksal operatörler",
        "kod": 'int x = 7;\nif (x > 5 && x < 7) printf("A"); else printf("B");',
        "dogru": "B",
        "aciklama": "&& için iki taraf da doğru olmalı. 7 < 7 yanlıştır.",
    },
    {
        "beceri": "if / else",
        "kod": 'int x = 0;\nif (x) printf("A"); else printf("B");',
        "dogru": "B",
        "aciklama": "C'de 0 yanlış sayılır, bu yüzden else çalışır.",
    },
]


TEKRAR = {
    "= ile ==": {
        "ders": "= değer atar, == iki değeri karşılaştırır.",
        "sorular": [
            {"kod": 'int x = 2;\nif (x == 5) printf("A"); else printf("B");', "dogru": "B"},
            {"kod": 'int x = 0;\nif (x = 0) printf("A"); else printf("B");', "dogru": "B"},
        ],
    },
    "mantıksal operatörler": {
        "ders": "&& için iki taraf da doğru olmalı, || için biri yeter, ! sonucu tersine çevirir.",
        "sorular": [
            {"kod": 'int x = 8;\nif (x < 5 || x > 7) printf("A"); else printf("B");', "dogru": "A"},
            {"kod": 'int x = 4;\nif (!(x == 4)) printf("A"); else printf("B");', "dogru": "B"},
        ],
    },
    "if / else": {
        "ders": "C'de 0 yanlıştır; 0 dışındaki her sayı doğrudur.",
        "sorular": [
            {"kod": 'int x = -1;\nif (x) printf("A"); else printf("B");', "dogru": "A"},
            {"kod": 'int x = 10;\nif (x > 10) printf("A"); else printf("B");', "dogru": "B"},
        ],
    },
}
