import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

if a**2 + b**2 == c**2:
	print("Triplet!")
else:
	print("Kein Triplet!")
