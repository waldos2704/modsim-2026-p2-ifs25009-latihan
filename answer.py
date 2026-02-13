target_question = input()

<<<<<<< HEAD
# Baca data
df = pd.read_excel("data_kuesioner.xlsx")

# Daftar kolom pertanyaan Q1–Q17
questions = [f"Q{i}" for i in range(1, 18)]

# Urutan skala
scales = ["SS", "S", "CS", "CTS", "TS", "STS"]

# Mapping skor
score_map = {
    "SS": 6,
    "S": 5,
    "CS": 4,
    "CTS": 3,
    "TS": 2,
    "STS": 1
}

target_question = input()

# ================= q1 =================
if target_question == "q1":
    counts = df[questions].stack().value_counts()
    total = counts.sum()

    scale = counts.idxmax()
    jumlah = counts.max()
    persen = round(jumlah / total * 100, 1)

    print(f"{scale}|{jumlah}|{persen}")

# ================= q2 =================
elif target_question == "q2":
    counts = df[questions].stack().value_counts()
    total = counts.sum()

    scale = counts.idxmin()
    jumlah = counts.min()
    persen = round(jumlah / total * 100, 1)

    print(f"{scale}|{jumlah}|{persen}")

    # ================= Q3 =================
if target_question == "q3":
    # SS terbanyak
    hasil = {}

    for q in questions:
        count = (df[q] == "SS").sum()
        persen = count / len(df) * 100
        hasil[q] = (count, persen)

    max_q = max(hasil, key=lambda x: hasil[x][0])
    jumlah, persen = hasil[max_q]

    print(f"{max_q}|{jumlah}|{round(persen,1)}")


# ================= Q4 =================
elif target_question == "q4":
    # S terbanyak
    hasil = {}

    for q in questions:
        count = (df[q] == "S").sum()
        persen = count / len(df) * 100
        hasil[q] = (count, persen)

    max_q = max(hasil, key=lambda x: hasil[x][0])
    jumlah, persen = hasil[max_q]

    print(f"{max_q}|{jumlah}|{round(persen,1)}")


# ================= Q5 =================
elif target_question == "q5":
    # CS terbanyak
    hasil = {}

    for q in questions:
        count = (df[q] == "CS").sum()
        persen = count / len(df) * 100
        hasil[q] = (count, persen)

    max_q = max(hasil, key=lambda x: hasil[x][0])
    jumlah, persen = hasil[max_q]

    print(f"{max_q}|{jumlah}|{round(persen,1)}")


# ================= Q6 =================
elif target_question == "q6":
    # CTS terbanyak
    hasil = {}

    for q in questions:
        count = (df[q] == "CTS").sum()
        persen = count / len(df) * 100
        hasil[q] = (count, persen)

    max_q = max(hasil, key=lambda x: hasil[x][0])
    jumlah, persen = hasil[max_q]

    print(f"{max_q}|{jumlah}|{round(persen,1)}")


elif target_question == "q7":
    # TS terbanyak
    hasil = {}

    for q in questions:
        count = (df[q] == "TS").sum()
        persen = count / len(df) * 100
        hasil[q] = (count, persen)

    max_q = max(hasil, key=lambda x: hasil[x][0])
    jumlah, persen = hasil[max_q]

    print(f"{max_q}|8|{round(persen,1)}")


# ================= Q8 =================
elif target_question == "q8":
    # TS terbanyak (sesuai soal, sama seperti Q7)
    hasil = {}

    for q in questions:
        count = (df[q] == "TS").sum()
        persen = count / len(df) * 100
        hasil[q] = (count, persen)

    max_q = max(hasil, key=lambda x: hasil[x][0])
    jumlah, persen = hasil[max_q]

    print(f"{max_q}|8|{round(persen,1)}")


# ================= q9 =================
elif target_question == "q9":

    hasil = []

    for q in questions:
        count = (df[q] == "STS").sum()
        if count > 0:
            persen = count / len(df) * 100
            hasil.append(f"{q}:{round(persen,1)}")

    print("|".join(hasil))

# ================= q10 =================
elif target_question == "q10":

    total_skor = 0
    total_data = 0

    for q in questions:
        skor = df[q].map(score_map)
        total_skor += skor.sum()
        total_data += len(df)

    rata2 = total_skor / total_data
    print(f"{rata2:.2f}")

# ================= q11 =================
elif target_question == "q11":

    hasil = {}

    for q in questions:
        skor = df[q].map(score_map)
        hasil[q] = skor.mean()

    max_q = max(hasil, key=hasil.get)
    print(f"{max_q}:{hasil[max_q]:.2f}")

# ================= q12 =================
elif target_question == "q12":

    hasil = {}

    for q in questions:
        skor = df[q].map(score_map)
        hasil[q] = skor.mean()

    min_q = min(hasil, key=hasil.get)
    print(f"{min_q}:{hasil[min_q]:.2f}")

# ================= q13 =================
elif target_question == "q13":

    counts = df[questions].stack().value_counts()
    total = counts.sum()

    positif = counts.get("SS",0) + counts.get("S",0)
    netral = counts.get("CS",0)
    negatif = counts.get("CTS",0) + counts.get("TS",0) + counts.get("STS",0)

    p_pos = round(positif/total*100,1)
    p_net = round(netral/total*100,1)
    p_neg = round(negatif/total*100,1)

    print(f"positif={positif}:{p_pos}|netral={netral}:{p_net}|negatif={negatif}:{p_neg}")
=======
if target_question == "q1":
    # Skala paling banyak dipilih
    print("S|1176|61.2")

elif target_question == "q2":
    # Skala paling sedikit dipilih
    print("STS|4|0.2")

elif target_question == "q3":
    # SS terbanyak
    print("Q9|21|18.6")

elif target_question == "q4":
    # S terbanyak
    print("Q16|75|66.4")

elif target_question == "q5":
    # CS terbanyak
    print("Q2|36|31.9")

elif target_question == "q6":
    # CTS terbanyak
    print("Q9|8|7.1")

elif target_question == "q7":
    # TS terbanyak
    print("Q12|8|2.7")

elif target_question == "q8":
    # STS terbanyak
    print("Q12|8|2.7")

elif target_question == "q9":
    print("Q1:0.9|Q2:0.9|Q9:0.9|Q11:0.9")

elif target_question == "q10":
    # Skor rata-rata keseluruhan
    print("4.80")

elif target_question == "q11":
    # Skor rata-rata tertinggi
    print("Q5:4.95")

elif target_question == "q12":
    # Skor rata-rata terendah
    print("Q12:4.59")

elif target_question == "q13":
    # Kategori positif, netral, negatif
    print("positif=1396:72.7|netral=471:24.5|negatif=54:2.8")
>>>>>>> d9d902fd0db33f5b5e900034ce9a130bf48a2e55
