zarobekRoczny = float(input("podaj swój zaróbek"))

if zarobekRoczny <= 30000:
    print("masz zarobek roczny poniżej krajowej, twój zarobek stanowi: " , zarobekRoczny)
elif 120000 >= zarobekRoczny > 30000 :
    print("twój zarobek stanowi: " , zarobekRoczny , "podatek stanowi: ", ((zarobekRoczny * 12) / 100)-3600)
elif 1000000 >= zarobekRoczny > 120000:
    podatekO = 10800 + ((zarobekRoczny - 120000) * 0.32)
    print("twój zarobek stanowi: ", zarobekRoczny,  "podatek stanowi: ", podatekO)
else:
    print("Ale jasteś biliarderem XD")

#nadwyżka 120000 - 32%
