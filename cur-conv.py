import sys

betrag = float(sys.argv[1])
waehrung = sys.argv[2]

if waehrung == "USD":
    kurs = 0.80
elif waehrung == "EUR":
    kurs = 0.93
elif waehrung == "GBP":
    kurs = 1.07
else:
    print("Unbekannte Währung")
    sys.exit()

chf = betrag * kurs
print(f"CHF {chf:.2f}")

