import sys

sec = int(sys.argv[1])

h = sec // 3600
m = (sec % 3600) // 60
s = sec % 60

print(f"{h}h{m}m{s}s")
