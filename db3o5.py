total = 0
for a in range(1, 100):
    if a % 3 == 0 or a % 5 == 0:
        total += a
print(total)
