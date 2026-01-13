import sys

AHV = 8.7
IV = 1.4
EO = 0.5
ALV = 1.1
NBU = 0.73
PK = 8.9

brutto = float(sys.argv[1])

ahv = brutto * AHV / 100
iv  = brutto * IV / 100
eo  = brutto * EO / 100
alv = brutto * ALV / 100
nbu = brutto * NBU / 100
pk  = brutto * PK / 100

netto = brutto - (ahv + iv + eo + alv + nbu + pk)

print(f"Bruttolohn     {brutto:.2f}")
print(f"AHV:           -{ahv:.2f}")
print(f"IV:            -{iv:.2f}")
print(f"EO:            -{eo:.2f}")
print(f"ALV:           -{alv:.2f}")
print(f"NBU:           -{nbu:.2f}")
print(f"PK:            -{pk:.2f}")
print(f"Nettolohn:     {netto:.2f}")
