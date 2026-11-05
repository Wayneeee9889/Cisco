zarobekRoczny = float(input("podaj swój zaróbek"))

if zarobekRoczny <= 30000:
    print("masz zarobek roczny poniżej krajowej, twój zarobek stanowi: " , zarobekRoczny)
elif zarobekRoczny > 30000 < 120000:
    print("twój zarobek stanowi: " , zarobekRoczny , "podatek stanowi: ", ((zarobekRoczny * 12) / 100)-3600)
elif zarobekRoczny >= 120000:
    print("twój zarobek stanowi: ", zarobekRoczny,  "podatek + danina solidarnościowa stanowi: ", ((((zarobekRoczny * 12) / 100) - 3600)*32) /100)
