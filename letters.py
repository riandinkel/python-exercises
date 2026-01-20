import sys

c = sys.argv[1]

match c:
    case "a" | "e" | "i" | "o" | "u":
        print(f"'{c}' ist ein Vokal")
    case "b" | "c" | "d" | "f" | "g" | "h" | "j" | "k" | "l" | "m" | "n" | "p" | "q" | "r" | "s" | "t" | "v" | "w" | "x" | "y" | "z":
        print(f"'{c}' ist ein Konsonant")
    case _:
        print(f"'{c}' ist unbekannt")
