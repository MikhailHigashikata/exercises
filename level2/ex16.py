a = input().split()

for i, e in enumerate(a):
    if int(e) % 2:
        a[i] = str(int(e) ** 2)
        
print(', '.join(a))