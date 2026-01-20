import sys

a = float(sys.argv[1])
b = sys.argv[2]

if b == "C" or b == "c":
    c = a * 9 / 5 + 32
    print(f"{a}°C = {c:.1f}°F")

elif b == "F" or b == "f":
    d = (a - 32) * 5 / 9
    print(f"{a}°F = {d:.1f}°C")

else:
    print("Fehler")
