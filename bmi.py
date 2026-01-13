kgroesse_cm = float(input("Körpergrösse in cm: "))
gewicht = float(input("Körpergewicht in kg: "))

groesse_m = groesse_cm / 100
bmi = gewicht / (groesse_m ** 2)

print(f"Dein Body-Mass-Index: {bmi:.2f}")

